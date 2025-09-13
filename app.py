import os
from jinja2 import Template
from markupsafe import escape
from core.functions import *
from core.templates_registry import TEMPLATES
from flask import Flask, jsonify, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = os.urandom(32)  # generates a random key at startup

@app.route("/test-expression", methods=["POST"])
def test_expression():
    data = request.get_json(force=True)
    expression = data.get("expression")
    try:
        output = Template(expression).render()
        return jsonify({
            "received": True,
            "expression": expression,
            "output": escape(output)
        })
    except Exception as e:
        return jsonify({
            "received": True,
            "expression": expression,
            "error": escape(e)
        })        

@app.route("/", methods=["GET", "POST"])
def index():
    rendered = None
    selected_key = None
    submitted_params = {}

    if request.method == "GET":
        selected_key = request.args.get("action_key")

    if request.method == "POST":
        selected_key = request.form.get("action_key")
        entry = get_template_by_key(selected_key) if selected_key else None
        if not entry:
            flash("Please select a valid action.", "error")
        else:
            params, errors = validate_and_collect_params(entry, request.form)
            if errors:
                for err in errors:
                    flash(err, "error")
            else:
                try:
                    if selected_key == "test_ssti_jinja_expression":
                        rendered = entry["expression"].format(generate_random_expression())
                        submitted_params = generate_random_expression()
                    else:
                        print(entry["expression"])
                        rendered = entry["expression"].format(**params)
                        submitted_params = params                       
                except KeyError as exc:
                    flash(f"Missing parameter for template: {exc}", "error")
                except Exception as exc:
                    flash("Error formatting expression.", "error")

    items = sorted(TEMPLATES["items"], key=lambda x: x["label"])

    if request.method == "GET" and not selected_key and items:
        selected_key = items[0].get("key")
    return render_template(
        "index.html",
        items=items,
        selected_key=selected_key,
        rendered=rendered,
        submitted_params=submitted_params,
        app_version=TEMPLATES.get("version", 1),
    )


if __name__ == "__main__":
    port = 5000
    host="0.0.0.0"
    app.run(host, port=port)



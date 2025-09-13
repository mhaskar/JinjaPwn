import random
from .templates_registry import TEMPLATES

def get_template_by_key(key):
    for item in TEMPLATES.get("items", []):
        if item.get("key") == key:
            return item
    return None


def coerce_type(value, field_type):
    return value.strip()


def validate_and_collect_params(entry, form_data):
    errors = []
    collected = {}

    params_spec = entry.get("params", [])
    for spec in params_spec:
        name = spec.get("name")
        label = spec.get("label", name)
        field_type = spec.get("type", "text")
        required = bool(spec.get("required", False))
        choices = spec.get("choices")

        raw_value = form_data.get(name, "").strip()
        custom_value = form_data.get(f"{name}_custom", "").strip()

        if required and not (raw_value or custom_value):
            errors.append(f"Missing required field: {label}")
            continue

        if field_type == "select":
            if custom_value:
                collected[name] = coerce_type(custom_value, "text")
            else:
                if raw_value and choices and raw_value not in choices:
                    errors.append(f"Invalid value for {label}")
                    continue
                if raw_value:
                    collected[name] = coerce_type(raw_value, field_type)
        else:
            if custom_value:
                collected[name] = coerce_type(custom_value, "text")
            elif raw_value:
                collected[name] = coerce_type(raw_value, field_type)

    return collected, errors

def generate_random_expression():
        expressions = []
        r1 = random.randint(1, 300)
        r2 = random.randint(1, 300)
        rr1 = f"{r1}*{r2}"
        expressions.append(rr1)
        
        r3 = random.randint(1, 300)
        r4 = random.randint(1, 300)
        rr2 = f"{r3}+{r4}"
        expressions.append(rr2)

        return random.choice(expressions)

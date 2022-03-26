import os
import requests


os.environ['HTTPS_PROXY'] = 'http://USiyQvWcT7wcpy8gvFb1GVmz:2b48a642-615a-4b3c-8db5-e02a88147174@tntsfeqzp4a.sandbox.verygoodproxy.com:8080'
response = requests.post('https://echo.apps.verygood.systems/post',
                         json={"card_holder": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM",
                               "card_number": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM",
                                "card_cvc": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM",
                                "card_exp": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM"
                                },
                         verify='certs/sandbox.pem')
print(str(response.text))

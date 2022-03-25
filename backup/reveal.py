import os
import requests

os.environ['HTTPS_PROXY'] = 'http://USiyQvWcT7wcpy8gvFb1GVmz:2b48a642-615a-4b3c-8db5-e02a88147174@tntsfeqzp4a.sandbox.verygoodproxy.com:8080'
response = requests.post('https://echo.apps.verygood.systems/post',
                         json={'account_number': 'tok_sandbox_w8CBfH8vyYL2xWSmMWe3Ds'},
                         verify='path/to/sandbox.pem')
print(str(response.text))

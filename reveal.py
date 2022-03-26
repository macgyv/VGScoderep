import os
import requests


os.environ['HTTPS_PROXY'] = 'http://USrD8iSwgj98rX49amoGYiqk:500edfdf-0831-4105-a512-a7d3fd1e9c9d@tnte6doqz8w.sandbox.verygoodproxy.com:8080'
response = requests.post('https://tnte6doqz8w.sandbox.verygoodproxy.com/post',
                         json={"card_holder": "tok_sandbox_5sCQ2zmHN4LRSwxk95tR2s",
                               "card_number": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM",
                                "card_cvc": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM",
                                "card_exp": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM"
                                },
                         verify='certs/sandbox.pem')
print(str(response.text))

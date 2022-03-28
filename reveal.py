import os
import requests


os.environ['HTTPS_PROXY'] = 'http://USrD8iSwgj98rX49amoGYiqk:500edfdf-0831-4105-a512-a7d3fd1e9c9d@tnte6doqz8w.sandbox.verygoodproxy.com:8080'
response = requests.post('https://echo.apps.verygood.systems/post',
                         json={"card_cvc": "tok_sandbox_f83HNxhZBgrAywnNTFvwpw",
                                "card_exp": "tok_sandbox_7ipuvMaUtLVePy2Kw17vKY",
                                "card_holder": "tok_sandbox_a975PkDRGeRqMbMPheSfou",
                                "card_number": "tok_sandbox_kv3zXsHRyqcqabBdhwJrc2"
                                },
                         verify='certs/sandbox.pem')
print(str(response.text))


"""
echo.apps.verygood.systems
api.stripe.com

https://tnte6doqz8w.sandbox.verygoodproxy.com/post

"card_holder": "tok_sandbox_xAxE4mH7NM3pdQP5YiqzWD",
      "card_number": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM",
       "card_cvc": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM",
       "card_exp": "tok_sandbox_tAk4ChGh7aGxgmmcKbxufM"

"""

import requests

response = requests.post("https://tnte6doqz8w.sandbox.verygoodproxy.com/post",
                          json={ 'card_holder': 'Oliver Pajarillo',
                                 'card_number': '4242424242424242',
                                 'card_cvc': '123',
                                 'card_exp': '03/28'})
print(str(response.text))

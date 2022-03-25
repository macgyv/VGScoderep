import requests

response = requests.post("https://tntkpxaxman.sandbox.verygoodproxy.com/post",
                          json={'account_number': 'ACn9AUkpAgeVhRrJRb1LMMGF'})
print(str(response.text))

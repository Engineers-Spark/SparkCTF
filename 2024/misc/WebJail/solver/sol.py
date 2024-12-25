import requests

p = "''.join('a' for _ in range(1000))"
r = requests.post('http://localhost:2501',d={'user_input':p})
print(r.text)
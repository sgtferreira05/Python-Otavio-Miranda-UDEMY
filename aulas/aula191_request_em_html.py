# Requests for requests HTTP resources in Python

import requests

url = 'http://127.0.0.1:5500/aulas/aula190_site/index.html'
response = requests.get(url)
print(response.status_code)  # 200 OK
print(response.headers['Content-Type'])  # text/html; charset=UTF-8
print(response.text)  # HTML content of the page
print(response.url)  # URL of the page
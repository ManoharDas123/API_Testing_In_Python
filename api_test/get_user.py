import requests

response = requests.get("https://reqres.in/api/users?page=2")

code = response.status_code

assert code == 200,"Code doesn't match"

# print(response.text)
# print(response.content)
print(response.json())
print(type(response.headers))
print(response.headers)
print(response.cookies)
print(response.url)
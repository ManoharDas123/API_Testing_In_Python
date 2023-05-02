import requests
import json

# payload = {
#     "name": "Manohar",
#     "job": "Automation"
# }
mydata = open("data.json", "r").read()
# print(type(payload))
response = requests.post("https://reqres.in/api/users", data=json.loads(mydata))
print(response)
print(response.json())
print(response.headers.get("Content-Type"))
assert response.json()['job'] == 'Engineer'

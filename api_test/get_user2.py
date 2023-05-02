import requests

p = {"page":2}
response = requests.get("https://reqres.in/api/users",params=p)
print(response.url)

json_response = response.json()
print(json_response['total'])
assert json_response['total']==12
print(json_response['total_pages'])
assert json_response['total_pages']==2 , "Total pages count is not matching"
print(json_response["data"][0]["email"])
print(json_response["data"][0]["first_name"])
print(json_response["data"][2]["last_name"])
assert json_response["data"][2]["last_name"]!=None

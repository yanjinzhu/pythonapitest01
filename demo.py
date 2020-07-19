import requests
url = "http://192.168.1.100:8082/login"
data = {"username":"lucy","password":"123456"}
headers = {"Content-Type":"application/json"}
r = requests.post(url,json=data, headers= headers)

cookie = r.headers.get("set-cookie")
headers["cookie"]=cookie

print(headers)

url = "http://192.168.1.100:8082/teachers"
r = requests.get(url, headers = headers)

print(r.text)
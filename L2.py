import requests
import json

request = requests.post("http://cit-home1.herokuapp.com/api/register",
                        data=json.dumps({'message':'Try to register'}),
                        headers={'content-type': 'application/json'})

if request.status_code == 200:
    print("It is ok")
    request = requests.get("http://cit-home1.herokuapp.com/api/check_me")
    print(request)
else:
    print("Try to send again")


import requests
import json

URL="http://127.0.0.1:8000/teacher/register/"
data={'teacher_id':'2253'}
json_data=json.dumps(data)
r=requests.delete(url=URL,data=json_data)
# data=r.json()
# print(data)
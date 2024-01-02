import json
import requests

URL='http://127.0.0.1:8000/teacher/register/'

data={'teacher_id':'2253','name':'Akbar Sami','course':'JAVA',
      'seat':6,'duration':5}

json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)
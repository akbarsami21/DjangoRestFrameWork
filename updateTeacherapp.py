import requests
import json

URL='http://127.0.0.1:8000/teacher/register/'

data={'teacher_id':'2269','name':'Sami','course':'Java',
      'seat':7,'duration':2}
json_data=json.dumps(data)
r=requests.put(url=URL,data=json_data)
data=r.json()
print(data)
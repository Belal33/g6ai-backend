import requests
from os import stat
url = 'http://127.0.0.1:8000/api/v1/chat/voice/'
file_path = 'AI_Modules_hameed.webm'

size = stat(file_path).st_size
with open(file_path, 'rb') as f:
    # files = {'file': f}
    # headers = {'Content-Disposition': 'attachment; filename="{}"'.format(file_path)}
    # response = requests.post(url, files=files,headers=headers)
    
    response = requests.post(url, files={"file": f})


print(response.status_code)
print(response.content)
print(response.json())

print(size)
# print(response.content)
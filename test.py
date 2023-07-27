import requests
response = requests.get('https://api-tau-vert.vercel.app/api/python')
print(response.text)
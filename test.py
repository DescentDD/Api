import re
import requests

response = requests.get('https://api-tau-vert.vercel.app/api/python.py')
print(response.text)
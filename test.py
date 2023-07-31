import re
import requests

response = requests.get('https://github.com/gxywy/pixiv-daily')
pattern = r'<a href="(https://pixiv.microyu.workers.dev.*?)" rel=.*?>.*?</a>'

matches = re.findall(pattern, response.text)
for match in matches:
    print(match)
    image_url = match
    image_response = requests.get(image_url, stream=True)
    if image_response.status_code == 200:
        image_name = image_url.split('/')[-1]
        with open('api/img/'+image_name, 'wb') as image_file:
            for chunk in image_response.iter_content(1024):
                image_file.write(chunk)
        print(f"Successfully downloaded: {image_name}")
    else:
        print(f"Failed to download: {image_url}")

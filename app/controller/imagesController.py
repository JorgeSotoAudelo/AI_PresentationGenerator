import requests
import urllib.parse
class imageController:

    def __init__(self):
        self.api_key = '37240249-b6a284da7936917de819e23e0'

    def searchImage(self,query):
        api_key = '37240249-b6a284da7936917de819e23e0'
        url = f"https://pixabay.com/api/?key={api_key}&q={urllib.parse.quote(query)}"
        response = requests.get(url,timeout=5)
        data = response.json()
        if 'hits' in data:
            if len(data['hits']) > 0:
                image_url = data['hits'][0]['largeImageURL']
                return image_url
            
    def downloadImage(self,url):
        response = requests.get(url,timeout=5)
        if response.status_code == 200:
            image_data = response.content
            image_path = 'temp.jpg'
            with open(image_path, 'wb') as file:
                file.write(image_data)
            return image_path
        return None

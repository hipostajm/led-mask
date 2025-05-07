import requests

class AppApiConnector:
    def __init__(self):
        pass

    def send_image(self, IP: str, image:list):
        print('dziłam')
        requests.post(json={"image": image}, url=IP+"/set-all/")
    
    def send_animated_image(self, IP:str, frames:list):
        requests.post(url=IP+"/animate/", json={"frames": frames})
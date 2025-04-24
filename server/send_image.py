import requests

def send_image(data: dict, IP: str, route: str, method):
    method(verify=False,url=IP+route, json=data)
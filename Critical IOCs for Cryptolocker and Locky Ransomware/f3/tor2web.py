import requests

def connect_to_tor2web(url):
    response = requests.get(url)
    print(response.text)

connect_to_tor2web("https://duskgytldkxiuqc6.onion.to/")

#https://duskgytldkxiuqc6.onion.to/
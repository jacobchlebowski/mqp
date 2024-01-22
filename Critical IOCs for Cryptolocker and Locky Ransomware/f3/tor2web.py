import requests

def connect_to_tor2web(url):
    tor2web_url = "https://your-tor2web-instance.onion.to/"
    
    # Construct the full Tor2web URL
    full_url = tor2web_url + url
    
    # Make a request to the Tor2web URL
    response = requests.get(full_url)
    
    # Print the content of the response
    print(response.text)

# Example usage
connect_to_tor2web("example-onion-site.onion")

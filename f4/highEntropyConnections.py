import requests

def simulate_connection(domain):
    try:
        url = f"{domain}"
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Successfully connected to {domain}")
        else:
            print(f"Failed to connect to {domain}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to {domain}: {str(e)}")

# Desired high entropy domain names
high_entropy1 = "http://a1b2c3d4e5.example.com"
high_entropy2 = "http://x8b4l3p2q9c1r7s0.example.com"
high_entropy3 = "http://x9y8z7w6v5.example.com"
high_entropy4 = "http://q1r2s3t4u5.example.com.example.com"
high_entropy5 = "http://m1n2o3p4q5.example.com"

# Simulate connections to high entropy domain names
simulate_connection(high_entropy1)
simulate_connection(high_entropy2)
simulate_connection(high_entropy3)
simulate_connection(high_entropy4)
simulate_connection(high_entropy5)
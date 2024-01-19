import httpx

proxy_url = "http://n000000930:20235Kaonick@tpisa:80"
proxies = {"http://": proxy_url, "https://": proxy_url}

# Verify our IP address without proxy first to this website
response = httpx.get("https://www.whatismyip.com/")
print("IP address without proxy:", response.text)

# And then we request through proxy
with httpx.Client(proxies=proxies) as client:
    response = client.get("https://www.whatismyip.com/")
    print("IP address with proxy:", response.text)
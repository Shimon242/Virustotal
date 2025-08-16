import requests

url = "https://www.virustotal.com/api/v3/files/b2ca6801358313925007c590d3f1c4e9c66593a6e510b0cf623eae0863c8e419"

headers = {
    "accept": "application/json",
    "x-apikey": "a076c992eeae14dc25c91425d01619338f7a7381c6421383036269407428"
}

response = requests.get(url, headers=headers)

print(response.text)

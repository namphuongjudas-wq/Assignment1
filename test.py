#10.4
import requests
request = "http://127.0.0.1:5000/airport/LFLL"
response = requests.get(request).json()
print(response)

#10.3
import requests
request = "http://127.0.0.1:5000/prime_number/31"
response = requests.get(request).json()
print(response)
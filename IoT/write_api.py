import requests
import random
import time
api_key = 'Your write api key'
while True:
  temp = random.randint(20,50)
  humd = random.randint(50,100)
  print(temp,humd)
  url = f"https://api.thingspeak.com/update?api_key={api_key}&field1={temp}&field2={humd}"
  payload = {}
  headers = {}
  response = requests.request("GET", url, headers=headers, data=payload)
  print(response.text)
  time.sleep(15)

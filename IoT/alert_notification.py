import requests
import time
import json
channel_id = your channel id;

while True:
  url = "https://api.thingspeak.com/channels/{channel_id}/feeds.json?results=1" # Copy your Read API request and change results to 1
  response = requests.request("GET", url)
  op = response.json()['feeds'][0]['field1']
  op = int(op)
  print(op)
  url = "https://api.thingspeak.com/alerts/send"

  payload = json.dumps({
  "subject": "Temp High",
  "body": f"Above 40 degrees. Its {op}"})

  headers = {
    'ThingSpeak-Alerts-API-Key': '', # Put your Alerts API key here
    'Content-Type': 'application/json'}

  if(op>40): 
    # 40 is the threshold value
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    
  time.sleep(10)

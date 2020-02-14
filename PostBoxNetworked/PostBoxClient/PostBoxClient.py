from datetime import datetime
import os
import requests

url = "http://127.0.0.1:8000"
_endpoint = "/PostBox.txt"

while True:
    r = requests.get(url + _endpoint, verify = False)
    
    os.system('cls')
    fileData = r.text
    fileData = fileData.split("\n")

    for line in fileData:
        print(line)
        
    userInput = input(">>> ")
    payload = {"input": userInput.replace(" ", "_")}
    
    requests.get(url + _endpoint, params = payload)

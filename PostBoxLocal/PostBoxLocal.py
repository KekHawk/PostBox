from datetime import datetime
import os

with open ("PostBox.txt", "a+") as postBox:
    while True:
        os.system('cls')
        postBox.seek(0)
        fileData = list(map(str.strip, postBox.readlines()))

        for line in fileData:
            print(line)

            
        userInput = input(">>> ")

        

        postBox.write("[" + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "]  " + userInput + "\n")


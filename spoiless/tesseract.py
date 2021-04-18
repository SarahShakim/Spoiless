import pytesseract
import re
import json
import numpy as np
import matplotlib.pyplot as plt
import random
import math

amount = True
grocery = []
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
extracted_text = pytesseract.image_to_string(r'C:\Users\User\Desktop\machacks\goast\walmart2.jpg')
receipt_ocr = {}

product_pattern = (r'([0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9])')
product = re.findall(product_pattern, extracted_text)


# Opening JSON file  S
f = open(r'C:\Users\User\Desktop\machacks\goast\receiptData.json') 

# returns JSON object as  
info = json.load(f) 

for i in product: #checks the product numbers for the items in the json file
    for j in info: #checks the product number on receipt
    #print(i['Name'])
        if j['productNumber'] == i:
            #print(j['Name'])
            empty = list(j['bestbefore'])
            data = list(j['days'])
            if j['category'] == 'fruit':
                index = 2
            elif j['category'] == 'grain':
                index = 2
            elif j['category'] == 'vegetable':
                index = 3
            elif j['category'] == 'meat':
                index = 3.5
            elif j['category'] == 'dairy':
                index = 1.5
            
            x = np.linspace(2, 9, 100)
            equation = np.polyfit(data, empty, 1) #average spoil index
            y = np.polyfit(data, empty, 1)[0]*x + np.polyfit(data, empty, 1)[1]
            plt.plot(x, y, '-r', label='Regret')
            close_to_spoil = math.floor((index - equation[1]) / equation[0])
            plt.plot(data, empty)
            plt.grid() 
            # plt.show()
            print(j['Name'] + " is fresh for another " + str(close_to_spoil) + " days")
            
        #replace this with the graph
        else: 
            continue





#add date time module to warn user when expiry is close
#update days in JSON to adjust to different users and multiple receipts
#make a front end
#make notifications

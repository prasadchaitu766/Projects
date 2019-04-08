import math
import random
import requests
contact=int(input("enter a number"))

digits = "0123456789"
OTP = ""
for x in range(4):
    OTP += digits[math.floor(random.random() * 10)]
url="https://www.fast2sms.com/dev/bulk"
payload="sender_id=FSTSMS&message="+"OTP FOR Registration in E commerce:"+OTP+"&language=english&route=p&numbers="+str(contact)
headers={
    'authorization':"RLt1hZ2zaJpd6KnVG0ovSfOsgNADT9WlEIjwB754MQkrymcXuHh3TCb5LH8D2swouqWrPc6EtgeAfIOy",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-control': "no-cache"
}
response=requests.request("POST",url,data=payload,headers=headers)
print(response.text)
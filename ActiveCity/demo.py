import json
from email import message

d1 = json.loads(message)
if d1["return"]:
    print("return")
else:
    print("not return")
import os
import requests
import time 


#res = requests.get(f"https://tg.kootahkon.ir/bot{tg_token}/sendPhoto?chat_id=295600320&photo=https://9497-2a01-5ec0-e001-adbe-216a-285b-14ce-2cdd.ngrok.io/{picname}.jpg")
before = before = dict ([(f, None) for f in os.listdir ('activities')])
print(before)

while True:
    time.sleep(2)
    after = dict ([(f, None) for f in os.listdir ('activities')])
    added = [f for f in after if not f in before]
    if len(added) > 0:
        added = added.sort()
        print(added[0])
    before = after
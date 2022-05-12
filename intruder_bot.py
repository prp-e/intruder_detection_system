import os
import requests

tg_token = os.getenv("BOT_API")
requests.get(f"https://tg.kootahkon.ir/bot{tg_token}/sendMessage?chat_id=295600320&text=Intruder entered the room")

import os
import time
from datetime import datetime
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, path):
        self.observer = Observer()
        self.path = path

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if "jpg" in event.src_path:
            print(event.src_path)
            event = event.src_path.split('/')
            res = requests.get(f"https://tg.kootahkon.ir/bot{os.getenv('BOT_API')}/sendPhoto?chat_id={os.getenv('CHAT_ID')}&photo={os.getenv('SERVER_ADDRESS')}/{event[-1]}&caption={datetime.now()}\nIntruder activity")

if __name__ == "__main__":
    w = Watcher("activities")
    w.run()
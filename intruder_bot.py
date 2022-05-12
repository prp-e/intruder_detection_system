import os
import time
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
            res = requests.get(f"https://tg.kootahkon.ir/bot{os.getenv('BOT_API')}/sendMessage?chat_id=295600320&text=Intruder entered the room. this is evidence:\n https://f2ad-2a01-5ec0-e001-adbe-216a-285b-14ce-2cdd.ngrok.io/{event.src_path}")

if __name__ == "__main__":
    w = Watcher("activities")
    w.run()
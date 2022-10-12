import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:path"

class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"{event.src_path} foi criado")

    def on_deleted(self, event):
        print(f"{event.src_path} foi excluído")

    def on_modified(self, event):
        print(f"{event.src_path} foi modificado")
    
    def on_moved(self, event):
        print(f"{event.src_path} foi movido para para {event.dest_path}")
        

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()
import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
 
from_Dir:r"C:\Users\\sai\\Desktop\\prathamesh whitehat .jr\\Python\\103\\downloads"

class FileMovementHandler(FileSystemEventHandler):
        def on_created(self, event):
           print(f"Hey,{event.downloads}has been created!")
             
        def on_deleted(self, event):
           print(f"opps someone deleted,{event.download}!")
        
        def on_moved(self, event):
         print(f" someone moved,{event.download}!") 
        
        def on_moved(self, event):
         print(f" someone ,{event.download} modified!") 

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_Dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
               
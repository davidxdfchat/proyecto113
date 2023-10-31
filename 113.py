import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/57317/Desktop/La Ferrari"

# Clase Event Hanlder 
class FileEventHandler(FileSystemEventHandler):

    def on_crated(self, event):
        print(f"¡oye,{event.src_path} ha sido crado!")

    def on_deleted(self, event):
        print(f"¡Lo siento! ¡Alguien borró{event.src_path}!")
 
    def on_modified(self, event):
        print(f"¡Hola!,{event.src_path} ha sido modificado")

    def on_moved(self, event):
        print(f"Alguien movió {event.src_path} a {event.dest_path}")



# Inicia clase Event Handler 
event_handler = FileEventHandler()

# Inicia Observer
observer = Observer()

# Programa the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicia el Observer
observer.start()


try:
    while True:
       time.sleep(2)
       print("ejecutando...")
except KeyboardInterrupt:
    print("¡detenido¡")
    observer.stop()



# Desktop notifier in python 

import time 
from plyer import notification  


tasks = [
    "Complete python homework",
    "Read 10 pages of Manga",
    "Exercise for 20 minutes",
    "Drink 8 glasses of lemonade"
]

for task in tasks: 
    notification.notify(

        title = "task reminder",
        message = f"Did you complete: {task}",
        timeout = 3,
        app_icon = str(current_folder / "face.ico")
    )
    time.sleep(3600)
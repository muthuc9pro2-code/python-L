from datetime import datetime

with open("/mnt/d/code/python/learning py/scheduling/time_cron.txt", "a") as file:  # for the scheduking just write the entire path 
    file.write(f"script ran at : {datetime.now()}\n")
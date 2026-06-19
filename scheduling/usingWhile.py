from datetime import datetime
import time     

def scheduling():

    with open("/mnt/d/code/python/learning py/scheduling/time_while.txt", "a") as f:
        f.write(f"script ran at : {datetime.now()}")
    print(f"success : {datetime.now()}")

while True:           # true is means just true it runs forever
    scheduling()
    time.sleep(10)    # time should be imported to use time





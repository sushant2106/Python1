# import schedule
# import time as tm
# from datetime import time,timedelta,datetime

# def job():
#     print("Hello....")


# schedule.every(5).seconds.do(job)

# while True:
#     schedule.run_pending()
#     tm.sleep(1)
 
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler,BlockingScheduler
from datetime import datetime


def display(msg):
    print("This func has been executed")
    print(msg)
    # job_id.remove()
    # scheduler.shutdown(wait=False)

# scheduler=BlockingScheduler()
scheduler=BackgroundScheduler()
# job_id=scheduler.add_job(display,'interval',seconds=3,args=["Hello World.."]) #hours=1
scheduler.add_job(display,'interval',seconds=3,args=["Hello World.."]) #hours=1
job_id=scheduler.add_job(display,'interval',seconds=5,args=["I am 5 sec.."]) #hours=1

scheduler.add_job(display,'date',run_date=datetime(2023,10,27,11,19,0),args=["job 3"])

scheduler.start()
sleep(10)
print("ALL DONE...")
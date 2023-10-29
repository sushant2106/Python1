from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio

async def my_async_task():
    print("Async task is running...")

scheduler = AsyncIOScheduler()
scheduler.add_job(my_async_task, 'interval', seconds=5)
scheduler.start()

# try:
#     asyncio.get_event_loop().run_forever()
# except (KeyboardInterrupt, SystemExit):
#     pass

# scheduler.shutdown()

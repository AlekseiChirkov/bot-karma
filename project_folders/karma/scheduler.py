import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from .crud import engine
from sqlalchemy.orm import sessionmaker
from .models_sql import User

sched = BlockingScheduler()
Session = sessionmaker(bind=engine)
s = Session()

@sched.scheduled_job('cron', day_of_week='fri', hour=10)
def timed_job():
    for user in s.query(User):
        date_from = user.busy_from_date
        date_to = user.busy_to_date
        now = datetime.date.today()
        print(now)
        print(date_from)
        print(date_to)
        if date_from and date_to:
            if now >= date_from and now <= date_to:
                user.busyness_points = 4
                s.add(user)
                s.commit()

sched.start()

from crontab import CronTab


empty_cron    = CronTab()
my_user_cron  = CronTab(user=True)
users_cron    = CronTab(user='pavan')

job = users_cron.new(command='echo hi 2>&1')

users_cron.write()

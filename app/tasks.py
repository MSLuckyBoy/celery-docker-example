from core.celery import app


@app.task
def add(x, y):
	return x + y

@app.task
def crontab_task():
	return 'OK'
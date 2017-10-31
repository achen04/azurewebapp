import datetime

#from django.contrib.auth.models import User
from django.db import models


class LogEntry(models.Model):
	#user = models.ForeignKey(User)
	content = models.TextField()
	date = models.DateField(
			default=datetime.date.today()
	)

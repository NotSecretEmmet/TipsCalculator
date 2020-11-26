from django.db import models
from django.contrib.auth.models import User

class TipsRun(models.Model):
	start_dt = models.DateTimeField()
	end_dt = models.DateTimeField()
	run_dt = models.DateTimeField()
	boh_hours = models.FloatField()
	boh_tipr = models.FloatField()
	foh_hours = models.FloatField()
	foh_tipr = models.FloatField()
	tips_amount = models.FloatField()
	overtips_amounts = models.FloatField()
	effective_tips = models.FloatField()
	locatie = models.CharField(max_length = 200)
	week = models.CharField(max_length=20)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '%s ran by %s for %s on %s' % (self.week, self.user.username, self.locatie, self.run_dt) 


class TipsResults(models.Model):
	personeelsnummer = models.CharField(max_length = 200)
	naam = models.CharField(max_length = 200)
	boh_hours = models.FloatField()
	foh_hours = models.FloatField()
	total_hours = models.FloatField()
	boh_tips = models.FloatField()
	foh_tips = models.FloatField()
	total_tips = models.FloatField()
	tipsrun = models.ForeignKey(TipsRun, null=True, on_delete=models.CASCADE)
	user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '%s , #%s, %s, %s' % (self.naam, self.personeelsnummer, self.tipsrun.locatie, self.user.username)

	


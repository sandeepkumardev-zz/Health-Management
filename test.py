import datetime


class Company(models.Model):
    date = models.DateField()
    time = models.TimeField()


c = Company(date=datetime.datetime.now(), time=datetime.datetime.now())

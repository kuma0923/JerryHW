from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length = 20)
	gender = models.CharField(max_length = 20)
	department = models.CharField(max_length=15)
	address = models.CharField(max_length = 50,blank = 15)
	about = models.CharField(max_length=500)
	def __str__(self):
		return self.name
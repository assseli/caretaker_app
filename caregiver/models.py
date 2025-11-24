from django.db import models

class User(models.Model):
	email = models.EmailField(unique=True)
	given_name = models.CharField(max_length=30)
	surname = models.CharField(max_length=30)
	city = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20)
	profile_description = models.TextField(blank=True)

	def __str__(self):
		return self.email

class Caregiver(models.Model):
	name = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='caregiver_photos/', blank=True, null=True)
	gender = models.CharField(max_length=10)
	caregiver_type = models.CharField(max_length=50)
	hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.name

class Member(models.Model):
	name = models.CharField(max_length=100)
	house_rules = models.TextField()
	dependent_description = models.TextField()
	
	def __str__(self):
		return self.name

class Address(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='addresses')
	house_number = models.CharField(max_length=10)
	street = models.CharField(max_length=100)
	town = models.CharField(max_length=50)
	
	def __str__(self):
		return f"{self.house_number} {self.street}, {self.town}"
	
class Job(models.Model):
	member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='jobs')
	required_caregiver_type = models.CharField(max_length=50)
	other_requirements = models.TextField()
	date_posted = models.DateField(auto_now_add=True)
	
	def __str__(self):
		return f"Job for {self.member.name} posted on {self.date_posted}"

class Job_Application(models.Model):
	job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
	caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name='applications')
	date_applied = models.DateField(auto_now_add=True)
	
	def __str__(self):
		return f"Application by {self.caregiver.name} for job posted on {self.job.date_posted}"
	
class Appointment(models.Model):
	caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name='appointments')
	member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='appointments')
	appointment_date = models.DateField()
	appointment_time = models.TimeField()
	work_hours = models.DecimalField(max_digits=4, decimal_places=2)
	status = models.CharField(max_length=20)
	
	def __str__(self):
		return f"Appointment on {self.appointment_date} at {self.appointment_time} between {self.caregiver.name} and {self.member.name}"
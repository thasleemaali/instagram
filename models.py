from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class Registration(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    photo=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    birthdate = models.DateField()
    bio=models.CharField(max_length=100)

class Complaint(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    date = models.DateField()
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

class Post(models.Model):
    REGISTRATION = models.ForeignKey(Registration, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post_post')
    date = models.DateField()

class Frequest(models.Model):
    REGISTRATION=models.ForeignKey(Registration,on_delete=models.CASCADE)

class Feedback(models.Model):
    REGISTRATION=models.ForeignKey(Registration, on_delete=models.CASCADE)
    send_date=models.DateField()
    feedback=models.CharField(max_length=255)
    status=models.CharField(max_length=255)

class Report(models.Model):
    REGISTRATION=models.ForeignKey(Registration, on_delete=models.CASCADE,related_name="fromuser")
    against_user = models.ForeignKey(Registration, on_delete=models.CASCADE,related_name="touser",default='')
    send_date=models.DateField()
    report=models.CharField(max_length=255)
    status=models.CharField(max_length=255)

# class Comments (models.Model):
#     comment_post = models.CharField(max_length=150)
#     author = models.ForeignKey('Registration',related_name='commenter' , on_delete=models.CASCADE)
#     commented_image = models.ForeignKey('Image', on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#
#
#
#

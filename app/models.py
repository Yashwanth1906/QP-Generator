from django.db import models

# Create your models here.

class questions(models.Model):
    sno = models.IntegerField()
    question = models.TextField(default="")
    Type = models.CharField(max_length=2,default="")
    difficulty = models.IntegerField(default=1)
    answer = models.TextField(default = "")
    BT = models.CharField(max_length=20,default="")
    CO = models.CharField(max_length=20,default = "")
    marks = models.IntegerField(default = 0)
    topic = models.CharField(max_length=200,default="")
    course_code = models.CharField(max_length=50,default="")
class partA(models.Model):
    difficulty1 = models.IntegerField(default=1,null=True)
    difficulty2 = models.IntegerField(default=1,null=True)
    difficulty3 = models.IntegerField(default=1,null=True)
class partB(models.Model):
    difficulty1 = models.IntegerField(default=1,null=True)
    difficulty2 = models.IntegerField(default=1,null=True)
    difficulty3 = models.IntegerField(default=1,null=True)
class partC(models.Model):
    difficulty1 = models.IntegerField(default=1,null=True)
    difficulty2 = models.IntegerField(default=1,null=True)
    difficulty3 = models.IntegerField(default=1,null=True)

class Image(models.Model):
    imagelink = models.CharField(max_length=500)

class Department(models.Model):
    department_id = models.CharField(max_length=20,primary_key = True)
    department_name = models.CharField(max_length=50)

class Courses(models.Model):
    course_code = models.CharField(max_length = 50,primary_key = True)
    course_name = models.CharField(max_length = 200)
    semester_no = models.IntegerField()
    department_id = models.ForeignKey(Department,on_delete=models.CASCADE)
class Semesters(models.Model):
    semester_no = models.IntegerField()
    department_id = models.ForeignKey(Department,on_delete = models.CASCADE)
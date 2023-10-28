from django.db import models
from django.contrib.auth.models import  User
from django.utils import timezone

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=256)
    teacher_user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)

    image = models.ImageField(upload_to='\image\teacher_images',null=True,blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    class_name = models.CharField(max_length=256)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    class_code = models.CharField(max_length=6,default='', unique=True)
    level = models.CharField(max_length=256,default='')

    image = models.ImageField(upload_to='\image',null=True,blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.class_name

    def save(self, *args, **kwargs):
        if not self.class_code:
            self.class_code = ''.join(str(random.randint(0, 9)) for _ in range(6))
        super(Classroom, self).save(*args, **kwargs)


class Mission(models.Model):
    class_mission = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    mission_name = models.CharField(max_length=256)
    point_get = models.IntegerField()

    image = models.ImageField(upload_to='\image',null=True,blank=True)

    available_mission = models.IntegerField(default=0)
    mission_tag = models.CharField(max_length=256,default='')
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)


class Reward(models.Model):
    class_reward = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    reward_name = models.CharField(max_length=256)
    point_to_redeem = models.IntegerField()

    image = models.ImageField(upload_to='\image',null=True,blank=True)

    available_reward = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)


class Student(models.Model):
    name = models.CharField(max_length=256)
    class_name = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    net_point = models.IntegerField(default=0)
    point = models.IntegerField()

    image = models.ImageField(upload_to='\image\student_images',null=True,blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)



class Mission_Log(models.Model):
    mission = models.ForeignKey(Mission,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status = models.CharField(max_length=125)

    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)



class Reward_Log(models.Model):
    reward = models.ForeignKey(Reward,on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status = models.CharField(max_length=125)

    created_at = models.DateTimeField(default=timezone.now)
    update_at = models.DateTimeField(default=timezone.now)


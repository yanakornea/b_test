from django.contrib import admin
from classroomapp.models import Teacher , Classroom , Mission , Student , Mission_Log , Reward , Reward_Log
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Mission)
admin.site.register(Student)
admin.site.register(Mission_Log)
admin.site.register(Reward)
admin.site.register(Reward_Log)



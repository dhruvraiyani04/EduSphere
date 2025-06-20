from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username','User_type']
admin.site.register(CustomUser,UserModel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Staff_Leave)
admin.site.register(Student_Notification)
admin.site.register(Student_Leave)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)
admin.site.register(StudentResult)
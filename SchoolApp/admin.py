from django.contrib import admin

# Register your models here.
from SchoolApp import models

admin.site.register(models.Login)
admin.site.register(models.Teacher)
admin.site.register(models.Student)
admin.site.register(models.Attendance)
admin.site.register(models.TimeTable)
admin.site.register(models.Circular)
admin.site.register(models.Feedback)
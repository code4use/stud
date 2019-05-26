from django.contrib import admin
from .models import Subject, SubjectSection, Task
# Register your models here.

admin.site.register(Subject)
admin.site.register(SubjectSection)
admin.site.register(Task)

from django.db import models


# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name


class SubjectSection(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    section_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject.subject_name + ' ' + self.section_name


class Task(models.Model):
    section = models.ForeignKey('SubjectSection', on_delete=models.CASCADE)
    task_head = models.CharField(max_length=50,blank=True)
    task_text = models.TextField(blank=True)
    task_solv = models.TextField(blank=True)
    task_num_answer = models.FloatField(blank=True, default=0.0)

    def __str__(self):
        return self.section.section_name + ' ' + str(self.id) + ' ' + self.task_head

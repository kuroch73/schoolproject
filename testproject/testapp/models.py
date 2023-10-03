from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

class Student(models.Model):
    grade = models.IntegerField('оценка')
    tel = models.CharField('телефон', max_length=9)
    firstname = models.CharField('имя фамилия',max_length=20)



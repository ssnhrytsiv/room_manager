from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Lecture(models.Model):
    lesson = models.OneToOneField('lesson.Lesson', null=True, on_delete=models.SET_NULL, default=None,
                                  related_name='Lesson')
    group = models.OneToOneField('group.Group', null=True, on_delete=models.SET_NULL, default=None,
                                  related_name='Lesson')
    room = models.OneToOneField('room.Room', null=True, on_delete=models.SET_NULL, default=None,
                                  related_name='Lesson')
    teacher = models.OneToOneField('user.User', null=True, on_delete=models.SET_NULL, default=None,
                                  related_name='Lesson')
    number_by_schedule = models.IntegerField(default=1)

    def __str__(self):
        return 'lecture'+str(self.id)

    @staticmethod
    def get_all():
        lectures = Lecture.objects.all()
        return lectures



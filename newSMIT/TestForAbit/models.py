from django.db import models
# Create your models here.

class UserPasses(models.Model):
    test1_finish = models.BooleanField(default=False)
    test1_start = models.BooleanField(default=False)
    test2_finish = models.BooleanField(default=False)
    test2_start = models.BooleanField(default=False)
    test3_finish = models.BooleanField(default=False)
    test3_start = models.BooleanField(default=False)

class UserProgress(models.Model):

    user_id = models.IntegerField()
    test_id = models.IntegerField()
    finish = models.BooleanField(default=False)
    if test_id == 1:
        list_answers = models.JSONField(default=[*[0] * 15])
    elif test_id == 2:
        list_answers = models.JSONField(default=[*[0] * 30])
    else:
        list_answers = models.JSONField(default=list)






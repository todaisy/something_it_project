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

class TestAnswers(models.Model):
    id_test = models.IntegerField()
    id_ques = models.IntegerField()
    id_answ = models.IntegerField()
    id_id_weights = models.IntegerField()
    id_group = models.IntegerField(null=True, blank=True)
    answer_text = models.TextField()

class Questions(models.Model):
    id_test = models.IntegerField()
    id_ques = models.IntegerField()
    id_group = models.IntegerField(null=True, blank=True)
    answer_text = models.TextField()

class Weight(models.Model):
    id_test = models.IntegerField()
    id_weight = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True)

class ListProf(models.Model):
    id_test = models.IntegerField()
    answer_text = models.TextField()
    id_group = models.IntegerField()
    list_prof = models.JSONField(default=list)

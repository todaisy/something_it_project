from django.db import models
import uuid
# Create your models here.

class UserPasses(models.Model):
    token = models.CharField(max_length=64, unique=True, default=uuid.uuid4, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    test1_finish = models.DateTimeField(null=True, blank=True)
    test2_start = models.DateTimeField(null=True, blank=True)
    test2_finish = models.DateTimeField(null=True, blank=True)
    test3_start = models.DateTimeField(null=True, blank=True)
    test3_finish = models.DateTimeField(null=True, blank=True)


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

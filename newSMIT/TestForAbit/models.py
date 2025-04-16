from django.db import models
# Create your models here.

class UserPasses(models.Model):
    user_id = models.CharField(primary_key=True)
    test1_finish = models.BooleanField(default=False)
    test1_start = models.BooleanField(default=False)
    test2_finish = models.BooleanField(default=False)
    test2_start = models.BooleanField(default=False)
    test3_finish = models.BooleanField(default=False)
    test3_start = models.BooleanField(default=False)

class UserProgress(models.Model):

    user_id = models.CharField()
    test_id = models.IntegerField()
    finish = models.BooleanField(default=False)
    list_answers = models.JSONField(default=list)
    class Meta:
        unique_together = ('user_id', 'test_id')

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

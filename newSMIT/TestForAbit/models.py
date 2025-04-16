from django.db import models
import uuid


class TestSession(models.Model):
    # Уникальный идентификатор сессии
    session_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,  # Автогенерация UUID
        editable=False,
        verbose_name="Идентификатор сессии"
    )

    # Дата и время создания сессии
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    is_completed = models.BooleanField(
        default=False,
        verbose_name="Тест завершен"
    )

    class Meta:
        verbose_name = "Сессия тестирования"
        verbose_name_plural = "Сессии тестирования"

    def __str__(self):
        return f"Сессия {self.session_id} ({self.created_at})"

'''  
class TestSession(models.Model):
    session_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID сессии"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
'''


class TestAnswers(models.Model):
    session = models.ForeignKey(
        TestSession,
        on_delete=models.CASCADE,
        related_name='answers'
    )
    id_test = models.IntegerField()
    id_ques = models.IntegerField()
    id_answ = models.IntegerField()
    answer_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session', 'id_test', 'id_ques', 'id_answ')

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

''' 
class TestAnswers(models.Model):
    id_test = models.IntegerField()
    id_ques = models.IntegerField()
    id_answ = models.IntegerField()
    id_id_weights = models.IntegerField()
    id_group = models.IntegerField(null=True, blank=True)
    answer_text = models.TextField()
'''


class Questions(models.Model):
    id_test = models.IntegerField(verbose_name="ID теста")
    id_ques = models.IntegerField(verbose_name="ID вопроса")
    # question_text = models.TextField(verbose_name="Текст вопроса")
    id_group = models.IntegerField(null=True, blank=True)
    answer_text = models.TextField(verbose_name="Эталонный ответ")

    class Meta:
        unique_together = ('id_test', 'id_ques')

'''      
class Questions(models.Model):
    id_test = models.IntegerField()
    id_ques = models.IntegerField()
    id_group = models.IntegerField(null=True, blank=True)
    answer_text = models.TextField()
'''

class Weight(models.Model):
    id_test = models.IntegerField()
    id_weight = models.IntegerField()
    weight = models.IntegerField(null=True, blank=True)

class ListProf(models.Model):
    id_test = models.IntegerField()
    answer_text = models.TextField()
    id_group = models.IntegerField()
    list_prof = models.JSONField(default=list)

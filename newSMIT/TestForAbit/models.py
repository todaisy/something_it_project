from django.db import models

# Create your models here.

class Question(models.Model):
    id = models.IntegerField(default=1,primary_key=True)
    lbl = models.CharField(max_length=100, verbose_name="Вопрос")
    ans = models.JSONField(verbose_name="Варианты ответа",
                           help_text="Список вариантов ответа. Например: ['Да', 'Нет', 'Не уверен']")

    def __str__(self):
        return self.lbl
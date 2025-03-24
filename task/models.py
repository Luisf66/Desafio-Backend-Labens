from django.db import models

# Create your models here.

# Perguntar se isso vale como enum
SITUATION = (
    ('N', 'Nova'),
    ('E', 'Em andamento'),
    ('C', 'Concluida'),
    ('CA', 'Cancelada')
)

class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    term = models.DateField()
    conclusion = models.DateField()
    situation = models.CharField(max_length=2,choices=SITUATION)

    def __str__(self):
        return self.title
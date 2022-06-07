from django.db import models
from django.utils.translation import gettext_lazy as _

class CoxitWorker(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    birthday = models.DateField()
    salary = models.FloatField()
    favorite_joke = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = "coxit_workers"

    def __repr__(self) -> str:
        return f'Worker - {self.first_name} {self.last_name}'
    
    
    def __str__(self) -> str:
        return f'Worker - {self.first_name} {self.last_name}'
    
    @property
    def json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'birthday': self.birthday,
            'salary': self.salary,
        }
        
    
class Position(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:
        db_table = "coxit_positions"
        

class WorkerPosition(models.Model):
    
    class PositionLevel(models.TextChoices):
        TRAINEE = 'Tr', _("Trainee")
        JUNIOR = 'Jr', _('Junior')
        MIDDLE = 'Md', _('Middle')
        SENIOR = 'Sr', _('Senior')
    
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    worker = models.ForeignKey(CoxitWorker, on_delete=models.CASCADE)

    level = models.CharField(
        max_length=2,
        choices=PositionLevel.choices,
        default=PositionLevel.JUNIOR,
    )
    
    class Meta:
        db_table = "worker_position_rel"
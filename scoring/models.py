from django.db import models

# Create your models here.
class Gymnast(models.Model):
    LEVELS = [
        ('1','Level 1'),
        ('2','Level 2'),
        ('3','Level 3'),
        ('4','Level 4'),
    ]
    AGE_GROUPS = [
        ('u8','Under 8'),
        ('u10','Under 10'),
        ('u12','Under 12'),
        ('u15','Under 15'),
        ('o15','Over 15'),
    ]
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    level = models.CharField(max_length=3, choices=LEVELS)
    age_group = models.CharField(max_length=3,choices=AGE_GROUPS)
    club = models.CharField(max_length=32)

    def __str__(self) -> str:
        return '%s %s, Level %s' %(self.name, self.surname, self.level)

class RegisteredAparatus(models.Model):
    class Meta:
        unique_together = (('aparatus_name', 'gymnast'),)

    aparatus_name = models.CharField(max_length=32)
    gymnast = models.ForeignKey(Gymnast, on_delete=models.CASCADE)

class CompetitionInformation(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=32)
    meet_date = models.DateField()
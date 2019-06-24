from django.db import models

# Create your models here.
class Special(models.Model):
    title       = models.CharField(max_length=120)
    image       = models.ImageField(upload_to='special-img')
    description = models.TextField()
    create      = models.DateTimeField(auto_now=True)
    view        = models.BooleanField(default=False)

    class Meta:
        ordering = ['-create']
    
    def __str__(self):
        return self.title


class Menu(models.Model):
    Choices_status = (
        ('BS','BREAKFAST & STARTERS'),
        ('MC','MAIN COURSE'),
        ('Di','DINNER'),
        ('De','DESSERTS')
    )
    title       = models.CharField(max_length=120)
    price       = models.IntegerField()
    description = models.TextField()
    menu_section_title = models.CharField(max_length=10, choices=Choices_status)

    def __str__(self):
        return self.title
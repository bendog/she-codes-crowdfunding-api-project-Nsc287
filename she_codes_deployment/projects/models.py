from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# from dateutil.relativedelta import relativedelta

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, null=True) 
    slug = models.SlugField(unique=True) 
    

class Idol(models.Model):
    name = models.CharField(max_length=200, null=True)
    bio = models.TextField(blank=True)
    image = models.URLField()
    

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
        )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
        )

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(default=timezone.now)
    # deadline = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    rewards_list= models.JSONField(null=True)
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, null=True)
        # related_name='categorized_projects', null=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects', 
    )
    idol = models.ForeignKey(
        Idol, 
        on_delete=models.CASCADE, null=True) 
        # related_name='Idolized_projects', null=True)

    # def save(self, *args, **kwargs):  # Override the save method to calculate the deadline
    #     if not self.id:
    #         self.deadline = self.date_created + relativedelta(months=+6)
    #         super(Project, self).save(*args, **kwargs)

class Reward(models.Model):
    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        related_name='project_rewards'
    )
    amount = models.IntegerField(null=True)
    description=models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.amount} - {self.description}'

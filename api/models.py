from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model) :
    name = models.CharField( max_length=50 , null=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Date(models.Model) :
    date = models.ForeignKey(Person , on_delete=models.CASCADE , related_name='date' , default=timezone.now)
    default_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.default_date} written by {self.date.name}"
    
class Task(models.Model) :
    task = models.ForeignKey(Date , on_delete=models.CASCADE  , related_name='task')
    task_name = models.CharField(max_length=50 , null=True)
    
    category = [
        ("HW" , "Home Ware") , 
        ("KW" , "Kitchen Ware" ) , 
        ("CL" , "Clothes" ) ,
        ("TC" , "Technology") ,
    ]
    task_time = models.TimeField(null=True)
    type = models.CharField(default="TC" , choices=category , max_length=2)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
    

from django.db import models
import django
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from wineproject.utils import  slug_generator_for_event,slug_generator_for_eventType
from autoslug import AutoSlugField
from datetime import datetime
from datetime import date
from django.urls import reverse
# Create your models here.


def user_directory_path(instance, filename):
    producer_id_in_list = instance.Event_name.split(" ")
    today_date = date.today()
    producer_id_in_string = '_'.join([str(elem) for elem in producer_id_in_list])
    return '{0}/{1}'.format(producer_id_in_string+"/event/"+str(today_date.year)+"/"+str(today_date.month)+"/"+str(today_date.day),filename)



class AwEventType(models.Model):
    Type = models.CharField(max_length=120,unique=True)
    Slug = AutoSlugField(populate_from='Type', always_update=True, unique_with='Created_date__month', null=True,blank=True)
    Created_date = models.DateTimeField(default=django.utils.timezone.now)


    def __str__(self):
        return str(self.Type)

    class Meta:
        verbose_name_plural = "AW Event Type"


def pre_save_create_slug_for_event_type(sender, instance, *args, **kwargs):
    if not instance.Slug:
        instance.Slug= slug_generator_for_eventType(instance)

pre_save.connect(pre_save_create_slug_for_event_type, sender=AwEventType)


class AwEvent(models.Model):
    Event_name = models.CharField(max_length=120,unique=True)
    Event_Host = models.CharField(max_length=120,null=True,blank=True)
    Event_Type = models.ForeignKey(AwEventType, on_delete=models.SET_NULL, null=True, blank=True,related_name='EventType_AwEvent')
    Slug = AutoSlugField(populate_from='Event_name', always_update=True,unique_with='Created_date__month',null=True, blank=True)
    Description = models.TextField(null=True,blank=True)
    Short_Description = models.TextField(null=True,blank=True)
    Producer_Notes = models.TextField(null=True,blank=True)
    Location = models.TextField(null=True,blank=True)
    Event_Image = models.ImageField(upload_to=user_directory_path)
    Start_Date = models.DateTimeField(default=0)
    End_Date = models.DateTimeField(default=0)
    ticket_pr_person = models.IntegerField(default=0)
    ticket_price = models.FloatField(default=0)
    Status =models.BooleanField(default=True)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='Created_by_AwEvent')
    Created_date = models.DateTimeField(default=django.utils.timezone.now)
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,related_name='Updated_by_AwEvent')
    Updated_date = models.DateTimeField(default=django.utils.timezone.now)


    def get_absolute_url(self):
        return reverse('manage_event:event')
    def __str__(self):
        return str(self.Event_name)

    class Meta:
        verbose_name_plural = "AW Event"

def pre_save_create_slug(sender, instance, *args, **kwargs):
    if not instance.Slug:
        instance.Slug= slug_generator_for_event(instance)

pre_save.connect(pre_save_create_slug, sender=AwEvent)
from django.db import models
from django.template.defaultfilters import  slugify
from django.conf import settings
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from django.utils import  timezone
# Create your models here.


class BaseModel(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =True


class Article(BaseModel):
    title = models.CharField(max_length=500)
    image = models.ImageField(
        upload_to='%d-%m-%Y/images')
    story = RichTextField()
    active = models.BooleanField('make puplic',default=True,help_text='make this article pubic')
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,null=True,blank=True)
    slug = models.SlugField(blank=True, null=True)
    tags = TaggableManager(blank=True)
    total_views = models.PositiveIntegerField(default=0)
    source = models.URLField(help_text='source link', blank=True, null=True)

    class Meta:
        ordering = ['-date_updated']

    def get_absolute_url(self):

        return reverse('tof_app:blogdetail', args=[str(self.added_by), str(self.slug),str(self.id)])
        
# create a new slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

     # delet the image from file system
    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super().delete(*args, **kwargs)


    def __str__(self):
        return self.title


class AcceptChrist(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    note = models.TextField(help_text='write a short not ie why you want to accept christ',
                            default='I just responded to an Alter call to give my life to Christ')
    mode = [
        ['Phone call', 'Phone Call'],
        ['Whatsapp', 'Whatsapp'],
        ['Sms', 'Sms'],
        ['Email', 'Email']
    ]
    mode_to_reach_you = models.CharField(max_length=10,choices=mode,default='Phone call')

    def get_absolute_url(self):

        return reverse('tof_app:accept-christ')


class PrayerRequest(BaseModel):
    r_type = [
        ['Prayer Request', 'Prayer Request'],
        ['General', 'General'],
        # ['Volunteer', 'Volunteer'],
        ['Testimonies', 'Testimonies'],
        ['Suggestions', 'Suggestions'],
        # ['Webmaster', 'Webmaster'],
    ]
    request_type = models.CharField(
        max_length=20, choices=r_type, default='Prayer Request')
    name = models.CharField(max_length=200, blank=True,
                            null=True, help_text='optional')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()

    def get_absolute_url(self):

        return reverse('tof_app:prayer-request')

class Event(BaseModel):
    choice = [
        ['event','Event'],
        ['anoycement','Anoucement'],
    ]
    event_type = models.CharField(max_length=15,choices=choice,default='event')
    name = models.CharField(max_length=200)
    time = models.TimeField(default=timezone.now,blank=True, null=True)
    date = models.DateField(default=timezone.now,blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return '{}:{}'.format(self.event_type,self.name)
    


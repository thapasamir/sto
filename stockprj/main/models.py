from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import  timezone
from django.utils.text import slugify 


#Modelmanager to get the post which is published
class PublishManger(models.Manager):
    def get_queryset(self):
        return super(PublishManger,self).get_queryset().filter(status="published")
 

class New(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    aurthor = models.ForeignKey(User,on_delete=models.CASCADE)
    title =models.CharField(max_length=100)
    thumnail = models.ImageField(upload_to="media/thumnail", height_field=None, width_field=None, max_length=None)
    post = RichTextField(blank=False, null=False)
    slug = models.SlugField(max_length=100,unique_for_date='publish')
    publish = models.DateField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
        )
    objects = models.Manager() 
    Post = PublishManger()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("New_detail", kwargs={"pk": self.pk})


from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
#  models here.






class Entry(models.Model):
    title = models.CharField(max_length=25,null=True)
    text = models.TextField(default='  ',null=True)
    author =models.CharField(default='  ',null=True,max_length=50)
    sub_heading = models.CharField(default='  ',null=True,max_length=50)
    date_posted = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='img/user.Username/%Y/%m/%d/',null="",default=" ",blank=True)

    fields = "__all__"
    def publish(self):
        self.date_posted = timezone.now()
        self.save()

    def __str__ (self):
        return self.title

    def snippet(self):
        return self.text[:20]+"......"

    class meta:
        verbose_name_plural='entries'


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField()
    def __str__(self):
        return "%s's profile" % self.user
    



class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    bio = models.CharField(max_length=300, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    avatar = models.ImageField(upload_to = 'images/profile/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



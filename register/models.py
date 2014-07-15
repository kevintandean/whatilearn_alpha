from django.contrib.auth.models import User
from django.db import models
from vote.managers import VotableManager
from registration.models import RegistrationProfile

#profile model that links to user
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    cover_image = models.ImageField(upload_to='cover', blank=True, null=True)
    last_modified = models.DateTimeField(auto_now_add=True)



    def __unicode__(self):
        return self.user.username

    def avatar_image_url(self):
        #print bool(self.avatar)
        if bool(self.avatar)==False:
            return "/media/avatar/default_avatar.jpg"
        else:
            return self.avatar.url

    def cover_image_url(self):
        if bool(self.cover_image)==False:
            return self.avatar_image_url()
        else:
            return self.cover_image.url

class Post(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField(max_length=300)
    source = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(blank=True,null=True)
    # tag = models.ManyToManyField('Tag', null=True, blank=True, related_name='post')
    votes = VotableManager()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.content


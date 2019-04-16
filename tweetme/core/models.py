from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    text=models.CharField(max_length=140,help_text="Please enter a tweet")
    owner=models.ForeignKey('auth.User',related_name='tweets',on_delete=models.CASCADE)
    is_public = models.BooleanField(default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    modified_at = models.DateTimeField(auto_now=True, editable=False)
    type = models.IntegerField(default=0, null=False, blank=False, editable=False)
    likes_count = models.IntegerField(default=0, null=False, blank=False, editable=False)
    comments_count = models.IntegerField(default=0, null=False, blank=False, editable=False)

    def __str__(self):
        return self.text

class Like(models.Model):
    tweet = models.ForeignKey('Tweet',
                              related_name='like',
                              on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User',
                               related_name='author',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.tweet.text

class Comment(Tweet):
    parent = models.ForeignKey('Tweet',
                               related_name='comments',
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Follow(models.Model):
    user = models.ForeignKey('auth.User', related_name='friends', on_delete=models.CASCADE)
    target = models.ForeignKey('auth.User', related_name='followers', on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)+"->"+str(self.target)

    class Meta: 
        unique_together = ('user', 'target')

class UserTimeLine(models.Model):
    username=models.ForeignKey('auth.User',related_name='own_timeline',on_delete=models.CASCADE)
    own_tweet = models.ForeignKey('Tweet',
                              related_name='own_tweet',
                              on_delete=models.CASCADE)

class PublicTimeLine(models.Model):
    username=models.ForeignKey('auth.User',related_name='public_timeline',on_delete=models.CASCADE)
    public_tweet = models.ForeignKey('Tweet',
                              related_name='public_tweet',
                              on_delete=models.CASCADE)

from annoying.fields import AutoOneToOneField

class UserProfile(models.Model):
    user = AutoOneToOneField('auth.user')
    follows = models.ManyToManyField('UserProfile', related_name='followed_by')

    def __unicode__(self):
        return self.user.username                    
from rest_framework import serializers
from . import models

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tweet
        fields=("id","text","likes_count","comments_count","owner")
        read_only_fields=("id","owner","likes_count","comments_count")
# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.Like
#         fields='__all__'
#         read_only_fields=("id","author")
# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=models.Comment
#         fields=('id','comments_count','owner','parent')
#         read_only_fields=('id','comments_count','owner','parent')
class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Follow
        fields='__all__'
        read_only_fields=('id','created_at','user','target')
        

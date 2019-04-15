from rest_framework import routers
from . import views
routee=routers.DefaultRouter()
routee.register(r"tweet",views.TweetSerialView)
#routee.register(r"like",views.LikeSerialView)
#routee.register(r"comment",views.CommentSerialView)
routee.register(r"follow",views.FollowSerialView)
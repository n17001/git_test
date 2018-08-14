from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stage/$',views.stage,name='stage'),
    url(r'^stage/head/$',views.head_html,name='head'),
    url(r'^stage/story/$',views.story_html,name='story'),
    url(r'^stage/game/$',views.game_html,name='game'),
]

from django.urls import path

from api.views.tag_views import *

from api.views.tag_views import get_all_tags, add_tag

app_name = 'tag'

urlpatterns = [
    path('all/', get_all_tags),
    path('add/', add_tag),

    # path('get/<int:pk>/', get_review),
    # path('get_critic_reviews/', get_critic_reviews),

]
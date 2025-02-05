"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/menu_review/', include('api.urls.book_review_urls')),
    path('api/menu_review/', include('api.urls.post_urls')),
    path('api/menu/', include('api.urls.menu_urls')),
    path('api/post/', include('api.urls.post_urls')),
    path('api/tag/', include('api.urls.tag_urls')),
    path('api/analyze/', include('api.urls.analyze_urls')),
    path('api/report/', include('api.urls.report_urls')),
    path('api/restaurant/', include('api.urls.restaurant_urls')),
    path('api/auth/', include('api.urls.auth_urls')),
    path('api/comment/', include('api.urls.comment_urls')),
    path('api/chat/', include('api.urls.chat_urls')),
   
]

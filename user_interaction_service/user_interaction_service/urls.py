"""user_interaction_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import UserInteractionCreateView, UserInteractionDetailView, UserInteractionUpdateView, TopReadContents, TopLikeContents, TopContents

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user-interactions/', UserInteractionCreateView.as_view(), name='user-interactions-create'),
    path('user-interactions/<int:user_id>/', UserInteractionDetailView.as_view(), name='user-interactions-detail'),
    path('update-user-interactions/<int:pk>/', UserInteractionUpdateView.as_view(), name='update-user-interactions'),
    path('top-read-contents/', TopReadContents.as_view(), name='top-read-contents'),
    path('top-like-contents/', TopLikeContents.as_view(), name='top-like-contents'),
    path('top-contents/', TopContents.as_view(), name='top-contents'),
]

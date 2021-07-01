"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from brain_games import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index), 
    path('game_selection/', views.game_selection),
    path('first_game/', views.first_game),
    path('first_game/checking_game_answer/', views.checking_game_answer),
    path('admin/', admin.site.urls),
]

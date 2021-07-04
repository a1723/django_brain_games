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
    path('game-selection/', views.game_selection),
    path('brain-even/', views.brain_even),
    path('brain-calc/', views.brain_calc),
    path('brain-gcd/', views.brain_gcd),
    path('brain-prime/', views.brain_prime),
    path('brain-progression/', views.brain_progression),
    path('brain-even/checking-brain-even-game-answer/', views.checking_brain_even_game_answer),
    path('brain-calc/checking-brain-calc-game-answer/', views.checking_brain_calc_game_answer),
    path('brain-gcd/checking-brain-gcd-game-answer/', views.checking_brain_gcd_game_answer),
    path('brain-prime/checking-brain-prime-game-answer/', views.checking_brain_prime_game_answer),
    path('brain-progression/checking-brain-progression-game-answer/', views.checking_brain_progression_game_answer),
    path('admin/', admin.site.urls),
]

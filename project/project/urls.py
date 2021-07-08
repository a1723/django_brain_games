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
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('game-selection/', views.game_selection),
    path('even/', views.even),
    path('calc/', views.calc),
    path('gcd/', views.gcd),
    path('prime/', views.prime),
    path('progression/', views.progression),
    path('even/even-check/', views.even_check),
    path('calc/calc-check/', views.calc_check),
    path('gcd/gcd-check/', views.gcd_check),
    path('prime/prime-check/', views.prime_check),
    path('progression/progression-check/', views.progression_check),
    path('admin/', admin.site.urls),
]

from django.urls import path

from users import views

urlpatterns = [
    path('register/', views.register),
    path('confirm/', views.confirm),
    path('login/', views.login_view),
]

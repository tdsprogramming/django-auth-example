from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view),
    path('register/', views.register_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('success/', views.success_view),
]
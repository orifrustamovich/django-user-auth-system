from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('confirm_email/', views.confirm_email, name='confirm_email'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    # path('logout/', LogoutView.as_view(), name='logout'),

]

from django.urls import path
from . import views

urlpatterns = [
    #login
    path('login', views.login_view, name='login'),
    #logout
    # path('logout', views.logout_view, name='logout'),
    #signup
    path('signup', views.signup_view, name='signup')
]
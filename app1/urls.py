from django.urls import path
from . import views


 
urlpatterns = [
    # path ('', views.index,name='index page'),
    path ('', views.home,name='home page'),
    path ('contact', views.contact,name='contact page'),
    path ('signup', views.signup,name='signup page'),
    path ('login', views.login,name='login page'),
    path ('logout', views.logout,name='logout page'),
    path ('linkedin', views.linkedin,name='linkedin page'),
    path ('twitter', views.twitter,name='twitter page'),
    path ('facebook', views.facebook,name='facebook page'),
    path ('instagram', views.instagram,name='instagram page'),
    path ('github', views.github,name='github page'),
    
]




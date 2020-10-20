from django.urls import path
from .import views
app_name='login'
urlpatterns = [
    path('signup/', views.signup,name='signup'),
    path('profile/', views.profile,name='profile'),
    path('profile/edite', views.profile_edit,name='profile_edit'),

    #path('create/', views.create_post, name='create_post'),
]


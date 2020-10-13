from django.urls import path
from . import views

app_name = 'youtube'
urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('new_video/',views.new_video, name = 'new_video'),
    path('login/',views.loginUser, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('video/<str:pk>/',views.video_view, name = 'video'),
    path('logout/',views.logoutUser, name = 'logout'),
    path('comments/',views.comments, name = 'commets')
] 
from django.urls import path
from . import views

urlpatterns = [
    path('signin-form/', views.signinForm, name='signin-form'),
    path('logout-form/', views.logoutUser, name='logout-form'),
    path('signup-form/', views.signupForm, name='signup-form'),

    path('', views.homePage, name='home'),
    path('user-profile/<int:pk>/', views.userProfile, name='user-profile'),
    path('detail/<int:pk>/', views.detailPage, name='detail'),
    path('add-post/', views.addPost, name='add-post'),
    path('update-post/<int:pk>/', views.updatePost, name='update-post'),
    path('delete-post/<int:pk>/', views.deletePost, name='delete-post'),
]

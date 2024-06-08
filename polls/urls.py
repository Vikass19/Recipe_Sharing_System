from django.urls import path

from . import views

urlpatterns = [
    path('recipi/',views.recipi, name = "recipi"),
    path('delete_recipi/<id>/', views.delete_recipi, name='delete_recipi'),
    path('update_recipi/<id>/', views.update_recipi, name='update_recipi'),
    path('signup/',views.signup, name = "signup"),
    path('login_page/',views.login_page, name = "login_page"),

    path('logout_page/',views.logout_page, name = 'logout_page'),
    
    
]
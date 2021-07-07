from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_view,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('acerca/',views.acerca,name="acercade"),
    path('contacto/',views.contacto,name="contacto"),
]
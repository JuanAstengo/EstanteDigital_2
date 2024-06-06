from django.urls import path
from . import views  # Importando views del mismo módulo accounts
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('signup/', views.signup, name='signup'),  # Asegúrate de añadir esto
]

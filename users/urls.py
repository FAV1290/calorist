from django.urls import path
from django.contrib.auth.views import LoginView

from .views import logout_view, user_ingredients_view, user_dishes_view


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('<slug:username>/ingredients/', user_ingredients_view, name='user_ingredients'),
    path('<slug:username>/dishes/', user_dishes_view, name='user_dishes'),
]

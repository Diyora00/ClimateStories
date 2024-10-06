from author.views import login_page, register, LogoutUserView
from django.urls import path


urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
]

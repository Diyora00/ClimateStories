from author.views import login_page, register, LogoutUserView
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
] + staticfiles_urlpatterns()

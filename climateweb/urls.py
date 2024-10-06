from django.urls import path
from climateweb.views import index, detail, detail2
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='home'),
    path('story_detail<pk>/', detail, name='story_detail'),
    path('echo_choice_<pk>/', detail2, name='echo_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

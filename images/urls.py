from django.conf.urls import url,include
from . import views


urlpatterns = [
    url('^$',views.welcome,name='welcome'),
    # url(r'^$',views.images,name='Images'),
]
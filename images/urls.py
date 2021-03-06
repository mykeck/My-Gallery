from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^$',views.images,name='Images'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^single_image/(\d+)',views.single_image, name='single_image')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
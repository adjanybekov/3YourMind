
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from App1.views import Test,SaveProfile
from ThreeYourMind import settings

urlpatterns = [
    url(r'^profile/',TemplateView.as_view(
      template_name = 'profile.html')),
    url(r'^saved/', SaveProfile , name='saved'),
]
# if settings.DEBUG:
#     urlpatterns +=static(settings.STATIC_URL,document_root = settings.STATIC_URL)
#     urlpatterns +=static(settings.MEDIA_URL,document_root = settings.MEDIA_URL)
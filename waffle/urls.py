from django.conf.urls import url

from waffle.views import wafflejs

urlpatterns = [
    url(r'^wafflejs$', wafflejs, name='wafflejs'),
]

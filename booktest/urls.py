from django.conf.urls import url
from booktest import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index$',views.index),
    url(r'^index2$',views.index2),
    url(r'temp_var$',views.temp_var)
]
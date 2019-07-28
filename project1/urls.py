from django.conf.urls import url
from src.views.userview import Userview


urlpatterns = [
   url(r'^user/', Userview.as_view()),

]
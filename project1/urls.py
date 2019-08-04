from django.conf.urls import url
from src.views.userview import Userview
from src.views.loginview import LoginView


urlpatterns = [
   url(r'^user/', Userview.as_view()),
   url(r'^login/', LoginView.as_view()),

]
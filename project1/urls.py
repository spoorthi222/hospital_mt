from django.conf.urls import url
from django.contrib import admin

# import testview from sample_app/view
from HMT_app.views import test_view
from HMT_app.views import staff_db_test

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^testview/', test_view),
   url(r'^staff/db/view/', staff_db_test),
]
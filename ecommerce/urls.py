from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include(apps.products.urls), namespace='products'),
    url(r'^user/', include(apps.users.urls), namespace='users'),
    url(r'^admin/', admin.site.urls),
]

from django.conf.urls import url
from django.contrib import admin
from mysite.core import views


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.UsersListView.as_view(), name='users_list'),
	url(r'^generate/$', views.GenerateRandomUserView.as_view(), name='generate'),
]

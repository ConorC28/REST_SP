from django.conf.urls import url
from rgc import views

urlpatterns = [
	url(r'^$',views.index, name='index'),
	url(r'^about$',views.about, name='about'),
	#url(r'^about/$', views.AboutPageView.as_view()),
]
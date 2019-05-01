from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test$', views.test, name='test'),
    url(r'^addact$', views.addact, name='addact'),
    url(r'^uploadact', views.upload_account, name='upload_account'),
    url(r'^addnewact', views.add_new_account, name='add_new_account'),
    url(r'^getnewact', views.get_new_account, name='get_new_account'),
    url(r'^resetactstatus', views.reset_account_status, name='reset_account_status'),
    url(r'^switch2admin', views.switch2admin, name='switch2admin'),    
]
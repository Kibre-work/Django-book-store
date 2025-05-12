from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),

]
#from .views import Home, Index

'''but if it is class based path('',classname.as_view(),name='home') every line of the path must include as_view()function'''
'''Method	             Purpose
get(self, request)	Handle GET requests (read/display data)
post(self, request)	Handle POST requests (submit form data)
put(self, request)	Handle PUT requests (update full data)
patch(self, request)	Handle PATCH requests (update partial data)
delete(self, request)	Handle DELETE requests (delete data)
head(self, request)	Like GET but returns only headers
options(self, request)	Returns allowed request methods (meta info)'''
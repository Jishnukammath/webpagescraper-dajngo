from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<id>',views.remove,name='remove'),
    path('favourite/<id>',views.favourite,name='favourite'),

]

from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('collection/',views.collection,name="collection"),
    path('home/',views.home,name="home"),
    
]
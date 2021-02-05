from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="shop home"),
    path("about/",views.about,name="about us"),
    path("contact/",views.contact,name="contact us"),
    path("track/",views.track,name="trackingstatus"),
    path("search/",views.search,name="search"),
    path("products/<int:myid>",views.products,name="products"),
    path("checkout/",views.checkout,name="checkout")






]

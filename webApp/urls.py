from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("index",index,name="index"),
    path("shop",shop,name="shop"),
    path("blog",blog,name="blog"),
    path("about",about,name="about"),
    path("contact",contact,name="contact"),
    path("cart",cart,name="cart"),
    path("sproduct1",sproduct1,name="sproduct1"),
    path("sproduct2",sproduct2,name="sproduct2"),
    path("sproduct3",sproduct3,name="sproduct3"),
    path("sproduct4",sproduct4,name="sproduct4"),
    path("signup",signup,name="signup"),
    path("login",login,name="login"),
    path("UserRegister",UserRegister,name="UserRegister"),
    path("UserLogin",UserLogin,name="UserLogin"),
    path("add",add,name="add"),
    path("add_product",add_product,name="add_product"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
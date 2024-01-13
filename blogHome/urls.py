
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home,name="Home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    path("content/<int:id>",views.content,name="content"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.Login,name="login"),
    path("logout/",views.logout_view,name="logout"),
    path("comment",views.comment,name="comment"),
    path('reply',views.replies,name='reply')
    
    
]
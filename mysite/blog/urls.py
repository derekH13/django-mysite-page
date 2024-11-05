from django.urls import path

from blog import views

# definindo o relacionamento de url e funções
urlpatterns = [
    path('/home', views.PostView.as_view(), name='home'),
    path('/exercicio', views.PostExercicio.as_view(), name='exercicio'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

from django.http import HttpResponse
from django.views import generic

from ..models import Post

# sobreescrevendo um metodo/função ja pronta do django


class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostExercicio(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello world')

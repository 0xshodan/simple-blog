from datetime import datetime

from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.template import loader
from django.views.generic import View

from .models import Post


class PostsView(View):
    def get(self, request: HttpRequest):
        posts = Post.objects.all()
        post = Post(
            name="John",
            description="Python django",
            content="flsdfj;as;fasdfsfjjsdflsdjfds",
            published_date=datetime.now(),
        )
        post.save()
        context_data = {"posts": posts}
        template = loader.get_template("posts.html")
        return HttpResponse(template.render(context_data, request))

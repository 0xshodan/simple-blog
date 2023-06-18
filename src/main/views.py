# from typing import Any, Dict

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class WorkView(TemplateView):
    template_name = "work.html"


class AboutView(TemplateView):
    template_name = "about.html"

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     _context = super().get_context_data(**kwargs)
    #     return _context
    # def get(self, request: HttpRequest):
    #     context_data = {"posts": posts}
    #     template = loader.get_template("posts.html")
    #     return HttpResponse(template.render(context_data, request))

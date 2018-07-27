from django.views.generic import TemplateView

from django import http


class CatGifView(TemplateView):
    template_name = "gifs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Jims Finest Cat Gifs"
        })
        return context

    def get(self, request: str, *args, **kwargs) -> http.HttpResponse:
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context=context)

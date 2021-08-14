from django.views.generic import TemplateView

class FlyingView(TemplateView):
    template_name = "flying.html"
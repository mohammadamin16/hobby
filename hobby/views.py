from django.http import HttpResponse
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'layout.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['Brand'] = "Hobby"
        return context




def home(request):
    return HttpResponse("Welcome!")




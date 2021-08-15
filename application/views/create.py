from django.views.generic.edit import CreateView
from ..models import Obon
from ..forms import ObonCreateForm
from django.shortcuts import redirect
from django.urls import reverse_lazy


class ObonCreate(CreateView):
    template_name = 'Obon_form.html'
    form_class = ObonCreateForm
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(ObonCreate, self).form_valid(form)
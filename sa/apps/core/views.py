from django.views.generic import DetailView, CreateView, DeleteView
from django.core.urlresolvers import reverse

from sa.apps.core.models import Car
from sa.apps.core.forms import CarForm


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"


class CarCreateView(CreateView):
    form_class = CarForm
    template_name = 'add_car.haml'

    def get_success_url(self):
        return reverse("home")


class CarDeleteView(DeleteView):
    model = Car

    def get_success_url(self):
        return reverse("home")

from sa.apps.core.models import Car
from django.views.generic import DetailView


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"

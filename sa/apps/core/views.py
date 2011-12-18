# -*- coding: utf-8 -*-
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, FormView
from django.core.urlresolvers import reverse
from django.contrib import messages

from sa.apps.core.models import Car
from sa.apps.core.forms import CarForm, PostCarForm


class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"


class CarCreateView(CreateView):
    form_class = CarForm
    template_name = 'add_car.haml'

    def form_valid(self, form):
        messages.info(self.request, u"Машина успешно добавлена")
        return super(CarCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("home")


class CarUpdateView(UpdateView):
    form_class = CarForm
    model = Car
    template_name = 'edit_car.haml'

    def form_valid(self, form):
        messages.info(self.request, u"Машина успешно отредактирована")
        return super(CarUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse("home")


class CarDeleteView(DeleteView):
    model = Car

    def get_success_url(self):
        return reverse("home")


class CarPostView(FormView):
    template_name = 'post_car.haml'
    form_class = PostCarForm

    def get_success_url(self):
        return reverse("home")

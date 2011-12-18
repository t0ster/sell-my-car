# -*- coding: utf-8 -*-
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, FormView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import redirect

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

    def get(self, request, *args, **kwargs):
        # If returning from twitter auth page
        if request.GET.get("oauth_verifier"):
            self.post_to_twitter()
            return redirect("home")
        return super(CarPostView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        if not self.request.twitter_api:
            return self.authorize_in_twitter()
        self.post_to_twitter()
        return super(CarUpdateView, self).form_valid(form)

    def authorize_in_twitter(self):
        self.request.twitter_auth.callback = self.request.build_absolute_uri()
        url = self.request.twitter_auth.get_authorization_url()
        return redirect(url)

    def post_to_twitter(self):
        pk = int(self.kwargs['pk'])
        car = Car.objects.get(pk=pk)
        status = (u"Продается %s, $%s %s" %
                (car, car.price, self.request.build_absolute_uri(car.get_absolute_url())))
        self.request.twitter_api.update_status(status=status, wrap_links=True)
        messages.info(self.request,
            u"Машина опубликована в <a target='_blank' href='http://twitter.com/%s'>twitter</a>" %
                self.request.twitter_api.me().name)

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView

from apps.forms import FormEmployee
from apps.models import Employee


class IndexView(ListView):
    queryset = Employee.objects.all()
    template_name = 'apps/index.html'
    context_object_name = 'employees'


class UpdateFormView(UpdateView):
    queryset = Employee.objects.all()
    form_class = FormEmployee
    model = Employee
    template_name = 'apps/update.html'
    success_url = reverse_lazy('index')


class CreateFormView(CreateView):
    form_class = FormEmployee
    model = Employee
    template_name = 'apps/create.html'

    def post(self, request, *args, **kwargs):
        form = FormEmployee(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')


class DeleteFormView(DeleteView):
    model = Employee
    template_name = 'apps/delete.html'
    success_url = reverse_lazy('index')


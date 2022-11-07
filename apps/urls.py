from django.contrib import admin
from django.urls import path

from apps.views import IndexView, UpdateFormView, CreateFormView, DeleteFormView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('update/<int:pk>', UpdateFormView.as_view(), name='update'),
    path('create/', CreateFormView.as_view(), name='create'),
    path('delete/<int:pk>', DeleteFormView.as_view(), name='delete'),
]

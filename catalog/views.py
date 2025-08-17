from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from catalog.models import Product


class ContactsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'catalog/contacts.html')

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')

        return HttpResponse(
            f'Спасибо, {name}! Ваше сообщение получено. '
            f'Сообщение: <{message}>. Телефон: <{phone}>'
        )


class HomeView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'catalog/home.html')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


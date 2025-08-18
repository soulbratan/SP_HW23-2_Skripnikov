from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.views import View

from catalog.forms import ProductForm
from catalog.models import Product
from django.urls import reverse_lazy


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # template_name = 'product_list/product_form.html'
    success_url = reverse_lazy('catalog:product_list')


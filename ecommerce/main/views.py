from itertools import product

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView
from django.template.response import TemplateResponse
from unicodedata import category

from .models import Product, Category, Size
from django.db.models import Q



class IndexView(TemplateView):
    template_name = 'main/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['current_category'] = None
        return context

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if request.headers.get('HX-Request'):
            return TemplateResponse(request, 'main/home_content.html', context)
        return TemplateResponse(request, self.template_name, context)




class CatalogView(TemplateView):
    template_name = 'main/base.html'


    FILTER_MAPPING = {
        'color': lambda queryset, value: queryset.filter(color__iexact=value),
        'min_price': lambda queryset, value: queryset.filter(min_price__gte=value),
        'max_price': lambda queryset, value: queryset.filter(max_price__lte=value),
        'size': lambda queryset, value: queryset.filter(product_size__size__name=value)
    }


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = kwargs.get('category_slug')
        categories = Category.objects.all()
        products = Product.objects.all()

        if category_slug:
            current_category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=current_category)


        query = self.request.GET.get('q')
        if query:
            products = products.filter(Q(name__icontains=query)
                                       | Q(description__icontains=query))


        filter_params = {}
        for param, filter_func in self.FILTER_MAPPING.items():
            value = self.request.GET.get(param)
            if value:
                products = filter_func(products, value)
                filter_params[param] = value
            else:
                filter_params[param] = ''

        filter_params['q'] = query or ''

        context.update({
            'categories': categories,
            'products': products,
            'filter_params': filter_params,
            'current_category': category_slug,
            'search_query': query or '',
            'sizes': Size.objects.all()
        })

        if self.request.GET.get('show_search') == 'true':
            context['show_search'] = True
        elif self.request.GET.get('reset_search') == 'true':
            context['reset_search'] = True


        return context



    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        if request.headers.get('HX-Request'):
            if context.get('show_search'):
                return TemplateResponse(request, 'main/search_input.html', context)
            elif context.get('reset_search'):
                return TemplateResponse(request, 'main/search_button.html', {})
            template = 'main/filter_modal.html' if request.GET.get('show_filters') == 'true' else 'main/catalog.html'
            return TemplateResponse(request, template, context)
        return TemplateResponse(request, self.template_name, context)




class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/base.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['related_products'] = Product.objects.filter(
            category=product.category
        ).exclude(id=product.id)[:4]
        context['current_category'] = product.category.slug
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        if request.headers.get('HX-Requset'):
            return TemplateResponse(request, 'main/product_detail.html', context)
        return TemplateResponse(request, self.template_name, context)









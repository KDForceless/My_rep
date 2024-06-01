from django.shortcuts import render
from .models import CategoryModel, ProductModel

# Create your views here.
def home_page(request):
    categories = CategoryModel.objects.all()
    products = ProductModel.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, template_name='index.html', context=context)





from django.http import HttpResponse
# from django.shortcuts import render
from django.shortcuts import render
from .models import Products


# Create your views here.


def product_detail_view(request):
    """ View for showing product details
     It returns the product object
     """

    my_product = Products.objects.get(id=1)

    # context = {
    #     "title": my_product.title,
    #     "description": my_product.description
    # }
    # print(my_product)
    context = {
        "my_product": my_product
    }
    return render(request, "product/detail.html", context)

from django.shortcuts import render
from products.models import Product
from products.serializer import ProductSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render,get_object_or_404


# Create your views here.
@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        products_serializer = ProductSerializer(products,many=True)
        return JsonResponse(products_serializer.data,safe=False)

    elif request.method == 'POST':
        products_data = JSONParser().parse(request)
        products_serializer = ProductSerializer(data = products_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse(products_serializer.data,status = status.HTTP_201_CREATED)

        return JsonResponse(products_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def product_details(request,pk):
    try:
        product = Product.objects.get(pk = pk)
    except Exception as e:
        return JsonResponse({"Message": str(e)},status = status.HTTP_404_NOT_FOUND)

    try:
        if request.method == 'GET':
            product_serializer = ProductSerializer(product)
            return JsonResponse(product_serializer.data)
        
        elif request.method == 'PUT':
            product_data = JSONParser().parse(request)
            product_serializer = ProductSerializer(product, data = product_data)
            if product_serializer.is_valid():
                product_serializer.save()
                return JsonResponse(product_serializer.data,status = status.HTTP_201_CREATED)
            return JsonResponse(product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            product.delete()
            return JsonResponse({"message":"Deleted Successfuly"},status = status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return JsonResponse({"message":str(e)},status = status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def product_total(request,pk):
    try:
        product = Product.objects.get(pk = pk)
    except Exception as e:
        return JsonResponse({"Message": str(e)},status = status.HTTP_404_NOT_FOUND)
    print(product)
    quantity = product.quantity
    price = product.price
    name = product.name

    response = f"The Product {name} is of price {price} and quantity {quantity} Total will be {(float(price))*(float(quantity))}"

    return JsonResponse({"message":str(response)})


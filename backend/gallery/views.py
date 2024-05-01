from django.shortcuts import render ,redirect,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    if request.method == "GET":
        products=Product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
    elif request.method =="POST":
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def product_detail(request,pk):
    if request.method =="GET":
        product=Product.objects.get(pk=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    
# @api_view(['GET','PUT'])
# def edit_product(request,pk):
#     product=get_object_or_404(Product,pk=pk)
#     if request.method=="PUT":
#         form = ProductForm(request.POST,instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect("product_list")
#     else:
#         form=ProductForm(instance=product)
#     return render(request,'edit.html',{"form":form})

# @api_view(['GET','DELETE'])
# def delete_product(request,pk):
#     product=get_object_or_404(Product,pk=pk)
#     if request.method=="DELETE":
#         product.delete()
#         return redirect('product_list')
#     return render(request,"delete.html",{"product":product})
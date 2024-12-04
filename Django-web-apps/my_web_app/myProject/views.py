from django.shortcuts import render
from .models import EmployeeModel
from .forms import EmployeeForm
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    return HttpResponse('Hello to Myapp - Shivam')

def create_view(req):
    context = {}
    form = EmployeeForm(req.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form

    return render(req,"create_view.html",context)

def list_view(request):
    context = {}
    context['dataset'] = EmployeeModel.objects.all()

    return render(request,'list_view.html',context)

def detail_view(request,id):
    context={}
    context['data'] = EmployeeModel.objects.get(id = id)
    print(context,type(context['data']))
    return render(request,'detail_view.html',context)

def update_view(request,id):
    context = {}
    obj = get_object_or_404(EmployeeModel,id = id)
    form = EmployeeForm(request.POST or None,instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/detail_list/"+id)
    context['form'] = form

    return render(request,'update_view.html',context)

def delete_view(request,id):
    context = {}
    obj = get_object_or_404(EmployeeModel,id = id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect("/list")

    return render(request,'delete_view.html',context)

# # Product Views

# def create_view_product(req):
#     context = {}
#     form = ProductForm(req.POST or None)
#     if form.is_valid():
#         form.save()
#     context['form'] = form

#     return render(req,"product_create_view.html",context)

# def list_view_product(request):
#     context = {}
#     context['dataset'] = ProductModel.objects.all()

#     return render(request,'product_list_view.html',context)

# def detail_view_product(request,id):
#     context={}
#     context['data'] = ProductModel.objects.get(id = id)
#     print(context,type(context['data']))
#     return render(request,'product_detail_view.html',context)

# def update_view_product(request,id):
#     context = {}
#     obj = get_object_or_404(ProductModel,id = id)
#     form = ProductForm(request.POST or None,instance = obj)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/detail_list_product/"+id)
#     context['form'] = form

#     return render(request,'product_update_view.html',context)

# def delete_view_product(request,id):
#     context = {}
#     obj = get_object_or_404(ProductModel,id = id)

#     if request.method == 'POST':
#         obj.delete()
#         return HttpResponseRedirect("/list_product")

#     return render(request,'product_delete_view.html',context)
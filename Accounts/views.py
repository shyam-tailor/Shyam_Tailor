from django.shortcuts import render, redirect,HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, ListView


from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from .forms import UserLoginForm, UserRegisterForm
from .models import *
from Homeapp.models import  Product
from math import ceil
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404


        
        # context = super().get_context_data(**kwargs)
        
        # context['product']=Product.objects.all()
        # context['mens']=Product.objects.filter(subcategory="mens")
        # context['womens']=Product.objects.filter(subcategory="womens")
        # context['accessories']=Product.objects.filter(subcategory="accessories")
        # print(context['mens'])
        # n=len(context['product'])
 

        # context['nslides']=n//3 + ceil((n/3)-(n//3))
        # print(context['nslides'])
        # context['range']=range(1,context['nslides'])
        # print(context['range'])
        
        

 
def login_view(request):

    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    context={}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print("users=",user)
        usr=Userprofile.objects.filter(user=user)
        product=Product.objects.all()
        mens=Product.objects.filter(subcategory="men's")
        womens=Product.objects.filter(subcategory="women's")
        accessories=Product.objects.filter(subcategory="accessories")
        
        n=len(product)
        nslides=n//3 + ceil((n/3)-(n//3))
        ranges=range(1,nslides)
        # print("users2=",usr[0].number)
        login(request, user)
        context={'users':usr,'product':product,'mens':mens,'womens':womens,'accessories':accessories,'range':ranges,'nslides':nslides}

        
        if next:
            return redirect(next)
        return render(request,'home.html',context)

    context = {
        'form': form,
    }
    return render(request, "login.html", context)


def register_view(request):
    next = request.GET.get('next')
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/login')

    context = {
        'form': form,
    }
    return render(request, "signup.html", context)


def logout_view(request):
    print("Logout")
    logout(request)
    return redirect('/login')

class Productview(TemplateView):
    template_name="product.html"
    # slug_url_kwarg = 'myid'

    def get_queryset(self):
        self.id = get_object_or_404(Product, id=self.kwargs['myid'])
        detail=Product.objects.filter(product_name=self.id)
        
        return(Product.objects.filter(product_name=self.id))
 

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['details']=Product.objects.filter(id=context['myid'])
        print("Details=",context['details'])
        for i in context['details']:
            context['descriptionlist']=i.desc.split(';')
            
            
        
        return context


class WomenProductview(TemplateView):
    template_name="product.html"
    # slug_url_kwarg = 'myid'

    def get_queryset(self):
        self.id = get_object_or_404(Womens, id=self.kwargs['myid'])
        detail=Womens.objects.filter(product_name=self.id)
        
        return(Womens.objects.filter(product_name=self.id))
 

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['details']=Womens.objects.filter(id=context['myid'])
        print("Details=",context['details'])
        for i in context['details']:
            context['descriptionlist']=i.desc.split(';')
            
            
        
        return context


class MenProductview(TemplateView):
    template_name="product.html"
    # slug_url_kwarg = 'myid'

    def get_queryset(self):
        self.id = get_object_or_404(Womens, id=self.kwargs['myid'])
        detail=Mens.objects.filter(product_name=self.id)
        
        return(Mens.objects.filter(product_name=self.id))
 

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['details']=Mens.objects.filter(id=context['myid'])
        print("Details=",context['details'])
        for i in context['details']:
            context['descriptionlist']=i.desc.split(';')
            
            
        
        return context




class Womensview(TemplateView):
    template_name="womens.html"
    def get_context_data(self, **kwargs):
        
        women = super().get_context_data(**kwargs)
        # women['womens']=Womens.objects.filter(subcategory="women's")
        women['salwarsuit']=Womens.objects.filter(category="salwar suit")
        women['tops']=Womens.objects.filter(category="top")
        women['tshirts']=Womens.objects.filter(category="t-shirt")
        women['jeans']=Womens.objects.filter(category="jeans")
        
        
        return women


class Mensview(TemplateView):
    template_name="mens.html"
    def get_context_data(self, **kwargs):
        
        men = super().get_context_data(**kwargs)
        men['shrug']=Mens.objects.filter(category="shrug")
        men['tshirt']=Mens.objects.filter(category="t-shirt")
        men['blazor']=Mens.objects.filter(category="blazor")
        # women['tshirts']=Womens.objects.filter(category="t-shirt")
        men['jeans']=Mens.objects.filter(category="jeans")
        
        
        return men

class Accessoriesview(TemplateView):
    template_name="accessories.html"
    def get_context_data(self, **kwargs):
        
        accessories = super().get_context_data(**kwargs)
        accessories['sunglasses']=Accessories.objects.filter(category="sunglasses")
        accessories['bags']=Accessories.objects.filter(category="bags")
        accessories['shoes']=Accessories.objects.filter(category="shoes")
        # women['tshirts']=Womens.objects.filter(category="t-shirt")
        # accessories['jeans']=Accessories.objects.filter(category="jeans")
        print("Done")
        
        
        return accessories






 
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
        

        # print(self.id)
        # context['detail']=Product.objects.filter(id=self.id)
        # print(context['detail'])


    







# from django.shortcuts import render, redirect

# from django.views.generic import View, CreateView
# from django.contrib.auth import get_user_model
# User=get_user_model()

# from django.contrib.auth import (
#     authenticate,
#     get_user_model,
#     login,
#     logout
# )

# from .forms import UserLoginForm, UserRegisterForm


# class LoginView(View):
#     model = User
#     form = UserLoginForm
#     template_name = 'login.html'
#     context={}
#     def get(self, request, *args, **kwargs):
#         form = self.form()
#         self.context['title'] = 'Login'
#         self.context['form'] = form
#         return render(request, self.template_name, self.context)
#     def post(self, request, *args, **kwargs):
#         form = UserLoginForm(request.POST or None)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
            
#             return redirect('/signup')

#         context = {
#             'form': form,
#         }
#         return render(request, "login.html", context)

# 

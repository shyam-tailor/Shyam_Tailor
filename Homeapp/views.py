from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ContactForm
from .models import Product
from math import ceil

# Create your views he 
# class Homeview(TemplateView):
#     template_name="home.html"
    # def get_context_data(self, **kwargs):
        
    #     context = super().get_context_data(**kwargs)
        
    #     context['product']=Product.objects.all()
    #     context['mens']=Product.objects.filter(subcategory="mens")
    #     context['womens']=Product.objects.filter(subcategory="womens")
    #     context['accessories']=Product.objects.filter(subcategory="accessories")
    #     print(context['mens'])
    #     n=len(context['product'])


    #     context['nslides']=n//3 + ceil((n/3)-(n//3))
    #     print(context['nslides'])
    #     context['range']=range(1,context['nslides'])
    #     print(context['range'])
        
    #     return context


    

class Formview(TemplateView):
    
    template_name="form.html"
    
    form_class="ContactForm"

    def get(self,request):
        form=ContactForm()
        return render(request,self.template_name,{'form':form})

    
        
        

    


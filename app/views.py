from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .serializers import PropertySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q



# Create your views here.
def home(request):

    context = {
    
        'properties' : Property.objects.all().order_by('-id'),
        'property' : Property.objects.all().last(),
        'footer_properties' : Property.objects.all().order_by('-id')[:3],
        'chicago' : Property.objects.filter(city='Chicago'),
        'ny' : Property.objects.filter(city='New York'),
        'wa' : Property.objects.filter(city='Washington'),
        'houston' : Property.objects.filter(city='Houston'),
    }

    return render(request, 'index.html', context)


def search(request):
	if request.GET:
		search_term = request.GET['search_term']
		search_results = Property.objects.filter(
			Q(name__icontains=search_term)  |
			Q(city__icontains=search_term) |
			Q(price__icontains=search_term) |
			Q(address__icontains=search_term)
		)
		context = {
			'search_term': search_term,
			'properties' : search_results,
            'footer_properties' : Property.objects.all().order_by('-id')[:3]
		}
		return render(request, 'search.html', context)
	else:
		return redirect('home')



def properties(request):

    context = {
    
        'properties' : Property.objects.all().order_by('-id'),
        'footer_properties' : Property.objects.all().order_by('-id')[:3]
    }

    return render(request, 'properties.html', context)





class SignUpView(CreateView):
	form_class = UserCreationForm
	template_name = 'registration/register.html'
	success_url = reverse_lazy('login')





def about(request):
    context = {
        'properties' : Property.objects.all(),
        # 'property' : Property.objects.get(id=1),
        'footer_properties' : Property.objects.all().order_by('-id')[:3]       
    }

    return render(request, 'about.html', context)


def contact(request):
    context = {
    
        'properties' : Property.objects.all().order_by('-id'),
        'footer_properties' : Property.objects.all().order_by('-id')[:3]
    }

    return render(request, 'contact.html', context)



def property(request, pk):

    context = {
    
        'footer_properties' : Property.objects.all().order_by('-id')[:3],
        'property' : Property.objects.get(id=pk)
    }

    return render(request, 'properties-details.html', context)

@login_required
def dashboard(request):

    context={
        'properties' : Property.objects.all().order_by('-id'),
        'footer_properties' : Property.objects.all().order_by('-id')[:3]
    }

    return render(request,'dashboard.html', context)



@login_required
def pay(request):
    context = {
        'footer_properties' : Property.objects.all().order_by('-id')[:3]
    }

    return render(request, 'buy.html', context)


        
class PropertyCreateView(CreateView, LoginRequiredMixin):
    model = Property
    template_name = 'submit-property.html'
    fields = '__all__'
    
    def form_valid(self, form):
        instance = form.save()
        messages.success(self.request, "Your property has been successfully added")
        return redirect('property-detail', instance.pk)




class PropertyUpdateView(LoginRequiredMixin, UpdateView):
	model = Property
	template_name = 'update.html'
	fields = '__all__'
	
	def form_valid(self, form):
		instance = form.save()
		messages.success(self.request, "Your contact has been successfully updated")
		return redirect('property-detail', instance.pk)


class PropertyCreateAPIView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


def delete_property(request, pk):
    queryset = Property.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/')
    context = {
        'property' : queryset,
        'footer_properties' : Property.objects.all().order_by('-id')[:3]
    }

    return render(request, 'delete.html', context)


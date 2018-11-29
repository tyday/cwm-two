from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def index(request):
    if request.method == 'GET':
        form = ContactForm()
    
    return render(request,'cwm_index/index.html',{'form':form})
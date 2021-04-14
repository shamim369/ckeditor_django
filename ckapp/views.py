from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreationForm

# Create your views here.
def index(request):
    product = Product.objects.all()
    ctx = {
        'product': product,
    }
    return render(request, 'index.html', ctx)

def create_product(request):
    if request.method == "POST":  
        form = ProductCreationForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = ProductCreationForm()  
    return render(request, 'create.html', {'form':form})



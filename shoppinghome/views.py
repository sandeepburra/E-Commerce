from django.shortcuts import render, HttpResponse
from .models import Product, Image
from .recommendation import get_similar_products_new
from .tfidf import tfidf_model
from .form import ImageForm
from .helpers import RandomFileName

# Create your views here.
def index(request):
    
        
    products = Product.objects.order_by('?')[:12]
   
    form = ImageForm()
    
    return render(request ,'home-page.html', {'products': products, 'form' : form})

def titleindex(request):

    products = Product.objects.order_by('?')[:12]
    form = ImageForm()
    return render(request ,'home-page2.html', {'products': products, 'form' : form})



def similar(request, qid):
    query_image= Product.objects.get(id=qid)
    

    imagelist = get_similar_products_new(query_image.product_Url,20)
    

    products2 = Product.objects.filter(product_img__in = imagelist)

    
    return render(request, 'detail-page.html', {"current_image" : query_image, "imlist" : products2})

def similartitle(request, qid):
    query_image= Product.objects.get(id=qid)
    imagelist = tfidf_model(query_image.title)
    products2 = Product.objects.filter(product_img__in = imagelist)
    
    return render(request, 'detail-page2.html', {"current_image" : query_image,"imlist" : products2})


def uploaded(request):

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #print(RandomFileName.__call__.name)
            Uploaded_path = "https://sandeepfileuploads.s3.amazonaws.com/" + RandomFileName.__call__.name
            imagelist = get_similar_products_new(Uploaded_path,30)
    
            products2 = Product.objects.filter(product_img__in = imagelist)
            return render(request, 'product-page.html',{"imlist" : products2})

def search(request):
    query = request.GET['query']
    form = ImageForm()
    imagelist = tfidf_model(query)
    products2 = Product.objects.filter(product_img__in = imagelist)
    return render(request ,'home-page.html', {'products': products2, 'form' : form})

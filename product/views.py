from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from .models import Product,City,Category,ProductImage
# , City
from django.db.models import Count
from .forms import ProductForm
# paGINATION
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# # Create your views here.
def productlist(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-created').filter(featured_post=0)
    featured_posts = Product.objects.filter(featured_post=1)

    paginator = Paginator(products,4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request,'product/index.html',{
        'categories':categories,
        'products':paged_listings,
        'featured_post':featured_posts,
        })


def product_detail(request,slug):
    # product = get_object_or_404(Product, id=id)    
    pro = Product.objects.get(slug=slug)
    # return render(request,'product/product_details.html',{'pro':pro})
    return render(request,'product/single.html',{'pro':pro})



def all_products(request):
    products = Product.objects.all()
    return render(request,'product/all_products.html',{'products':products})

# try
def all_items(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('-created').filter(featured_post=0)
    featured_posts = Product.objects.filter(featured_post=1)
    paginator = Paginator(products,1)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    return render(request,'product/all_items.html',{
        'categories':categories,
        'products':paged_listings,
        'featured_post':featured_posts,
        })


def category_detail(request,slug):
    category = get_object_or_404(Category,slug=slug)
    cat_product = Product.objects.filter(category=category)
    categories = Category.objects.annotate(total_products=Count('product'))
    return render(request,'product/try.html',
        {
        'title':category,
        'cat_product':cat_product,
        'categories':categories
        })
# @login_required(login_url='/login/')


@method_decorator(login_required, name='dispatch')
class ProductCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def load_cities(request):
    state_id = request.GET.get('state')
    cities = City.objects.filter(state_id=state_id).order_by('name')
    return render(request, 'product/city_dropdown_list_options.html', {'cities': cities})


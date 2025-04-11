from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
from .utils import extract_features
import numpy as np
from io import BytesIO

class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    paginate_by = 12
    ordering = ['-created_at']

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('product-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

def image_search(request):
    if request.method == 'POST' and request.FILES.get('image'):
        # Handle file upload
        fs = FileSystemStorage()
        uploaded = fs.save(request.FILES['image'].name, request.FILES['image'])
        query_path = fs.path(uploaded)
        
        # Extract features
        query_features = np.load(BytesIO(extract_features(query_path)))
        
        # Calculate similarities
        results = []
        for product in Product.objects.exclude(features=None):
            product_features = np.load(BytesIO(product.features))
            similarity = np.dot(query_features, product_features)
            results.append((product, similarity))
        
        # Sort and return results
        results.sort(key=lambda x: x[1], reverse=True)
        return render(request, 'products/search_results.html', {
            'results': results[:5],
            'query_image': fs.url(uploaded)
        })
    
    return render(request, 'products/search.html')
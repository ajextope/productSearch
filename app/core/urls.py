from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import CustomLoginView, CustomLogoutView, RegisterView, ProfileView
from products.views import ProductListView, ProductCreateView, image_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductListView.as_view(), name='product-list'),
    path('search/', image_search, name='image-search'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    
    # Authentication URLs
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
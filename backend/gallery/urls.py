from django.urls import path,include
from gallery import views

from django.conf import settings # here
from django.conf.urls.static import static # here

urlpatterns = [
    path('api/products',views.product_list,name="product_list"),
    path('api/product/<int:pk>/',views.product_detail,name="product_detail"),
    # path('<int:pk>/edit',views.edit_product,name="edit_product"),
    # path('<int:pk>/delete',views.delete_product,name="delete_product"),
]+ static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)# here
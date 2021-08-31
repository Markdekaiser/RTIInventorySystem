from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.indexView),

    path('customers', views.customer,name="customer"),
    path('customers/details/<str:id>', views.customerDetail,name="customerDetail"),

    path('order/all', views.createRequest, name="create_order"),
    path('order/pending', views.pending, name="pending"),
    path('order/accepted', views.accepted, name="accepted"),
    path('order/partial', views.partial, name="partial"),
    path('order/delivered', views.delivered, name="delivered"),

    path('order/details/<str:id>', views.details, name="details"),
    path('order/accept/<str:id>', views.acceptOrder, name="acceptOrder"),
    path('order/updatePart/<str:id>', views.updatePart, name="updatePart"),
    path('order/updateFull/<str:id>', views.updateFull, name="updateFull"),

    path('products', views.productView, name="products"),

    #For Authentication
    path('login/', views.loginView, name="login"),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL} , name="logout"),
    path('register/', views.registerView, name="register"),
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
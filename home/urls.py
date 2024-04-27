from django.urls import path 
from.import views 


urlpatterns = [ 
    path('', views.index, name='home'),    
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/', views.products, name='products'),
    path('updateItem/', views.updateItem, name='updateitem'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),

]


    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),


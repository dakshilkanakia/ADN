from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('add_apparel/', views.add_apparel, name='add_apparel'),
    path('apparel/<int:apparel_id>/', views.apparel, name='apparel'),
    path('delete_apparel/<int:pk>', views.delete_apparel, name='delete_apparel'),
    path('confirm_delete/<int:pk>', views.confirm_delete, name='confirm_delete'),
    path('update_apparel/<int:pk>', views.update_apparel, name='update_apparel'),
]

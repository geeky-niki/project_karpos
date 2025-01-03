#import path from django
from django.urls import path
from . import views

# give url patterns
urlpatterns = [
  path('data', views.view_karpos , name = 'vw_krps'),
  path('', views.external_homepage, name='homepage'),  # Root URL
  path('<int:cust_id>',views.view_karpos_by_id, name ='karpos_by_id')
]
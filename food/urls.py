from . import views
from django.urls import path

app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'), # --> function based view
    # path('', views.IndexClassView.as_view(), name='index'), # --> class based view
    # path('<int:item_id>/', views.detail, name='detail'), # --> function based view
    path('<int:pk>', views.FoodDetailView.as_view(), name='detail'), # --> class based view
    path('add', views.CreateItemView.as_view(), name='create_item'),
    path('edit/<int:item_id>', views.edit_item, name='edit_item'),
    path('delete/<int:item_id>', views.delete_item, name='delete_item'),
]

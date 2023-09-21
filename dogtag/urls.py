from django.urls import path
from .views import DogInfoCreateView, DogInfoUpdateView, DogInfoDeleteView, DogInfoDetailView, DogInfoListView

app_name = 'dogtag'  # 앱 이름 설정

urlpatterns = [
    path('doginfo/', DogInfoListView.as_view(), name='doginfo_list'),
    path('doginfo/new/', DogInfoCreateView.as_view(), name='doginfo_create'),
    path('doginfo/<int:pk>/edit/', DogInfoUpdateView.as_view(), name='doginfo_update'),
    path('doginfo/<int:pk>/delete/', DogInfoDeleteView.as_view(), name='doginfo_delete'),
    path('doginfo/<int:pk>/', DogInfoDetailView.as_view(), name='doginfo_detail'),
]

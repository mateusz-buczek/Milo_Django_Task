from django.urls import path

from .views import ProfileListView, CreateProfileView, ProfileDetailView, UpdateProfileView, DeleteProfileView, csv_view


app_name = 'custom_user'
urlpatterns = [
    path('add/', CreateProfileView.as_view(), name='create'),
    path('user/<int:pk>/', ProfileDetailView.as_view(), name='details'),
    path('user/<int:pk>/edit/', UpdateProfileView.as_view(), name='update'),
    path('user/<slug:pk>/delete/', DeleteProfileView.as_view(), name='delete'),
    path('', ProfileListView.as_view(), name='profiles'),
    path('download/', csv_view, name='download'),

]

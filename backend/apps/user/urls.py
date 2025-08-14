from django.urls import path
from .views import UserListCreateView, BlockUserView, SendEmailView
urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create '),
    path('/<int:pk>', BlockUserView.as_view(), name='block'),
    path('/test', SendEmailView.as_view(), name='send_email'),
]
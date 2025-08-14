from django.urls import path

from apps.pizza.views import PizzaCreateListView, PizzaRetrieveUpdateDestroyView, PizzaAddPhotoView

urlpatterns = [
    path('', PizzaCreateListView.as_view()),
    path('/<int:pk>', PizzaRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/photos', PizzaAddPhotoView.as_view()),
]
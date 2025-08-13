from django.urls import path

from apps.pizza.views import PizzaCreateListView, PizzaRetrieveUpdateDestroyView

urlpatterns = [
    path('', PizzaCreateListView.as_view()),
    path('/<int:pk>', PizzaRetrieveUpdateDestroyView.as_view()),
]
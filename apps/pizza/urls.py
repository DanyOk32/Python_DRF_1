from django.urls import path

from apps.pizza.views import PizzaCreateListView, PizzdaRetrieveUpdateDestroyView

urlpatterns = [
    path('', PizzaCreateListView.as_view()),
    path('/<int:pk>', PizzdaRetrieveUpdateDestroyView.as_view()),
]
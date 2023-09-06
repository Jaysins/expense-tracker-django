from django.urls import path
from expenses.views.expense import ExpenseView
from expenses.services.expense import ExpenseService

expense = ExpenseView.as_view(service_class=ExpenseService, serializer_class=ExpenseView.serializer_class)

urlpatterns = [
    path('expenses', expense, name='expense'),
    path('expenses/<int:obj_id>', expense, name='expense-detail'),
]

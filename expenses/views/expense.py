from expenses.base.views import BaseView
from expenses.serializers import ExpenseSerializer


class ExpenseView(BaseView):
    """

    """
    serializer_class = ExpenseSerializer
    service_class = None

    def save(self, data):
        """

        """
        return self.service_class.register(**data)

from expenses.models import Expense
from expenses.base.service import ServiceFactory

BaseExpenseService = ServiceFactory.create_service(Expense)


class ExpenseService(BaseExpenseService):

    @classmethod
    def register(cls, **kwargs):
        """

        """
        return cls.create(**kwargs)

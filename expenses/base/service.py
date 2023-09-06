from expenses.helpers.utils import clean_kwargs, populate_obj


class ServiceFactory:

    @classmethod
    def create_service(cls, model_klass):
        """

        """

        class BaseService:
            model_class = model_klass

            @classmethod
            def create(cls, ignored_args=None, **kwargs):
                if not ignored_args:
                    ignored_args = ["_id", "date_created", "last_updated", "pk"]

                data = clean_kwargs(ignored_args, kwargs)
                obj = populate_obj(cls.model_class(), data)
                return obj.save()

            @classmethod
            def filter(cls, filters):
                return cls.model_class.objects.filter(**filters)

            @classmethod
            def get(cls, obj_id):
                try:
                    obj = cls.filter(dict(id=obj_id)).get()
                    return obj
                except cls.model_class.DoesNotExist:
                    print("Object not found.")

            @classmethod
            def find_one(cls, filters):
                try:
                    return cls.filter(filters).get()
                except cls.model_class.MultipleObjectsReturned:
                    print("multiple")
                except cls.model_class.DoesNotExist:
                    print("not found")

            @classmethod
            def update(cls, obj_id, data):
                # Implement update logic here
                pass

            @classmethod
            def delete(cls, obj_id):
                # Implement delete logic here
                pass

        return BaseService

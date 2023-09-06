from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BaseView(APIView):

    def __init__(self, *args, **kwargs):
        print("ovaries")
        print(args)
        print(kwargs)
        serializer_class = kwargs.pop('serializer_class', None)
        service_class = kwargs.pop('service_class', None)

        super().__init__(*args, **kwargs)

        self.serializer_class = serializer_class
        self.service_class = service_class

    def save(self, data):
        """

        """
        return self.service_class.create(**data)

    def fetch(self, obj_id):
        """

        """
        obj = self.service_class.get(obj_id)
        return obj

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            res = self.save(serializer.validated_data)
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, obj_id=None, **kwargs):
        if obj_id:
            obj = self.service_class.get(obj_id)
            serializer = self.serializer_class(obj)

        else:
            obj = self.service_class.filter({})
            print("in here===<", obj)
            serializer = self.serializer_class(obj, many=True)

        return Response(serializer.data)

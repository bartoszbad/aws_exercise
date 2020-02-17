import random

from rest_framework import views
from rest_framework.response import Response


class EchoView(views.APIView):
    def post(self, request):
        json_message = request.data
        data = {"status": "ok", "msg": json_message}
        return Response(data)


class RandomView(views.APIView):
    def get(self, request):
        data = {"status": "ok", "number": random.randint(0, 100)}
        return Response(data)

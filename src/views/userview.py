from django.http import JsonResponse
from rest_framework.views import APIView

class Userview(APIView):

    def get(self,requests):
        print requests.GET
        Response = {"success": True, "message" : "GET APT working succesfuly"}
        return JsonResponse(Response)

    def post(self,requests):
        print requests.data
        Response = {"success": True, "message" : "POST APT working succesfuly"}
        return JsonResponse(Response)
from django.http import JsonResponse
from rest_framework.views import APIView
from src.libraries.userlib import UserLib

class Userview(APIView):

    def get(self,requests):
        print requests.GET
        Response = {"success": True, "message" : "GET APT working succesfuly"}
        return JsonResponse(Response)

    def post(self,requests):
        response_text, success_status = UserLib().createUser(user_info=requests.data)
        Response = {"success": success_status, "message" : response_text}
        return JsonResponse(Response)
from __future__ import unicode_literals
import json
from models import StaffTable

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def test_view(requests):
    print requests
    response = {"message": "API Working Successfully"}
    return JsonResponse(response)

@csrf_exempt
def staff_db_test(requests):
    if (requests.method== "GET"):
        response_obj= StaffTable.objects.all()
        response = {"data" : []}
        for element in response_obj:
            response["data"].append(
                {
                    "name": element.name,"designation" : element.desig,"staff scale " : element.s_scale
                }
            )

        #print a
        #response =  {"message": "GET method is Working Successfully"}
    elif (requests.method== "PUT"):
        response = {"message": "PUT method is Working Successfully"}
    elif (requests.method== "POST"):
        request_body = json.loads(requests.body)
        StaffTable.objects.create(**request_body)
        response = {"message": "POST method is Working Successfully"}
    else :
        response = {"message": "DELETE method is Working Successfully"}

    return JsonResponse(response)

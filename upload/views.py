from django.shortcuts import render

from django.http.response import HttpResponse

import time
from asgiref.sync import sync_to_async


def te(request):
    print("start")
    time.sleep(3)
    print("finish...")
    return HttpResponse("finish")

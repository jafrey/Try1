from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

import requests
import json

@csrf_exempt
def login(request):

     if request.method == "GET":

       v = ""
       return render_to_response('login.html', { 'dato' : v })

     else:

         usuario = request.POST['username']
         contra = request.POST['password']

         r = requests.post("http://api:8000/api/login", data={'username': usuario, 'password': contra})
         jsonData = r.json()


         if r.status_code == 400:
             jsonData = r.json()
             v = jsonData["error"]
             return render_to_response('login.html', { 'dato' : v })
             v = ""

         elif r.status_code == 404:
             v = jsonData["error"]
             return render_to_response('login.html', { 'dato' : v })

         elif r.status_code == 200:
             jsonData = r.json()
             v = "De culo funca todo bien, por ahora. Acá ta tu token del orto " + jsonData["token"]
             return render_to_response('login.html', { 'dato' : v })

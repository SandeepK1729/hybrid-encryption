import random
import string

from cryptography.fernet import Fernet
from django.forms import JSONField
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse

from django.views.decorators.csrf import csrf_exempt
import json
from .encryption import *

def index(request):
    return render(request, 'home.html')

@csrf_exempt
def generate(request):
	if request.method == "POST":
		# Get the data from the request
		data = request.body.decode("utf-8")
		data = json.loads(data) 

		# Get the selected action
		action = data["action"]

		# Get the input text
		text = data["text"]

		# get number of algo's
		n = int(data.get('n', '1'))

		
		algorithms = []
		for i in range(1, n + 1):
			algorithms.append({
				'name' : data.get(f"algorithm{i}"),
				'key'  : data.get(f"key{i}")
			})

		

		# Encrypt or decrypt the text based on the selected action
		output = text
		algo_type = get_action(action)

		for algorithm in algorithms:
			func = algo_type[algorithm['name']]
			output = func(output, algorithm['key'])
		
		# Return the output as a JSON response
		return HttpResponse(output)

	return HttpResponse("NONE")
# Imports the Google Cloud client library
import os
import io
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import translate

from django.http import HttpResponse
from django.shortcuts import render



# Instantiates a client
def google(request):
	translate_client = translate.Client()
	vision_client = vision.ImageAnnotatorClient()
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    'download.png')

	print("\n\n\n")
	print(request)
	print("\n\n\n")

	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)

	# Performs label detection on the image file
	response = vision_client.label_detection(image=image)
	labels = response.label_annotations


	# The target language
	target = 'es'

	# Translates some text into spanish
	translation = translate_client.translate(
	    labels[0].description,
	    target_language=target)
	name = translation['translatedText']
	args = {'myName':name}
	return render(request, 'webapp/template2.html', args)
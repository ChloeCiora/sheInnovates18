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

	#for label in labels:
	#    print(label.description)

	answer1 = labels[0].description
	answer2 = labels[1].description
	answer3 = labels[2].description

	prob1 = labels[0].score

	# The target language
	target = 'es'

	# Translates some text into turkish
	translation1 = translate_client.translate(
	    answer1,
	    target_language=target)

	translation2 = translate_client.translate(
	    answer2,
	    target_language=target)

	translation3 = translate_client.translate(
	    answer3,
	    target_language=target)

	#return HttpResponse("<h2> This is your translation: " + translation1['translatedText'] + "</h2>")
	name = translation1['translatedText']
	args = {'myName':name}
	return render(request, 'webapp/template2.html', args)


'''
print(answer1)
print(prob1*100)
print(u'Translation: {}'.format(translation1['translatedText']))
print(answer2)
print(u'Translation: {}'.format(translation2['translatedText']))
print(answer3)
print(u'Translation: {}'.format(translation3['translatedText']))
'''

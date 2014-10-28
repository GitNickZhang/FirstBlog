from django.shortcuts import render_to_response
from django.http import HttpResponse
# Create your views here.


def index(req):
    return render_to_response('content.html', {'User': 'Nick'})

def page(req, page=0):
	pages = range(1, 11)
	width = 11 * (67 / 2)
	return render_to_response('content.html', {
		'User': 'Nick', 
		'pages': pages, 
		'current_page': int(page),
		'width': width,
		})

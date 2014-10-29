from django.shortcuts import render_to_response
from blog.models import BlogPost
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.


def index(req):
    return render_to_response('content.html', {'User': 'Nick'})

def page(req):
	post_list = BlogPost.objects.all()
	paginator = Paginator(post_list, 2)
	num_pages = paginator.num_pages
	pages = range(1, num_pages + 1)
	width = num_pages * 34

	# Make sure page request is an int. If not, deliver first page.
	try:
		page = int(req.GET.get('page', '1'))
	except ValueError:
		page = 1

	# If page request (9999) is out of range, deliver last page of results.
	try:
		posts = paginator.page(page)
	except (EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)


	return render_to_response('content.html', {
		'User': 'Nick', 
		'pages': pages, 
		'current_page': int(page),
		'width': width,
		'posts': posts,
		})

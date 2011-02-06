
def starting_page(request):
    if request.user.is_authenticated():
	    page = get go user page
    else:
   		page = get  starting page
	return page

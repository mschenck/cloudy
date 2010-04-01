from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    msg = "Hello World!"
    return render_to_response( 'consoleHome/index.html', {'message': msg,} )


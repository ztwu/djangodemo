from datetime import datetime
from django.http import HttpResponse

def sayHello(request):
    s = 'Hello World!'
    current_time = datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)
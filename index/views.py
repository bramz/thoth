from django.http import HttpResponse
from django.template.loader import get_template

def index_view(request):
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)

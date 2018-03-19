from django.shortcuts import render
from django.http import HttpResponse
from excuses.models import RootCause
from django.template import loader
from django.http import Http404

# Create your views here.
def index(request):
    latest_excuses_list = RootCause.objects.all()[:10]
    template = loader.get_template('index.html')
    context = {
        'latest_excuses_list': latest_excuses_list,
    }
    return HttpResponse(template.render(context, request))

def excuse(request, excuse_id):
    try:
        excuse_detail = RootCause.objects.get(pk=excuse_id)
    except:
        raise Http404("This content is not available in your country.")
    return render(request, 'detail.html', {'excuse_detail': excuse_detail})
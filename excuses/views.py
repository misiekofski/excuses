from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from excuses.models import RootCause, Bug
from django.template import loader
from django.http import Http404, JsonResponse

# Create your views here.
def index(request):
    latest_excuses_list = RootCause.objects.all()[:10]
    template = loader.get_template('index.html')
    context = {
        'latest_excuses_list': latest_excuses_list,
    }
    return HttpResponse(template.render(context, request))

def excuse(request, excuse_id):
    rootcause = get_object_or_404(RootCause, pk=excuse_id)
    return render(request, 'detail.html', {'rootcause': rootcause})

def bugs_list(request):
    MAX_OBJECTS = 20
    bugs = Bug.objects.all()[:MAX_OBJECTS]
    data = {"results": list(bugs.values("bug_description", "created_by__username", "pub_date"))}
    return JsonResponse(data)
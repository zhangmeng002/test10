from django.shortcuts import render, HttpResponse

# Create your views here.
def views_index(request):
    return render(request, 'index.html')


def query1_view(request, year, month, name):

    return HttpResponse('hello_%s_%s_%s' % (name, year, month))


def index(request):
    sch = request.META
    return HttpResponse('Scheme: %s'% sch)

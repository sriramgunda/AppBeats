from django.http import HttpResponse


def index(request):
    return HttpResponse("AppBeats check the status of infrastrucutre .")
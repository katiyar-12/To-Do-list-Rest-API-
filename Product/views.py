from django.http import JsonResponse

def home(request) :
    return JsonResponse({
        'message' : 'welcome to my To Do API '
    })




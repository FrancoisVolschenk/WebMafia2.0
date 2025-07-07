from django.http import JsonResponse

def hello(request):
    return JsonResponse({"status": "Hello from django"})
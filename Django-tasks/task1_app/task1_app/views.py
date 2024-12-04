from django.http import HttpResponse

def welcom_view(req):
    return HttpResponse(f"Welcome to task1 of Django created on 2-12-2024 Shivam Here")
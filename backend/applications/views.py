from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "Backend is working pedazo de corazónm de melón!"})

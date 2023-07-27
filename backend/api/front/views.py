from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def detail_profile(request):
    contact_id = request.GET.get("id")
    return render(request, "detail_profile.html", {"contact_id": contact_id})


def create(request):
    return render(request, "create.html")

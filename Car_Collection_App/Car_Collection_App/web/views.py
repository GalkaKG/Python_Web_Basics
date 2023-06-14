from django.shortcuts import render

from Car_Collection_App.web.models import Profile


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    context = {
        'profile': profile
    }

    return render(request, 'base/index.html', context)


def catalogue(request):
    return render(request, 'base/catalogue.html')


def profile_create(request):
    return render(request, 'profile/profile-create.html')


def profile_details(request):
    return render(request, 'profile/profile-details.html')


def profile_edit(request):
    return render(request, 'profile/profile-edit.html')


def profile_delete(request):
    return render(request, 'profile/profile-delete.html')


def car_create(request):
    return render(request, 'car/car-create.html')


def car_details(request, pk):
    return render(request, 'car/car-details.html')


def car_edit(request, pk):
    return render(request, 'car/car-edit.html')


def car_delete(request):
    return render(request, 'car/car-delete.html')

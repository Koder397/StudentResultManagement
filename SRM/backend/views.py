
from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout
from backend.models import Student, Country, State, City, MarkList
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, CreateView, UpdateView, DeleteView


@login_required
def dashboard(request):
    content = {
        "student_count": Student.objects.all().aggregate(total_count=Count('name')).get('total_count')
    }

    return render(request, "backend/dashboard.html", content)


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'backend/login.html')


def admin_logout(request):
    logout(request)
    return redirect('login')


class CountryList(ListView):
    model = Country

    template_name = "backend/country/list.html"


class CountryNew(CreateView):
    model = Country

    template_name = "backend/country/create.html"

    fields = "__all__"

    success_url = "/backend/country"


class CountryUpdate(UpdateView):
    model = Country

    template_name = "backend/country/update.html"

    fields = "__all__"

    success_url = "/backend/country"


class CountryDelete(DeleteView):
    model = Country

    template_name = "backend/country/delete.html"

    success_url = "/backend/country"


class StateList(ListView):
    model = State

    template_name = "backend/state/list.html"


class StateNew(CreateView):
    model = State

    template_name = "backend/state/create.html"

    fields = "__all__"

    success_url = "/backend/state"


class StateUpdate(UpdateView):
    model = State

    template_name = "backend/state/update.html"

    fields = "__all__"

    success_url = "/backend/state"


class StateDelete(DeleteView):
    model = State

    template_name = "backend/state/delete.html"

    success_url = "/backend/state"


class CityList(ListView):
    model = City

    template_name = "backend/city/list.html"


class CityNew(CreateView):
    model = City

    template_name = "backend/city/create.html"

    fields = "__all__"

    success_url = "/backend/city"


class CityUpdate(UpdateView):
    model = City

    template_name = "backend/city/update.html"

    fields = "__all__"

    success_url = "/backend/city"


class CityDelete(DeleteView):
    model = City

    template_name = "backend/city/delete.html"

    success_url = "/backend/city"


def student_chart(request):
    student = MarkList.objects.all()
    pass_count = student.filter(mark__gte=40).count()
    fail_count = student.filter(mark__lt=40).count()
    student_count=Student.objects.all().count()

    context = {
        'pass_count': pass_count,
        'fail_count': fail_count,
        'student_count': student_count,
    }

    return render(request, "backend/charts/chartjs.html", context)

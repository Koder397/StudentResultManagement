from django.shortcuts import render
from django.db.models import Q, Sum, Count
from django.contrib import messages
from backend.models import Student, MarkList


def login(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        dob = request.POST.get('dob')

        if not roll_no or not dob:
            messages.error(request, 'Roll number and date of birth are required.')
            return render(request, "frontend/search.html")

        student = Student.objects.filter(Q(roll_no=roll_no) & Q(dob=dob)).first()

        context = {
            "student": student,
            "mark_lists": MarkList.objects.filter(student=student).all(),
            "grand_total": MarkList.objects.filter(student=student).aggregate(grand_total=Sum('mark')).get(
                'grand_total')
        }

        if student:
            return render(request, "frontend/result.html", context)
        else:
            messages.error(request, 'Enter Valid Details')
            return render(request, "frontend/search.html")

    return render(request, "frontend/search.html")




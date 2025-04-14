from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from .models import Appointment, Therapist


@login_required  # فقط کاربران وارد‌شده می‌توانند به این ویو دسترسی داشته باشند
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user  # کاربر فعلی را به نوبت اختصاص می‌دهیم
            appointment.save()
            return redirect('appointments')  # به صفحه نوبت‌ها هدایت می‌شود
    else:
        form = AppointmentForm()

    # لیست درمانگران را برای انتخاب کاربر نمایش می‌دهیم
    therapists = Therapist.objects.all()
    return render(request, 'book_appointment.html', {'form': form, 'therapists': therapists})


@login_required  # فقط کاربران وارد‌شده می‌توانند به این ویو دسترسی داشته باشند
def view_appointments(request):
    # فقط نوبت‌های کاربر فعلی را نمایش می‌دهیم
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'appointments.html', {'appointments': appointments})

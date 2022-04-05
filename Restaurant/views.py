from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import About,Special_Dishes,Category,Food_Menu,Reservation_Date,Reservation_Time,Reservation_Count,Reservation_Table_Number,Reservation_Received,Service,Popular_Dishes,Event,Event_Bottom,Testimonial,ContactUs,Contact,Profile
<<<<<<< HEAD
from django.db import IntegrityError
from .forms import ContactUsForm,ReservationForm
from django.contrib import messages
=======

>>>>>>> 2a9f08caae49ee08a09ed70e8efb936b5683a185

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home(request):
    about = About.objects.latest('updated')
    special_Dishes = Special_Dishes.objects.all()
    category = Category.objects.filter()
    food_menu = Food_Menu.objects.all()
    reservation_date = Reservation_Date.objects.all()
    reservation_time = Reservation_Time.objects.all()
    reservation_count = Reservation_Count.objects.all()
    reservation_table_number = Reservation_Table_Number.objects.all()
    service = Service.objects.all()
    popular_dishes = Popular_Dishes.objects.all()
    event = Event.objects.all()
    event_bottom = Event_Bottom.objects.latest('updated')
    testimonial = Testimonial.objects.all()
    contact = Contact.objects.latest('updated')
    profile = Profile.objects.all()

    context = {
        'about':about,
        'special_Dishes':special_Dishes,
        'category':category,
        'food_menu':food_menu,
        'reservation_date':reservation_date,
        'reservation_time':reservation_time,
        'reservation_count':reservation_count,
        'reservation_table_number':reservation_table_number,
        'service':service,
        'popular_dishes':popular_dishes,
        'event':event,
        'event_bottom':event_bottom,
        'testimonial':testimonial,
        'contact':contact,
<<<<<<< HEAD
        'form1':ReservationForm,
        'form2':ContactUsForm,
=======
>>>>>>> 2a9f08caae49ee08a09ed70e8efb936b5683a185
        'profile':profile
    }

    if request.method == "POST":
        if request.POST.get('name'):
            reservation = Reservation_Received()
            reservation.name = request.POST.get('name')
            reservation.date = request.POST.get('date')
            reservation.time = request.POST.get('time')
            reservation.count = request.POST.get('count')
            reservation.table_number = request.POST.get('table_number')
            reservation.save()
<<<<<<< HEAD
            return JsonResponse({'msg1':'Success'})
=======
>>>>>>> 2a9f08caae49ee08a09ed70e8efb936b5683a185

        elif request.POST.get('name2'):
            contactus = ContactUs()
            contactus.name2 = request.POST.get('name2')
            contactus.subject = request.POST.get('subject')
            contactus.email = request.POST.get('email')
            contactus.message = request.POST.get('message')
            contactus.save()
<<<<<<< HEAD
            return JsonResponse({'msg2':'Success'})
    else:
        return render(request, 'home.html',context)
=======
            return JsonResponse({'msg':'Success'})
            
    return render(request,'home.html',context)

>>>>>>> 2a9f08caae49ee08a09ed70e8efb936b5683a185

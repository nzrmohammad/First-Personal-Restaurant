from django.shortcuts import render
from django.http import JsonResponse
from .models import About,Special_Dishes,Category,Food_Menu,Reservation_Date,Reservation_Time,Reservation_Count,Reservation_Table_Number,Reservation_Received,Service,Popular_Dishes,Event,Event_Bottom,Testimonial,ContactUs,Contact,Profile
from .forms import ContactUsForm,ReservationForm

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
    # reservation_table_number = Reservation_Table_Number.objects.filter(id=1)
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
        'form':ContactUsForm,
        'form2':ReservationForm,
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
            
            return render(request,'home.html',JsonResponse({'msg':'Success'}))

        if request.POST.get('name2'):
            contactus = ContactUs()
            contactus.name = request.POST.get('name2')
            contactus.subject = request.POST.get('subject')
            contactus.email = request.POST.get('email')
            contactus.message = request.POST.get('message')
            contactus.save()
            return JsonResponse({'msg':'Success'})
        return render(request,'home.html')
    else:
        return render(request, 'home.html',context)



    # if request.method == "POST" and 'send-message1' in request.POST:
    #     reservation = Reservation_Received(request.POST)
    #     name = request.POST.get('Name')
    #     date = request.POST.get('Date')
    #     time = request.POST.get('Time')
    #     count = request.POST.get('Count')
    #     table_number = request.POST.get('Table_Number')
    #     reservation.name = name
    #     reservation.date = date
    #     reservation.time = time
    #     reservation.count = count
    #     reservation.table_number = table_number
    #     reservation.save()

    # if request.method == "POST":
    #     reservation = Reservation_Received()
    #     name = request.POST.get('Name')
    #     date = request.POST.get('Date')
    #     time = request.POST.get('Time')
    #     count = request.POST.get('Count')
    #     table_number = request.POST.get('Table_Number')
    #     reservation.name = name
    #     reservation.date = date
    #     reservation.time = time
    #     reservation.count = count
    #     reservation.table_number = table_number
    #     reservation.save()

    # if request.method == "POST" and 'send-message2' in request.POST:
    #     contactus = ContactUs(request.POST)
    #     name = request.POST.get('name')
    #     subject = request.POST.get('subject')
    #     email = request.POST.get('email')
    #     comment = request.POST.get('comment')
    #     contactus.name = name
    #     contactus.subject = subject
    #     contactus.email = email
    #     contactus.message = comment
    #     contactus.save()

    # if is_ajax(request=request):
    #     form = ContactUsForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return JsonResponse({'msg':'Success'})
    #     else:
    #         return JsonResponse({'msg':'Error'})

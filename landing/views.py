from django.shortcuts import render, HttpResponse
from .forms import AppointmentForm
from .models import Visit, appointment
from datetime import date, datetime

# Exceptions
from django import forms
from django.contrib import messages # success message

# Geo location
from django.contrib.gis.geoip2 import GeoIP2

# Send message by Gmail
from django.core.mail import send_mail
from django.conf import settings

# Filters and pagination
from .filters import appointmentFilter
from django.core.paginator import Paginator

# Chart
from django.db.models import Count
from datetime import date, datetime

import numpy as np 

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip 

def APPOINTMENT(request):
    # SAVE BASIC DATA
    ip_address_v = get_client_ip(request)
    visit_day_v = datetime.now()

    g = GeoIP2()

    try:
        location_v = g.city(ip_address_v)
        location_country_v = location_v["country_name"]
        location_city_v = location_v["city"]
    except:
        location_country_v = 'Colombia'
        location_city_v = 'San German'

    if request.user_agent.is_mobile:
        device_type_v = "Mobile"
    if request.user_agent.is_tablet:
        device_type_v = "Tablet"
    if request.user_agent.is_pc:
        device_type_v = "PC"
    
    browser_type_v = request.user_agent.browser.family
    browser_version_v = request.user_agent.browser.version_string
    os_type_v = request.user_agent.os.family
    os_version_v = request.user_agent.os.version_string

    data = Visit(ip_address_V=ip_address_v, visit_day=visit_day_v, location_country=location_country_v, location_city=location_city_v, device_type=device_type_v, browser_type=browser_type_v, browser_version=browser_version_v, os_type=os_type_v, os_version=os_version_v)
    data.save()

    if request.method == "POST":

        name = request.POST['first_name']
        email = request.POST['email']
        date = request.POST['date']
        hour = request.POST['hour']

        form = AppointmentForm(request.POST) # NEW
        
        if form.is_valid():

           # process form data
            obj = appointment() #gets new object
            obj.first_name = form.cleaned_data['first_name']
            obj.email = form.cleaned_data['email']
            obj.date = form.cleaned_data['date']
            obj.hour = form.cleaned_data['hour']
            obj.all_is_accurate = form.cleaned_data['all_is_accurate']

            #agenda_data = appointment.objects.all() # GET ALL THE DATABASE
            filter_1 = appointment.objects.all().filter(date="23 de febrero").filter(hour="9-10")
            filter_2 = appointment.objects.all().filter(date="23 de febrero").filter(hour="10-11")
            filter_3 = appointment.objects.all().filter(date="23 de febrero").filter(hour="11-12")
            filter_4 = appointment.objects.all().filter(date="23 de febrero").filter(hour="12-13")
            filter_5 = appointment.objects.all().filter(date="23 de febrero").filter(hour="14-15")
            filter_6 = appointment.objects.all().filter(date="23 de febrero").filter(hour="15-16")
            filter_7 = appointment.objects.all().filter(date="23 de febrero").filter(hour="16-17")
            filter_8 = appointment.objects.all().filter(date="23 de febrero").filter(hour="17-18")
            filter_9 = appointment.objects.all().filter(date="23 de febrero").filter(hour="18-19")

            filter1_1 = appointment.objects.all().filter(date="24 de febrero").filter(hour="9-10")
            filter1_2 = appointment.objects.all().filter(date="24 de febrero").filter(hour="10-11")
            filter1_3 = appointment.objects.all().filter(date="24 de febrero").filter(hour="11-12")
            filter1_4 = appointment.objects.all().filter(date="24 de febrero").filter(hour="12-13")
            filter1_5 = appointment.objects.all().filter(date="24 de febrero").filter(hour="14-15")
            filter1_6 = appointment.objects.all().filter(date="24 de febrero").filter(hour="15-16")
            filter1_7 = appointment.objects.all().filter(date="24 de febrero").filter(hour="16-17")
            filter1_8 = appointment.objects.all().filter(date="24 de febrero").filter(hour="17-18")
            filter1_9 = appointment.objects.all().filter(date="24 de febrero").filter(hour="18-19")

            count_1 = filter_1.count()
            count_2 = filter_2.count()
            count_3 = filter_3.count()
            count_4 = filter_4.count()
            count_5 = filter_5.count()
            count_6 = filter_6.count()
            count_7 = filter_7.count()
            count_8 = filter_8.count()
            count_9 = filter_9.count()

            count1_1 = filter1_1.count()
            count1_2 = filter1_2.count()
            count1_3 = filter1_3.count()
            count1_4 = filter1_4.count()
            count1_5 = filter1_5.count()
            count1_6 = filter1_6.count()
            count1_7 = filter1_7.count()
            count1_8 = filter1_8.count()
            count1_9 = filter1_9.count()

            #PR = [count_1, count_2] # person restrictions 
            #test = appointment.objects.values('date', 'hour').filter(hour="9-10").annotate(the_count=Count('hour'))
            #test2 = appointment.objects.values('date', 'hour').annotate(type_count=Count("hour")).filter(type_count__gt=2).order_by("-type_count")
            #test3 = list(test2)
            #test4 = list(test2[0].values())
            #test5 = [test2[element] for element in test2]
            
            test = appointment.objects.values('date', 'hour').order_by('hour').annotate(count=Count('hour'))
            print(test)

            #for i in range(0, len(test3)):
            #    print(list(test2[i].values()))

            # if (obj.hour == "3" and obj.am_pm == "AM") or (obj.hour == "4" and obj.am_pm == "AM"):
            #     messages.error(request, "{} este horario no está permitido.".format(obj.first_name))
            #     #return render(request, 'agenda.html', {'form': form})

            # else:
            if (obj.date == "23 de febrero" and obj.hour == "9-10" and count_1 == 3) or (obj.date == "23 de febrero" and obj.hour == "10-11" and count_2 == 3) or (obj.date == "23 de febrero" and obj.hour == "11-12" and count_3 == 3) or (obj.date == "23 de febrero" and obj.hour == "12-13" and count_4 == 3) or (obj.date == "23 de febrero" and obj.hour == "14-15" and count_5 == 3) or (obj.date == "23 de febrero" and obj.hour == "15-16" and count_6 == 3) or (obj.date == "23 de febrero" and obj.hour == "16-17" and count_7 == 3) or (obj.date == "23 de febrero" and obj.hour == "17-18" and count_8 == 3) or (obj.date == "23 de febrero" and obj.hour == "18-19" and count_9 == 3) or (obj.date == "24 de febrero" and obj.hour == "9-10" and count1_1 == 3) or (obj.date == "24 de febrero" and obj.hour == "10-11" and count1_2 == 3) or (obj.date == "24 de febrero" and obj.hour == "11-12" and count1_3 == 3) or (obj.date == "24 de febrero" and obj.hour == "12-13" and count1_4 == 3) or (obj.date == "24 de febrero" and obj.hour == "14-15" and count1_5 == 3) or (obj.date == "24 de febrero" and obj.hour == "15-16" and count1_6 == 3) or (obj.date == "24 de febrero" and obj.hour == "16-17" and count1_7 == 3) or (obj.date == "24 de febrero" and obj.hour == "17-18" and count1_8 == 3) or (obj.date == "24 de febrero" and obj.hour == "18-19" and count1_9 == 3):
                messages.error(request, "{} para el {} a las {} el cupo ya está asignado, por favor seleccione otra hora".format(obj.first_name, obj.date, obj.hour))

            else:
                obj.save()
                messages.success(request, "{} Te has inscrito satisfactoriamente".format(obj.first_name))

                #send_mail(
                #'Inscripción satisfactoria', # subject
                #'Sr/Sra ' + name + ' su inscripción para el día ' + date + ' a las ' + hour + ' se logró de forma satisfactoria ' + '. Si por algún motivo no puede presentarse o quiere cancelar la asignación por favor enviar un correo a este Email indicando eso, muchas gracias y te esperamos en este grandioso evento.', # name, email and message
                #settings.EMAIL_HOST_USER,
                #['wimateusav@unal.edu.co'] # To Email
                #)
                
                return render(request, 'agenda.html', {'form': form})

    else:
        form = AppointmentForm()
    return render(request, 'agenda.html', {'form': form})


def summary(request):

    users = appointment.objects.all()

    myFilter = appointmentFilter(request.GET, queryset=users)
    #users = myFilter.qs

    paginated_filtered_users = Paginator(myFilter.qs, 10)
    page_number = request.GET.get('page')
    users_page_obj = paginated_filtered_users.get_page(page_number)

    return render(request, 'summary.html', {
        'users': users,
        'myFilter': myFilter,
        'users_page_obj': users_page_obj,
    })


def chart(request):

    visits = Visit.objects.all()
    
    visitors = Visit.objects.values('ip_address_V').annotate(num_ip=Count('ip_address_V', distinct=True))
    visitors_num = visitors.count()
    lab_visitors = [ip['ip_address_V'] for ip in visitors]

    date_visit = Visit.objects.values('visit_day').annotate(num_dv=Count('visit_day', distinct=True))
    date_visit_num = date_visit.count()
    lab_date_visit = [dv['visit_day'].strftime("%d-%B") for dv in date_visit]#strftime("%Y-%m-%d") for dv in date_visit]    
    lab_date_visit_set = set(lab_date_visit)
    unique_lab_date_visit = (list(lab_date_visit_set))
    unique_lab_date_visit.sort()
    co_date_visit = [lab_date_visit.count(u_lab_da) for u_lab_da in unique_lab_date_visit]
    
    countries = Visit.objects.values('location_country').annotate(num_country=Count('location_country', distinct=True))
    countries_num = countries.count()
    lab_countries = [co['location_country'] for co in countries]

    cities = Visit.objects.values('location_city').annotate(num_city=Count('location_city'))
    cities_num = cities.count()
    lab_cities = [ci['location_city'] for ci in cities]
    co_cities = [Visit.objects.filter(location_city=lab_ci).count() for lab_ci in lab_cities]
    
    device = Visit.objects.values('device_type').annotate(num_device=Count('device_type'))
    device_num = device.count()
    lab_device = [de['device_type'] for de in device]
    co_device = [Visit.objects.filter(device_type=lab_de).count() for lab_de in lab_device]
    co_device1 = np.divide(co_device, sum(co_device))*100
    co_device1 = np.round_(co_device1, decimals = 2)
    co_device1 = co_device1.tolist()
    #co_device1 = ["{:.2%}".format(x) for x in co_device1]
    
    ostype = Visit.objects.values('os_type').annotate(num_ostype=Count('os_type'))
    ostype_num = ostype.count()
    lab_ostype = [os['os_type'] for os in ostype]
    co_ostype = [Visit.objects.filter(os_type=lab_os).count() for lab_os in lab_ostype]

    return render(request, 'chart.html', {
        'visits': visits,
        'date_visit': date_visit,
        'date_visit_num': date_visit_num,
        'lab_date_visit': lab_date_visit,
        'unique_lab_date_visit': unique_lab_date_visit,
        'co_date_visit': co_date_visit,
        'lab_visitors': lab_visitors,
        'visitors_num': visitors_num,
        'countries_num': countries_num,
        'lab_countries': lab_countries,
        'cities': cities,
        'cities_num': cities_num,
        'lab_cities': lab_cities,
        'co_cities': co_cities,
        'device': device,
        'device_num': device_num,
        'lab_device': lab_device,
        'co_device': co_device,
        'co_device1': co_device1,
        'ostype': ostype,
        'ostype_num': ostype_num,
        'lab_ostype': lab_ostype,
        'co_ostype': co_ostype,
    })

def calendar(request):

    vip = appointment.objects.all()

    filter_1 = appointment.objects.all().filter(date="23 de febrero").filter(hour="9-10")
    filter_2 = appointment.objects.all().filter(date="23 de febrero").filter(hour="10-11")
    filter_3 = appointment.objects.all().filter(date="23 de febrero").filter(hour="11-12")
    filter_4 = appointment.objects.all().filter(date="23 de febrero").filter(hour="12-13")
    filter_5 = appointment.objects.all().filter(date="23 de febrero").filter(hour="14-15")
    filter_6 = appointment.objects.all().filter(date="23 de febrero").filter(hour="15-16")
    filter_7 = appointment.objects.all().filter(date="23 de febrero").filter(hour="16-17")
    filter_8 = appointment.objects.all().filter(date="23 de febrero").filter(hour="17-18")
    filter_9 = appointment.objects.all().filter(date="23 de febrero").filter(hour="18-19")

    filter1_1 = appointment.objects.all().filter(date="24 de febrero").filter(hour="9-10")
    filter1_2 = appointment.objects.all().filter(date="24 de febrero").filter(hour="10-11")
    filter1_3 = appointment.objects.all().filter(date="24 de febrero").filter(hour="11-12")
    filter1_4 = appointment.objects.all().filter(date="24 de febrero").filter(hour="12-13")
    filter1_5 = appointment.objects.all().filter(date="24 de febrero").filter(hour="14-15")
    filter1_6 = appointment.objects.all().filter(date="24 de febrero").filter(hour="15-16")
    filter1_7 = appointment.objects.all().filter(date="24 de febrero").filter(hour="16-17")
    filter1_8 = appointment.objects.all().filter(date="24 de febrero").filter(hour="17-18")
    filter1_9 = appointment.objects.all().filter(date="24 de febrero").filter(hour="18-19")

    count_1 = filter_1.count()
    count_2 = filter_2.count()
    count_3 = filter_3.count()
    count_4 = filter_4.count()
    count_5 = filter_5.count()
    count_6 = filter_6.count()
    count_7 = filter_7.count()
    count_8 = filter_8.count()
    count_9 = filter_9.count()

    count1_1 = filter1_1.count()
    count1_2 = filter1_2.count()
    count1_3 = filter1_3.count()
    count1_4 = filter1_4.count()
    count1_5 = filter1_5.count()
    count1_6 = filter1_6.count()
    count1_7 = filter1_7.count()
    count1_8 = filter1_8.count()
    count1_9 = filter1_9.count()

    return render(request, 'calendar.html', {
        'vip': vip,
        'count_1':count_1,
        'count_2':count_2,
        'count_3':count_3,
        'count_4':count_4,
        'count_5':count_5,
        'count_6':count_6,
        'count_7':count_7,
        'count_8':count_8,
        'count_9':count_9,
        'count1_1': count1_1,
        'count1_2': count1_2,
        'count1_3': count1_3,
        'count1_4': count1_4,
        'count1_5': count1_5,
        'count1_6': count1_6,
        'count1_7': count1_7,
        'count1_8': count1_8,
        'count1_9': count1_9,     
    })
from django.http import JsonResponse
from django.shortcuts import render
from .models import City, Hotel

"""
    View for the form page
    :param request: HttpRequest object
    :return: HttpResponse object

    This view is used to render the form page. It also handles the form submission.
    If a city name is submitted, it searches for the city in the database and retrieves the hotels associated with that city.
"""

def city_hotel_view(request):
    cities = City.objects.all()
    selected_city = None
    hotels = None

    if request.method == 'POST':
        city_name_search = request.POST.get('city')
        if city_name_search:
            try:
                selected_city = City.objects.get(name__icontains=city_name_search)
                hotels = Hotel.objects.filter(city_code=selected_city)
            except City.DoesNotExist:
                selected_city = None
                hotels = None

    return render(request, 'form.html', {
        'cities': cities,
        'selected_city': selected_city,
        'hotels': hotels
    })

def autocomplete_city(request):
    if 'term' in request.GET:
        qs = City.objects.filter(name__icontains=request.GET.get('term'))
        cities = list(qs.values('name'))
        return JsonResponse(cities, safe=False)
    return JsonResponse([], safe=False)
from .models import Cars
from django.db.models import Q
from django.shortcuts import render


def filter(request):
    qs = Cars.objects.all()
    make_filter = request.GET.get('make')
    model_filter = request.GET.get('model')
    year_filter = request.GET.get('year')
    color_filter = request.GET.get('color')

    if (make_filter != '' and make_filter is not None):
        qs = qs.filter(Q(make__icontains=make_filter))

    if (model_filter != '' and model_filter is not None):
        qs = qs.filter(Q(model__icontains=model_filter))

    if (year_filter != '' and year_filter is not None):
        qs = qs.filter(Q(year__icontains=year_filter) )

    if (color_filter != '' and color_filter is not None):
        qs = qs.filter(Q(color__icontains=color_filter))

    return qs

def FilterList(request):
    qs = filter(request)
    context = {
        'queryset': qs
    }
    return render(request, 'filter.html', context)

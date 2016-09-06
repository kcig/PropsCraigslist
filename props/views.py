from django.shortcuts import render
from django.utils import timezone
from .models import Props

# Create your views here.
def props_list(request):
    props = Props.objects.order_by('-published_date')
    return render(request, 'props/props_list.html', {'props':props})

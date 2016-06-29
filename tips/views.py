from django.shortcuts import render

from .models import Tip

# Create your views here.
def tip_list(request):
	tips = Tip.objects.all()
	return render(request, 'tips/tip_list.html', {'tips': tips})
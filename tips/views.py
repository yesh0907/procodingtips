from django.shortcuts import get_object_or_404, render

from .models import Series, Tip

# Create your views here.
def all_series_list(request):
	series = Series.objects.all()
	return render(request, 'tips/series_list.html', { 'series': series })

def all_tip_list(request):
	tips = Tip.objects.all().order_by('-pub_date')
	series_length = len(tips)
	return render(request, 'tips/tip_list.html', { 'tips': tips, 'series_length': series_length })

def all_tips_in_series(request, pk):
	series = get_object_or_404(Series, pk=pk)
	tip = Tip.objects.filter(series=series).order_by('-pub_date')
	series_length = len(tip)
	context = {
		'series': series,
		'tip': tip,
		'series_length': series_length
	}
	return render(request, 'tips/all_tips_in_series.html', context)
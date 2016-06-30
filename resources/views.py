from django.shortcuts import get_object_or_404, render

from .models import Group, Resource

# Create your views here.
def all_resources(request):
	groups = Group.objects.all()
	resources = Resource.objects.order_by('group')
	print resources
	return render(request, 'resources/all_resources.html', { 'groups': groups, 'resources': resources })
from django.shortcuts import get_object_or_404, render

from .models import Group, Resource

# Create your views here.
def all_resources_and_groups(request):
	groups = Group.objects.all()
	resources = []
	if len(groups) > 0:
		hasGroups = True
		for group in groups:
			currentGroup = Group.objects.get(name=group)
			resources.append(Resource.objects.filter(group=group))
	else:
		hasGroups = False
	context = {
		'groups': groups, 
		'resources': resources,
		'hasGroups': hasGroups,
	}
	return render(request, 'resources/all_resources_and_groups.html', context)

def all_groups(request):
	groups = Group.objects.all()
	return render(request, 'resources/all_groups.html', { 'groups': groups })

def group_detail(request, group_id):
	group = get_object_or_404(Group, pk=group_id)
	resources = Resource.objects.filter(group=group)
	return render(request, 'resources/group_detail.html', { 'group': group, 'resources': resources })
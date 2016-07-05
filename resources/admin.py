from django.contrib import admin

from .models import Resource, Group

# Register your models here.
class ResourceInline(admin.StackedInline):
	model = Resource

class GroupAdmin(admin.ModelAdmin):
	inlines = [ResourceInline,]

admin.site.register(Group, GroupAdmin)
admin.site.register(Resource)
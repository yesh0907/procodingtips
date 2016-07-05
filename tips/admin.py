from django.contrib import admin

from .models import Series, Tip

# Register your models here.
class TipInline(admin.StackedInline):
	model = Tip

class SeriesAdmin(admin.ModelAdmin):
	inlines = [TipInline,]

admin.site.register(Series, SeriesAdmin)
admin.site.register(Tip)
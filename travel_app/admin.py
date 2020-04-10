from django.contrib import admin
from .models import Travel, TravelMembers
# Register your models here.

class TravelAdmin(admin.ModelAdmin):
    list_display = ('name','start_date', 'end_date',)
    list_filter = ('start_date', 'end_date', 'country')
    fieldsets = (
        (None, {'fields': ('name', 'description')}),
        ('Dates', {'fields': ('start_date', 'end_date',)}),
        ('Details', {'fields': ('country', 'city', 'creator_id', 'members', 'image',)}),
    )
    search_fields = ('name',)
    ordering = ('id', 'start_date',)

class TravelMembersAdmin(admin.ModelAdmin):
    list_display = ('travel_id', 'user_id',)

admin.site.register(Travel, TravelAdmin)
admin.site.register(TravelMembers, TravelMembersAdmin)
from django.contrib import admin
from .models import Article, AcceptChrist, PrayerRequest,Event
# Register your models here.


admin.site.site_header='TREE OF LIFE ADMINISTRATION PAGE'
admin.site.site_title ='TREE OF LIFE FELLOWSHIP'
admin.site.index_title='WELCOME TO TREE OF LIFE ADMIN PORTAL'

class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'active', 'total_views', ]
    # prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        ('Write A new Article', {
            'fields': ('title',)
        }),
        ('Content', {

            'fields': ('image', 'story', 'tags', 'source',),
        }),
        ('Advance Options', {
            'classes': ('collapse',),
            'fields': ('added_by','active','slug'),
        })
    )

admin.site.register(Article, ArticleAdmin)

class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ['request_type', 'name', 'email', 'phone', 'message']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['date_add']


admin.site.register(PrayerRequest, PrayerRequestAdmin)


class AcceptChristAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'note']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['date_add']


admin.site.register(AcceptChrist, AcceptChristAdmin)


class EventsAdmin(admin.ModelAdmin):
    list_display = ['event_type','name','time','date','active']
    list_editable = ['active']
    list_filter = ['date_updated','date_add','active']
    search_fields = ['name']

admin.site.register(Event,EventsAdmin)
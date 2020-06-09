from django.contrib import admin
import csv
from django.http import  HttpResponse
from .models import (ChurchGroup, Question, Student, StudentAnswer, Subject,
                     TakenQuiz, User,Quiz)

admin.site.register(Student)
admin.site.register(Question)
admin.site.register(StudentAnswer)
admin.site.register(Subject)

admin.site.register(TakenQuiz)
admin.site.register(ChurchGroup)




#can_participate false
def unmakeActive(modeladmin,request,queryset):
    queryset.update(can_participate=False)
    # for user in queryset:
    #     user.can_participate =False
    #     user.save()

unmakeActive.short_description='make all participate inactive'



def makeActive(modeladmin,request,queryset):
    queryset.update(can_participate=True)
    # for user in queryset:
    #     user.can_participate =False
    #     user.save()

makeActive.short_description='make all participate active'



# export model to csv
def export_people(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tof_users.csv"'
    writer = csv.writer(response)
    writer.writerow(['username', 'First Name', 'Last Name', 'Is Member', 'Is leader','group'])
    user = queryset.values_list('username', 'first_name', 'last_name', 'is_member', 'is_leader','group')
    for users in user:
        writer.writerow(users)
    return response
export_people.short_description = 'Export to csv'

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','can_participate',
                    'last_name', 'is_active','is_leader','is_member','group',]
    actions =[unmakeActive,makeActive,export_people,]
    list_filter = ['is_leader', 'is_member','can_participate','group','date_updated',]
    search_fields = ['first_name', 'username']
    list_editable = ['can_participate','group',]
    list_per_page =20


admin.site.register(User, UserAdmin)

# not woking find a way to fix it

class QuizeAdmin(admin.ModelAdmin):
    list_display = ['owner','name','every_one','active',]
    search_fields =['name',]
    list_editable = ['active']
    list_filter=['active','date_updated',]

admin.site.register(Quiz,QuizeAdmin)
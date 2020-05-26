from django.urls import path

from . import views

# views.sitemap(request, sitemaps, section=None, template_name='sitemap.xml', content_type='application/xml')

app_name = 'tof_app'
urlpatterns = [
    # path('',Templateview.as_view()),
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    path('blog/', views.BlogView.as_view(), name='blog'),
    path('createarticle/',views.CreateArtcle.as_view(),name='createarticle'),
    path('update/<int:pk>/',views.UpdateArticleView.as_view(),name='updatearticle'),
    path('tof/<slug:added_by>/<str:slug>/<int:pk>/',views.articleDetail, name='blogdetail'),
    path('tag_article/<str:tags>/',views.tag_articles,name='tag_articles'),
    # small pages:
    path('become-member/', views.BecomeMemberView.as_view(), name='become-member'),
    path('accept-christ/', views.AcceptChristView.as_view(), name='accept-christ'),
    path('prayer-request/', views.PrayerRequesttView.as_view(),
         name='prayer-request'),
    path('donate/', views.calender.as_view(), name='donate'),

    # registration

    path('register-member/',views.MemberSignUpView.as_view(),name='register-member'),
    path('register-leader/',views.LeaderSignUpView.as_view(),name='register-leader'),

    # Events
    path('events/',views.CreateEventView.as_view(),name='create-event'),
    path('update-event/<int:pk>/',views.UpdateEventView.as_view(),name='update-event'),

]

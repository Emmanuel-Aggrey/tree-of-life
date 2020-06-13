from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, FormView, ListView, TemplateView,
                                  UpdateView)

from classroom.decorators import teacher_required
from classroom.forms import StudentSignUpForm, TeacherSignUpForm, User

from .forms import ArticleForm, EventForm
from .models import AcceptChrist, Article, Event, PrayerRequest

# Create your views here.


class HomeView(ListView):
    # queryset = Event.objects.filter(active=True)
    context_object_name = 'objects'
    template_name = 'main-page/index.html'

    def get_queryset(self):
        queryset = Event.objects.filter(active=True)

        queryset = {
            'anoycements': queryset.filter(event_type='anoycement'),
            'events': queryset.filter(event_type='event'),

        }

        return queryset


class AboutView(TemplateView):
    template_name = 'main-page/about.html'


class ContactView(TemplateView):
    template_name = 'main-page/contact.html'
    # return render(request, '')


class BlogView(ListView):
    queryset = Article.objects.filter(active=True)
    # context_object_name = ''
    template_name = 'main-page/blog.html'
    paginate_by = 12

    # return render(request, 'main-page/blog.html')


# def blogSingle(request):
#     return render(request, 'main-page/blog-single.html')

@method_decorator([login_required, teacher_required], name='dispatch')
class CreateArtcle(SuccessMessageMixin, CreateView):
    model = Article
    template_name = 'article/create_article.html'
    form_class = ArticleForm
    # success_url = reverse_lazy('tof_app:createarticle')
    # success_message = "ARTICLE SAVED"

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        
        # form.instance.user_phone = self.request.user.userphone.phonenumber

        return super().form_valid(form)


@method_decorator([login_required, teacher_required], name='dispatch')
class UpdateArticleView(UpdateView):

    model = Article
    template_name = 'article/create_article.html'
    form_class = ArticleForm


def articleDetail(request, added_by, slug, pk):
    article = get_object_or_404(Article, slug=slug, pk=pk)
    total_views = int(article.total_views)
    total_views += 1

    Article.objects.filter(pk=pk).update(total_views=total_views)

    context = {

        'articles': article,

    }
    return render(request, 'main-page/blog-detail.html', context)


# filters all posts with the specific tag
def tag_articles(request, tags):
    # posts = Post.objects.filter(tagged_items=tags)
    # url_tag = str(request.GET('tags')).lower
    # tag = get_object_or_404(Tag, tags)  # get the tags from the url
    article = Article.objects.filter(tags__name__in=[tags]).distinct()
    context = {
        'article': article,
        'article_tag': tags,
    }
    return render(request, 'main-page/tag_articles.html', context)

    # small pages


class BecomeMemberView(TemplateView):
    template_name = 'main-page/small_sites/become_memner.html'


class AcceptChristView(SuccessMessageMixin, CreateView):
    template_name = 'main-page/small_sites/accept_christ.html'
    model = AcceptChrist
    fields = ['name', 'email', 'phone', 'note']
    success_message = "saved successfully thank you for reaching to us"

    # success_url='accept-christ'


class PrayerRequesttView(SuccessMessageMixin, CreateView):
    template_name = 'main-page/small_sites/prayer_request.html'
    model = PrayerRequest
    fields = ['request_type', 'name', 'email', 'phone', 'message']
    success_message = "saved successfully thank you for reaching to us"


class calender(TemplateView):
    template_name = 'main-page/donate.html'


class MemberSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'member_register/register_member.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Member'  # student
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tof_app:home')


class LeaderSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'member_register/register_member.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Leader'  # teacher
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('tof_app:home')


class CreateEventView(SuccessMessageMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'article/events/events-annoucement.html'
    success_url = reverse_lazy('tof_app:create-event')
    success_message = 'created with success'


class UpdateEventView(SuccessMessageMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'article/events/events-annoucement.html'
    success_message = 'updated with success'
    def get_success_url(self):
        return reverse('tof_app:update-event', kwargs={'pk': self.object.pk})

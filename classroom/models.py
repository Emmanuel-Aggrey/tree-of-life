from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

from tof_app.models import BaseModel


class ChurchGroup(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    

class User(AbstractUser,BaseModel):
    is_member = models.BooleanField('is member',default=False)
    is_leader = models.BooleanField('is leader',default=False)
    can_participate = models.BooleanField(default=True)
    
    group = models.ForeignKey(ChurchGroup,on_delete=models.DO_NOTHING,blank=True, null=True)

    


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff',editable=False)

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)

class Quiz(BaseModel):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    # subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes',verbose_name='topic',blank=True, null=True)
    # every_one = models.BooleanField('participant',default=True)
    active = models.BooleanField(default=True,help_text='make this quize public now')

    def __str__(self):
        return self.name


class Question(BaseModel):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    #available topic(s)*
    # interests = models.ManyToManyField(Subject, related_name='interested_students',help_text='available topics',verbose_name='available topic(s)',blank=True)

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name ='Member'
        verbose_name_plural ='Members'


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes',verbose_name='Member')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers',verbose_name='Member')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name ='Member Answer'
        verbose_name_plural='Members Answers'

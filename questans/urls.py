from django.urls import path
from django.conf.urls import url
from .views import home_view, new_question,question_detail,tagged,new_answer,upvote,questions,answer_edit,add_answer

urlpatterns = [
    path('',home_view,name='home'),
    path('question/new/',new_question,name='new_question'),
    path('topic/<slug:slug>/', tagged, name="tagged"),
    path('add-answer/<int:pk>',new_answer,name='add-answer'),
    url(r'^add-answer/$',add_answer),
    path('question/<int:pk>',question_detail,name='question-details'),
    path('upvote/<int:pk>',upvote,name='upvote'),
    path('questions/',questions,name='questions'),
    path('answer-edit/<qk>/<ak>',answer_edit,name='answer-edit')
    # path('index/page/<int:pg>',),
]
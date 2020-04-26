from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Questions, Answers, UpVote
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from .forms import QuestionForm,AnswerForm

# Create your views here.
def home_view(request):
    ques_obj = Questions.objects.all().order_by("-created_on")
    # common_topics = Questions.topics.all()
    page_number = request.GET.get('page', 1)
    paginate_result = do_paginate(ques_obj, page_number)
    ques_obj = paginate_result[0]
    paginator = paginate_result[1]
    base_url = '/index/page?'
    context = {
        'ques_obj':ques_obj,
        'paginator' : paginator, 
        'base_url':base_url,
    }
    return render(request,'home.html',context)

def do_paginate(data_list, page_number):
    ret_data_list = data_list
    result_per_page = 10
    paginator = Paginator(data_list, result_per_page)
    try:
        ret_data_list = paginator.page(page_number)
    except EmptyPage:
        ret_data_list = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        ret_data_list = paginator.page(1)
    return [ret_data_list, paginator]

def questions(request):
    ques_obj = Questions.objects.all().order_by("-created_on")
    common_topics = Questions.topics.all()
    page_number = request.GET.get('page', 1)
    paginate_result = do_paginate(ques_obj, page_number)
    ques_obj = paginate_result[0]
    paginator = paginate_result[1]
    base_url = '/index/page?'
    context = {
        'ques_obj':ques_obj,
        'common_topics':common_topics,
        'paginator' : paginator, 
        'base_url':base_url,
    }
    return render(request,'questions.html',context)

def is_upvoted(user,pk):
    answer = get_object_or_404(Answers,pk=pk)
    if user.upvotes.filter(answer=answer).count()==1 and answer.upvotes.filter(user=user).count()==1:
        return True
    else:
        return False
        
def upvote(request,pk):
    if (is_upvoted(request.user,pk)):
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    else:
        answer = get_object_or_404(Answers,pk=pk)
        up = UpVote.objects.create(user=request.user,answer=answer)
        up.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def question_detail(request, pk):
    question = get_object_or_404(Questions, pk=pk)
    form = AnswerForm()
    context = {
        'question':question,
        'form':form
    }
    return render(request, 'question_details.html', context)

def new_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            form.save_m2m()
            return redirect('question-details', pk=question.pk)
    else:
        form = QuestionForm()
    return render(request, 'question_edit.html', {'form': form})


def new_answer(request,pk):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            question = get_object_or_404(Questions,pk=pk)
            answer.question = question
            answer.save()
            
            return redirect('question-details',pk=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'add-answer.html',{'form':form})


def answer_edit(request,qk,ak):
    answer = get_object_or_404(Answers, pk=ak)
    question = get_object_or_404(Questions,pk=qk)
    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            return redirect('question_detail',pk=question.pk)
    else:
        form = AnswerForm(instance=answer)
    return render(request, 'answer_edit.html', {'form': form})
def add_answer(request):
    if request.method == "POST":
        text = request.POST['text']
        print(text)
        pk=request.POST['pk']
        question = get_object_or_404(Questions,pk=pk)
        answer = Answers.objects.create(user=request.user,question=question,answer_text=text)   
        answer.save()
        return redirect('question-details',pk=question.pk)
    else:
        form = AnswerForm()
    return render(request, 'add-answer.html',{'form':form})


def tagged(request, slug):
    topics = get_object_or_404(Tag, slug=slug)
    common_topics = Questions.topics.most_common()[:4]
    ques_obj = Questions.objects.filter(topics=topics)
    context = {
        'topics':topics,
        'common_topics':common_topics,
        'ques_obj':ques_obj,
    }
    return render(request, 'home.html', context)
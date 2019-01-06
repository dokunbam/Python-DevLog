from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from . models import Board, Topic, Post
from django.contrib.auth.decorators import login_required
from django.db.models import Count

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') -1)
    return render(request, 'topics.html', {'board': board, 'topics': topics})

@login_required
def new_topics(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    user = request.user
    if request.method == 'POST':
        form = forms.NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            form.save()
            Post.objects.create(
            message=form.cleaned_data.get('message'),
            topic=topic,
            created_by=request.user  
        )
            return redirect('board_topics', board.id)
    else: 
        form = forms.NewTopicForm()
    return render(request, 'new_topics.html', {'board': board, 'form': form})


def topic_posts(request, board_id, topic_id):
    topic = get_object_or_404(Topic, board_id=board_id, id=topic_id)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})

@login_required
def reply_topic(request, board_id, topic_id):
    topic = get_object_or_404(Topic, board_id=board_id, id=topic_id)
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', board_id, topic_id)
    else:
        form = forms.PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})

from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Article, Comment
from django.contrib import auth

def index(request):
	latestArticlesList = Article.objects.order_by('-pubDate')[:5]
	return render(request, 'articles/list.html', {'latestArticlesList':latestArticlesList})

def detail(request, articleId):
	try:
		a = Article.objects.get(id = articleId)
	except:
		raise Http404("Такой статьи нет :(")

	latestCommentsList = a.comment_set.order_by('-id')[:10]

	return render(request, 'articles/detail.html', {'article': a, 'latestCommentsList': latestCommentsList})	


def leaveComment(request, articleId):
	try:
		a = Article.objects.get(id = articleId)
	except:
		raise Http404("Такой статьи нет :(")

	author_name = auth.get_user(request)

	a.comment_set.create(authorName = author_name, commentText = request.POST['text'])

	return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))

def reply_to_comment():
	pass

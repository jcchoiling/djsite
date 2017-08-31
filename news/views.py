from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

# Create your views here.

def article_list(request):
	articles = Article.objects.all()
	output = ','.join([str(article) for article in articles])
	return HttpResponse(output)


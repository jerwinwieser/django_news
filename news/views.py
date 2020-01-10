from django.shortcuts import render, redirect


from bs4 import BeautifulSoup as bs
from datetime import timedelta, timezone, datetime
import requests

from .models import Article


def home(request):
	return render(request, 'news/home.html', {'title': 'News Page', 'articles': Article.objects.all()})


def scrape(request):
	Article.objects.all().delete()

	html = requests.get("https://www.bbc.com/news//world").content
	bsobj = bs(html, "html.parser")

	headers = bsobj.find_all("a", {"class": "gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor"})
	introductions = bsobj.find_all("p", {"class": "gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary gs-u-display-none gs-u-display-block@l"})



	for i in range(0, len(headers)):
		title = headers[i].text
		href = headers[i].get("href")

		if href[:5] != "https":
			href = "https://www.bbc.com/" + href

		try: 
			introduction = introductions[i].text
		except IndexError:
			introduction = ''




		new_article = Article()
		new_article.title = title
		new_article.href = href
		new_article.introduction = introduction
		new_article.publisher = "BBC News"
		new_article.save()

	return redirect('/')

def get_blog_queryset(query=None):
	queryest = []
	queries = query.split(" ")
	for q in queries:
		posts = BlogPost.objects.filter(
			Q(title__iconstrains=q) |
			Q(body__iconstrains=q)
			).distinct()

		
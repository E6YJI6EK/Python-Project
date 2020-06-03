from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model):
	articleTitle = models.CharField('article name', max_length = 200)
	articleText = models.TextField('text')
	pubDate = models.DateTimeField('publication date')

	def __str__(self):
		return self.articleTitle

	def wasPublishedRecently(self):
		return self.pubDate	>= (timezone.now() - datetime.timedelta(days = 7))	

	class Meta:
		verbose_name = "Статья"
		verbose_name_plural = "Статьи"	

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	authorName = models.CharField('people name', max_length = 50)
	commentText = models.CharField('comment text', max_length = 200)

	def __str__(self):
		return self.authorName

	class Meta:
		verbose_name = "Коммент"
		verbose_name_plural = "Коммы"		
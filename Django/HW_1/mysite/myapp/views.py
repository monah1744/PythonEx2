from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("Hello dodik")


def main_article(request):
    return HttpResponse('There will be a list with articles')


def uniq_article(request):
    return HttpResponse('This is uniq answer for uniq value')


def article(request, article_id, name=''):
    return HttpResponse(
        "This is an article #{}. {}".format(article_id, "Name of this article is {}".format(
            name) if name else "This is unnamed article"))


def article_archive(request):
    return HttpResponse('This is uniq answer for article archive ...!!!')


def archive_number(request, article_number):
    return HttpResponse('This is uniq answer for article number #{} archive ...!!!'.format(article_number))


def main_users(request):
    return HttpResponse('This is uniq answer for Users :) :)')


def users_number(request, user_number):
    return HttpResponse(
        "This is an user #{}".format(user_number))

from django.shortcuts import render
from django.http import HttpResponse


class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Create your views here.


def hello(request):
    my_num = 33
    my_str = 'some string'
    my_dict = {"some_key": "some_value"}
    my_list = ['list_first_item', 'list_second_item', 'list_third_item']
    my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
    my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
    my_class = MyClass('class string')
    return render(request, 'hello.html', {
        'my_num': my_num,
        'my_str': my_str,
        'my_dict': my_dict,
        'my_list': my_list,
        'my_set': my_set,
        'my_tuple': my_tuple,
        'my_class': my_class,
    })


def user(request):
    # return HttpResponse('Hello user')
    return render(request, 'user.html')


def index1(request):
    # return HttpResponse('Hello user')
    return render(request, 'index1.html', {'number_list': number_list})


def index2(request):
    # return HttpResponse('Hello user')
    return render(request, 'index2.html', {'number_list': number_list})

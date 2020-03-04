from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm
from django.views.generic import FormView, View, ListView
from my_app.models import Article
# Create your views here.


def login_view(request):
    print(request.POST)
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
    return render(request, "login.html", {'form': form})


class LoginView(FormView):
    # http_method_names = ['post']
    form_class = LoginForm
    success_url = '/'
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return redirect('/')


class LogoutView(View):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        logout(self.request)
        return redirect('/')
        # return super().post(request, *args, **kwargs)


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(is_deleted=False)
    paginate_by = 1

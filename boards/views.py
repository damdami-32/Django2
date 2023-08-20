from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from .models import Board
from .forms import BoardForm
from accounts.models import User
from django.core.paginator import Paginator
# from .models import Tag
from tag.models import Tag
import pickle
from django.http.request import HttpRequest

def board_main(request):
    redirect('/')

def board_write(request):
    if not request.session.get('user'):
        return redirect('/accounts/login')

    if request.method =='POST': 
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)
            tags = form.cleaned_data['tags'].split(',')

            board=Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            for tag in tags:
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/boards/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form':form})
    
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board_detail.html',{'board':board})
    
def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    paginator = Paginator(all_boards, 5)
    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards':boards})

def test(request):
    return render(request, 'test.html')

def apart(request):
    return render(request, 'apart.html')

def predict(request:HttpRequest, *args, **kwargs):
    first = request.GET.get("first")
    second = request.GET.get("second")
    third = request.GET.get("third")
    fourth = request.GET.get("fourth")
    


    return render(request, 'predict.html')
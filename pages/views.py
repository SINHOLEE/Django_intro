from django.shortcuts import render
import random
# Create your views here.


def index(request): # 첫번째 인자는 반드시 request가 온다. => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'index.html')  # render의 첫번째 인자도 반드시 request
    #아직 index.html을 만들진 않았지만, template_name -> 유저에게 보여줄 정보를 명시적으로 작성한다.


def introduce(request):
    return render(request, 'introduce.html')


# Template Variable example
def dinner(request):
    menu = ['강남 더막창스', '노랑통닭', '양자강']

    # 최대한 다른함수나 메소드, 어트리뷰트등 겹치지 않게 한다.
    pick = random.choice(menu)
    context = {
        'pick' : pick,
    }
    # Django template로 context 전달
    return render(request, 'dinner.html', context)
    
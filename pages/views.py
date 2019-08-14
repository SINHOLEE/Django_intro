from django.shortcuts import render
import random
from datetime import datetime
# Create your views here.


def index(request): # 첫번째 인자는 반드시 request가 온다. => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'index.html')  # render의 첫번째 인자도 반드시 request
    #아직 index.html을 만들진 않았지만, template_name -> 유저에게 보여줄 정보를 명시적으로 작성한다.


def introduce(request):
    return render(request, 'introduce.html')


# Template Variable example
def dinner(request, name):
    menu = ['강남 더막창스', '노랑통닭', '양자강']

    # 최대한 다른함수나 메소드, 어트리뷰트등 겹치지 않게 한다.
    pick = random.choice(menu)
    context = {
        'pick' : pick,
        'name' : name,
    }
    # Django template로 context 전달
    return render(request, 'dinner.html', context)
    

def image(request):
    nums = random.randint(1,1010)
    url = f'https://picsum.photos/id/{nums}/500/500'
    context = {
        'url' :url,
    }
    return render(request, 'image.html', context)


def greeting(request, name):

    context = {
        'name' : name,
    }
    return render(request,'greeting.html', context)


def times(request, num1, num2):
    
    result = num1 * num2
  
    def comma(num):
        num = str(num)
        num = num[::-1]
        s = ''
        for i in range(len(num)):
            if i == 0:
                s += num[i]

            else:
                if i % 3 == 0:
                    s = s + ',' + num[i] 
                else:
                    s += num[i]
        
        s = s[::-1]
        return s
    context = {
        'num1' : comma(num1),
        'num2' : comma(num2),
        'result' : comma(result),
    }

    return render(request, 'times.html', context)


def template_language(request):
    menu = ['짜장면', '탕수육', '양장피', '짬뽕']
    my_santence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango', 'bob']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menu' : menu,
        'my_santence' : my_santence,
        'messages' : messages,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list,
    }
    return render(request, 'template_language.html', context)
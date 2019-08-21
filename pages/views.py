from django.shortcuts import render
import random
from datetime import datetime
# Create your views here.


def index(request): # 첫번째 인자는 반드시 request가 온다. => 사용자가 보내는 요청에 대한 정보
    # 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'pages/index.html')  # render의 첫번째 인자도 반드시 request
    #아직 index.html을 만들진 않았지만, template_name -> 유저에게 보여줄 정보를 명시적으로 작성한다.


def introduce(request):
    return render(request, 'pages/introduce.html')


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
    return render(request, 'pages/dinner.html', context)
    

def image(request):
    nums = random.randint(1,1010)
    url = f'https://picsum.photos/id/{nums}/500/500'
    context = {
        'url' :url,
    }
    return render(request, 'pages/image.html', context)


def greeting(request, name):

    context = {
        'name' : name,
    }
    return render(request,'pages/greeting.html', context)


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

    return render(request, 'pages/times.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '양장피', '짬뽕']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango', 'bob']
    datetimenow = datetime.now()
    empty_list = []

    context = {
        'menus' : menus,
        'my_sentence' : my_sentence,
        'messages' : messages,
        'datetimenow' : datetimenow,
        'empty_list' : empty_list,
    }
    return render(request, 'pages/template_language.html', context)

def isitbirthday(request):
    my_birthday = datetime(1992, 8, 16)
    context = {
        'my_birthday' : my_birthday,
    }
    return render(request, 'pages/isitbirthday.html', context)

def lotto(request):
    real_lotto = [21, 25, 30, 32, 40, 42]
    lotto = sorted(random.sample(range(1,46), 6))  # 희원이가 랜덤으로 뽑은 로또
    count = 0
    
    context = {
        'real_lotto' : real_lotto,
        'lotto' : lotto,
    }

    return render(request, 'pages/lotto.html', context)

def search(request):
    return render(request, 'pages/search.html')

def result(request):
    category = request.GET.get('category')
    query = request.GET.get('query')
    context = {
        'query' : query,
        'category' : category,
    }
    return render(request, 'pages/result.html', context)

def lotto_pick(request):
    
    return render(request, 'pages/lotto_pick.html')

def lotto_result(request):
    nums = list(map(int, request.GET.get('pick').split()))
    sorted_nums = sorted(nums)
    real_lotto = [21, 25, 30, 32, 40, 42]
    count = 0
    for i in range(6):
        if sorted_nums[i] == real_lotto[i]:
            count += 1
    context = {
        'nums' : nums,
        'real_lotto' : real_lotto,
        'count' : count,
    }
    return render(request, 'pages/lotto_result.html',context)

def api_lotto(request):
    return render(request, 'pages/api_lotto.html')


def api_lotto_result(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=870#'
    aa = request.GET
    print(aa)
    return render(request, 'pages/api_lotto_result.html')

def static_example(request):
    return render(request, 'pages/static_example.html')

def num_push(request):
        return render(request, 'pages/num_push.html')
    
def num_pull(request):
    num = request.GET.get('num')
    context = {
        'num': num,
        }
    return render(request, 'pages/num_pull.html', context)	
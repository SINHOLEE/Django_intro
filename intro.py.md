# 1. settings.py 설정

```python
# setting.py안에 설정 바꾸기

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

```

application 만들기

```bash
(venv)
$ python manage.py startapp pages
# 어플리케이션 폴더가 생성된다.
```

# 2. application 설명

1. admin.py 

   어플리케이션마다 모델들이 많은데, 이를 관리하고 등록하는 장소( 커스터마이징 장소)

2. apps.py
   앱에대한 정보가 입력되는 장소(건드릴 일은 없다.)

3. models.py

   여기서 저장한 모델을 admin에서 관리한다.

   각 정보들을 저장하고 조작한다?

4. test.py

   수정할 일 없다.

5. views.py(!!!!중요!!!!)

   MTV 모델을 따른다 할 때, v가 view이다. 

   어떤 작업을 하는 공간.

   함수로 정의된다. 

### application 3대장

1. models.py
2. views.py
3. <project name>/urls.py

   # 3. 어플리케이션 등록

프로젝트 생성 -> 어플리케이션 생성 -> 프로젝트에 어플리케이션을 등록해야한다.

<프로젝트 폴더>/settings.py

   ```python
# 기본
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# 등록 / 등록할 때 순서가 있다. 
INSTALLED_APPS = [
    # Local apps / 우리가 생성한 앱들, 항상 맨 위에 둔다.
    'pages',
    
    # Third party apps / ex) bootstrap을 사용할 때 등록해야하는데 중간에 둔다.
    
	# Django apps / 기본 앱스고, 항상 밑에 둔다.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
   ```



   # 4. index page 생성

home 화면 만들기



1. open -> pages/views.py

```python
from django.shortcuts import render

# Create your views here.


def index(request): # 첫번째 인자는 반드시 request가 온다. => 사용자가 보내는 요청에 대한 정보
	# 요청이 들어오면 'index.html'을 보여준다.
    return render(request, 'index.html')  # render의 첫번째 인자도 반드시 request
    #아직 index.html을 만들진 않았지만, template_name -> 유저에게 보여줄 정보를 명시적으로 작성한다.


```

2. <project name>/urls.py / url과 view 함수를 맵핑한다.

```python

# 경로를 잘 보라.
# pages/views.py/index()
# pages라는 어플리케이션안에 있는 view.py라는 파일을 임포트 해서, view.index 함수를 접근하도록 하자.
from pages import views

urlpatterns = [
    # path('사용자가 접속하는 경로')
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
```

3. index.html 만들기

pages/templates/index.html만든다.

이렇게 구조화 한다면 views.py가 알아서 html파일을 찾는다.

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>index</title>
</head>
<body>
  <h1>Hi Django?</h1>
</body>
</html>
```



# 5. dinner recommend code 작성

1. views.py안에 작성

```python
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
    
```

- context 안에 dictionary형태로 정보를 저장하면 html 에 {{ <변수이름> }}을 삽입하면 변수를 호출할 수 있게 된다.

1. urls.py에 등록
2. html파일 생성 



# 6. variable routing

1. urls.py

```python
urlpatterns = [
    path('greeting/<str:name>/', views.greeting),
]
```

2. views.py

```python
def greeting(request, name):

    context = {
        'name' : name,
    }
    return render(request,'greeting_iu.html', context)

```

3. greeting.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>greeting!</title>
</head>
<body>
  <h1>안녕 ! {{ name }}</h1>
  
</body>
</html>
```



# 7. Django template language

1. template_language.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>template language</title>
 

</head>
<body>
  <h1>Template language</h1>
  <hr>

  {% comment %} for문 {% endcomment %}
  <h2>1. 반복문</h2>
  {% comment %} {% <로직를 작성하는 공간> %}  {% endcomment %}
  {% for menu in menus %} 
  <p>{{ menu }}</p>
  {% comment %} 함수의 구분을 인덴트로 하지 못하므로 다음과 같이 끝내야 한다. {% endcomment %}
  {% endfor %} 
  <hr/>

  {% for menu in menus%}
  {% comment %} 
  {{ forloop }}은 DTL for 문에서 자동으로 생기는 객체.
  {{ forloop.counter }}는 인덱스가 1부터 시작하는 숫자를 생성해 준다. 
  {% endcomment %}
  <p>{{ forloop.counter }}.  {{menu}}</p>
  {% endfor %}
  
  <hr/>
  
  {% for user in empty_list %}
  <p>{{ user }}</p>
  {% empty %}
  <p>현재 가입한 유저가 없습니다.</p>
  {% endfor %}
  <hr/>

  <h2>2. 조건문</h2>
  {% if '짜장' in menus%}
  <p> 어머님은 짜장면이 싫다고 하셨어!</p>
  {% else %}
  <p>야이야이야아~</p>
  {% endif %}
  <hr>

  {% for menu in menus%}
  <p> <strong>{{ forloop.counter }}번째 도는 중</strong>
  </p>
  {% if forloop.first %}
  <p>{{ menu }} + 고춧가루</p>
  {% else %}
  <p>{{ menu }}</p>
  {% endif %}
  {% endfor %}
  <hr>
  <h2>3. length filter 활용</h2>
  {% for message in messages %}
    {% if message|length > 5 %}
      <p>{{ message }}, 글자가 너무 길어요.</p>
      {% else %}
      <p>{{ message }}, 글자길이는 {{ message|length }}</p>
    {% endif %}
  {% endfor %}
  <hr align='left' width=300px;>

  <h2>4. lorem ipsum</h2>
  {% comment %}
   시각적 연출, 표준 채우기 텍스트 아무 글이나 가져와서 내 페이지상에서 어떤식으로 표현되는지 확인하는 것 
  {% endcomment %}
  {% lorem 1 p random %}
  {% comment %} 
  밑에처럼 쓸 경우 불러오지 않는 이유 : {{}}는 사용자가 지정한 변수를 가져오기 때문에
  {% endcomment %}
  {{ lorem }}
  <hr>

  <h2>5. 글자 수 제한(truncate) : 잘라내기</h2>
  {% comment %} 
  F12에서 주석을 보이게하고 싶거나, 태그 뒤에 주석을 달고 싶을때는
  html문법의 주석인 <!-- 내용 -->으로 작성해야 한다. 
  {% endcomment %}
  <p>{{ my_sentence|truncatewords:3 }}</p><!-- 단어 단위로 제한 -->
  <p>{{ my_sentence|truncatechars:3 }}</p><!-- 문자 단위로 제한(3번째 문자는 포함하지 않는다.) -->
  <p>{{ my_sentence|truncatechars:10 }}</p><!-- 문자 단위로 제한(10번째 문자는 포함하지 않는다.) -->

  <hr>
  <h2>6. 글자 관련 필터</h2>
  <p>{{ 'abc'|length }}</p>
  <p>{{ 'ABC'|lower }}</p>
  <p>{{ my_sentence|title }}</p>
  <p>{{ 'abc def. asdasgl'|capfirst }}</p>
  <p>{{ menus|random }}</p>
  <hr>

  <h2>7. 연산</h2>
  <p>
  {{ 4|add:6 }}
  </p>
  <hr>

  {% comment %} 
  {% now "DATE_FORMAT" %} 가 내장되어 있다.
   {% endcomment %}
  <h2>8. 날짜표현(중요)</h2>
  <p>{{ datetimenow }}</p>
  {% now "DATE_FORMAT" %}
  {% now "DATETIME_FORMAT" %}
  
  <p>{% now "SHORT_DATE_FORMAT" %}</p>
  <p>{% now "SHORT_DATETIME_FORMAT" %}</p>
  {% now "m-d H:i" %}
  {% now "Y" as current_year %}
  <p>Copyright {{ current_year }}</p>
  <hr>
  {% comment %}
  위에 NOW를 쓴 상태는 지금의 날짜나 시간밖에 컨트롤하지 못하므로,
  python database에 저장된 시간관련 로직을 다음과 같이 꺼낼 수 있다.
   {% endcomment %}
  {{datetimenow|date:"DATE_FORMAT"}}
  <hr>

  <h2>9. 기타</h2>
  {% comment %} a tag 대용으로 사용 가능 {% endcomment %}
  <p>{{"google.com"|urlize}}</p>
  <hr>

</body>
</html>
```

#  8. Final



마지막 작업을 끝맞추고 다음과 같은 과정을 거친다.

```bash
$ pip freeze -> requirements
```

이렇게 하면 `requirements.txt`파일이 생긴다.



새로시작할때  `requirements.txt` 를 통해서 인스톨 한다.

```bash
pip install -r requirements.txt
```

- -r은 재귀적으로 순회하면서 깔라는 뜻


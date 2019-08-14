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


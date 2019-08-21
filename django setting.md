# django setting

## 1. 가상환경 설정

- 모든 프로젝트 하나하나당 파이썬 환경 하나씩 설정할것입니다. 왜? 
- 프로젝트마다 사용하는 라이브러리가 다르고, 버전이 다를 수 있다. 그리고 호환성, 의존성에 대한 이슈가 발생할 수 있다.

1. 파이썬 버전을 확인한다.

```python
$ python -V
Python 3.5.3
$ venv
(3.7.4)

# 반드시 3.7.x버전으로 맞춰야 한다.
$ python -V
Python 3.7.4
(3.7.4)


```



2. 새롭게 만들 가상환경 폴더를 생성한다.

```python
#가상환경 생성
# $ python -m venv venv<가상환경 설치경로>

$ python -m venv venv
```

3. 새로운 가상환경 적용시키기

```python
$ source venv/Scripts/activate
```

4.  버전 재확인

```python
$ python -V
Python 3.7.4
(venv) # 가상환경 적용시 git bash에서 해당 환경 이름이 표시된다.
```

5. 설치된 모듈 확인

```python
$ pip list
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
You are using pip version 19.0.3, however version 19.2.2 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.
(venv) # pip upgrade 요구함

# 업그레이드 다시 하고 pip list 재확인
$ python -m pip install --upgrade pip

$ pip list
Package    Version
---------- -------
pip        19.2.2
setuptools 40.8.0
```







## vs code 세팅

1. django and python extentions down
2. ctrl + shift + p -> python select interpriter -> 방금 생성한 가상환경을 선택('')
3.  .vscode/settings.json 파일이 생성되며 터미널에서 자동으로 가상환경이 적용된다면 정상작동



## git ignore setting

- 가상환경 폴더나, .vscode 같은 설정을 위한 정보는 깃에 올릴 필요 없다.

1. gitignore.io를 인터넷 창에 검색
2. python, django, windows, visualstudiocode를 설정에 붙여넣기
3. girignore 파일 생성 후 안에 복사했던 text붙인다.

```python
touch .gitignore
```

4. 기본설정에는 !으로 표시된 파일들은 깃에 올린다고 설정되어있다. 이를 지우면 모두 올리지 않게 된다.

```python
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json

```





## VS code Django 환경세팅

1. .vscode/settings.json 에서 환경세팅을 설정한다.

```json
    // 파이썬 가상환경 자동 설정(컨트롤 백팁 눌렀을 때) 
    "python.pythonPath": "venv\\Scripts\\python.exe",

```



2. Django extentions -> details에서 복사한다.

```json
// Django에서 사용되는 파일 타입에 대한 정의
    "files.associations": {
        "**/templates/*.html": "django-html",
        "**/templates/*": "django-txt",
        "**/requirements{/**,*}.{txt,in}": "pip-requirements",
        
    },

    // django html 에서도 html emmet(바로생성)을 적용 
    "emmet.includeLanguages": {"django-html": "html"},

```

3. tab-size 설정

```json
// tab- size 2칸고정
    "[django-html]": {
        "editor.tabSize": 2,
    },

```



## Start Django Project

```bash
(venv)
$ pip install Django
```

- Django 를 설치한 순간부터 django-admin 이라는 commend를 사용할 수 있게 된다.

- 이 commend를 통해 django project 에 여러가지 명령을 할 수 있다.

  

1. 장고 프로젝트 생성하기

```bash
(venv)
# startproject 뒤에는 프로젝트를 관리할 폴더명을 쓰고 띄어쓰기 . 으로 마무리 한다.
$ django-admin startproject django_intro .
```

- 현재 디렉토리에서 django_intro라는 이름으로 프로젝트를 시작하겠다라는 뜻.

- 프로젝트 명으로 된 폴더와 manage.py폴더가 생성되면 ok

- Django project naming

  - `-`캐릭터는 사용될 수 없다.
  - python 과 django 에서 이미 사용되는 이름은 사용하지 않는다.(django라는 이름은 그 자체와 충돌이 발생하며, text 또한 자체적으로 사용되는 모듈 이름이다.)

  

2. 장고 프로젝트 시작하기

```bash
(venv)
$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 14, 2019 - 10:51:46
Django version 2.2.4, using settings 'django_intro.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

```bash
# 이 url 클릭하면 정상적으로 작동이 됨.
http://127.0.0.1:8000/

# 127.0.0.1 => 내 컴퓨터 로컬 호스트
```

- ctrl + c -> quit 
- 기본적으로 localhost:8000 에서 실행된다.
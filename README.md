210706 블로그 프로젝트 완성 (템플릿 상속 & url 관리)
-------------------------------------------
1. 글 저장 시간을 대한민국 시간으로 변경
2. nav 태그 내 home 버튼 클릭 시 home 화면으로 이동 
3. nav 태그 내 portfolio 버튼 클릭 시 portfolio 화면으로 이동
4. 회원가입 및 로그인 페이지 생성
5. pagination 활용하여 페이지 이동 생성
6. Form 이용하여 형식 고정
   #### pagination 관련 bootstrap 사용 애매해서 아직 못했음 . . 
   #### github merge 못했음 . . master to main 하기
   #### SECRET_KEY 알림 메일 왔음

***
### 참고 


- 시간을 대한민국 시간으로 변경하려고 할 때

   setting.py에 들어가서
```python
TIME_ZONE = 'Asia/Seoul'
.
.
USE_TZ = False
```   

- `form` 태그의 속성
1. `action` : 데이터를 보낼 url을 지정
2. `method` : 데이터의 전송방식을 지정, GET방식과 POST 방식으로 나뉨
   
- `get` 방식과 `post` 방식의 차이점
```
get, post : http 메서드로 클라이언트에서 서버로 무언가를 요청할 때 사용

* get - 데이터 조회(read) 
* post - 데이터 생성(create)

get : 클라이언트에서 서버로 어떠한 리소스로부터 정보를 요청하기 위해 사용되는 메서드 (ex : 게시판의 게시물을 조회)
방식 : url 끝에 '?' 붙이고 그다음 변수명1=값1&변수명2=값2... 형식으로 이어 붙이기
특징 :
- 데이터를 요청할 때만 사용됨
- 중요한 정보를 다루면 안됨 (파라미터에 다 노출되기 때문)

post : 클라이언트에서 서버로 리소스를 생성하거나 업데이터하기 위해 데이터를 보낼 때 사용되는 메서드 (ex : 게시판에 게시글을 작성하는 작업 등)
방식 : 전송할 데이터를 http 메시지 body 부분에 담아서 서버로 보냄
특징 :
- 데이터 길이에 제한이 없음
- 브라우저 히스토리에 남지 않음
```

- `{% csrf_token %}`
~~~
csrf : 사이트 간 요청 위조. 웹사이트 취약점 공격의 하나로, 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위를 특정 웹사이트에 요청하게 하는 공격
이를 해결하기 위해선 changepassword 페이지의 form 전달값에 특정한 값을 추가하면 됨
~~~

- `{% if user.is_authenticated %}` : 로그인이 되어있는지 물어보는 코드
- `{% else %}`, `{% endif %}`, `{% for --- %}`, `{% endfor %}` : if, for문이라고 생각하면 될듯
- Paginator : 페이지 관리

- model을 기반으로 한 form : 장고에서 기본으로 제공
- meta class : 파이썬에서는 클래스도 객체임. 클래스라는 객체를 만들기 위한 클래스가 메타 클래스임. 클래스가 동작하는 방식을 정의함

- faker : 가짜 데이터
- faker에 한글 데이터 삽입 가능 `myfake = Faker('ko_KR')`
- os 모듈 : 운영체제 API에 대한 인터페이스를 제공
-`os.path.join` : 운영체제에 독립적으로 경로를 연결해줌
- sqlite : 파이썬 안에 내장된 SQL 데이터베이스 

1. pagination 관련 bootstrap 연결 방법
    1. posts.paginator.num_pages 
    2. html 에서 반복문 사용하기
    3. num_page보다 작으면 계속 li 페이지 만들어주기
2. media 부분에서 사진을 넣으면 화면 출력 안됨
    1. view, edit 버튼 클릭하기
    2. aws
3. github merge 관련 - master to main
    1. main이 예전 master
4. faker 사용법 & seed 이해
    1. faker - 가짜 데이터
    2. 몇개를 쓸 건지 → seed → db안에 넣을 때 사용하는 명령어
    3. faker를 이용해서 db 안에 랜덤값을 넣을 수 있음
    4.

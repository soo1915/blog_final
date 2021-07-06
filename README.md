### 210706 블로그 프로젝트 완성 (템플릿 상속 & url 관리)
1. 글 저장 시간을 대한민국 시간으로 변경
2. nav 태그 내 home 버튼 클릭 시 home 화면으로 이동 
3. nav 태그 내 portfolio 버튼 클릭 시 portfolio 화면으로 이동

### 참고 

시간을 대한민국 시간으로 변경하려고 할 때

setting.py에 들어가서
```python
TIME_ZONE = 'Asia/Seoul'
.
.
USE_TZ = False
```



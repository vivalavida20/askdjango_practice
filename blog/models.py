from django.db import models
import re
from django.forms import ValidationError

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid ㅇLngLat Type')

class Post(models.Model):
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name="제목", help_text="포스팅 제목을 입력해주세요 최대 100자") #verbose_name을 설정하면 브라우저별 언어 설정에 대응하기가 어렵다는 단점
    content = models.TextField()
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text="경도,위도 포맷으로 입력",
                              validators=[lnglat_validator],)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # auto_now_add - 최초 생성 시 값이 생성 auto_now - 조회할 때마다 값이 갱신
    # 일단 커밋용

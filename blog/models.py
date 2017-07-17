from django.db import models
import re
#from django.conf.auth import User
from django.conf import settings
from django.forms import ValidationError

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    # author = models.CharField(max_length=20)
    title = models.CharField(max_length=100, verbose_name="제목", help_text="포스팅 제목을 입력해주세요 최대 100자") #verbose_name을 설정하면 브라우저별 언어 설정에 대응하기가 어렵다는 단점
    content = models.TextField()
    tags = models.CharField(max_length=100, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text="경도,위도 포맷으로 입력",
                              validators=[lnglat_validator],)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_set = models.ManyToManyField('Tag')
    # auto_now_add - 최초 생성 시 값이 생성 auto_now - 조회할 때마다 값이 갱신

    class Meta:
        # 기본 정렬 순서를 제공
        ordering = ['-id'] #id필드 역순

    # 쿼리셋으로 불러올 때 보이게 하고 싶은 내용 정의
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True) #unique 값을 설정하면 같은 태그를 또 등록하지 않을 수 있도록 설정 가능 

    def __str__(self):
        return self.name

from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import JokeImg, JokeDuanzi
from .mypagenumberpagination import MyPageNumberPagination
from .serializer import JokeImgSerializer, JokeDuanziSerializer


# Create your views here.


@csrf_exempt
@api_view(['GET', 'POST'])
def joke_img(request):
    if request.method == 'GET':
        queryset = JokeImg.objects.all()
        page = MyPageNumberPagination()
        instance = page.paginate_queryset(request=request, queryset=queryset)
        if instance is not None:
            serializer = JokeImgSerializer(instance, many=True)
            return page.get_paginated_response(serializer.data)
        serializer = JokeImgSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        ser = JokeImgSerializer(data=request.data)
        if ser.is_valid():
            # ser.save()
            return Response(data=ser.data, status=status.HTTP_201_CREATED)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)


class JokeDetail(APIView):
    def get_object(self, id):
        try:
            joke = JokeImg.objects.get(id=id)
            return joke
        except JokeImg.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        joke = self.get_object(id=kwargs.get('id'))
        ser = JokeImgSerializer(instance=joke)
        return Response(data=ser.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        joke = self.get_object(id=kwargs.get('id'))
        ser = JokeImgSerializer(data=request.data, instance=joke)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data, status=status.HTTP_200_OK)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        print('我走了patch方法')
        joke = self.get_object(id=kwargs.get('id'))
        ser = JokeImgSerializer(data=request.data, instance=joke, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(data='修改成功', status=status.HTTP_200_OK)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        joke = self.get_object(id=kwargs.get('id'))
        joke.delete()
        joke.save()
        return Response(data='删除成功', status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['get', 'post'])
def joke_font(request):
    if request.method == 'GET':
        queryset = JokeDuanzi.objects.filter(is_hot=0).all()
        page = MyPageNumberPagination()
        instance = page.paginate_queryset(request=request, queryset=queryset)
        if instance is not None:
            serializer = JokeDuanziSerializer(instance, many=True)
            return page.get_paginated_response(serializer.data)
        serializer = JokeDuanziSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        ser = JokeDuanziSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data, status=status.HTTP_200_OK)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)


class JokeFont(RetrieveUpdateDestroyAPIView):
    queryset = JokeDuanzi.objects.filter(is_hot=0).all()
    serializer_class = JokeDuanziSerializer


class JokeHotFont(
                    ListModelMixin,
                    CreateModelMixin,
                    GenericAPIView
            ):
    queryset = JokeDuanzi.objects.filter(is_hot=1).all()
    serializer_class = JokeDuanziSerializer

    def get(self,request,*args,**kwargs):
        print('adfasfd')
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class JokeHotFontDetail(RetrieveUpdateDestroyAPIView):
    queryset = JokeDuanzi.objects.filter(is_hot=1).all()
    serializer_class = JokeDuanziSerializer


def plus_joke_img_zan(request,id):
    joke = JokeImg.objects.filter(id=id).first()
    joke.like_num += 1
    joke.save()
    return HttpResponse('点赞成功')

def jian_joke_img_zan(request,id):
    joke = JokeImg.objects.filter(id=id).first()
    joke.like_num -= 1
    joke.save()
    return HttpResponse('取消点赞成功')


def plus_joke_img_cai(request, id):
    joke = JokeImg.objects.filter(id=id).first()
    joke.no_like += 1
    joke.save()
    return HttpResponse('踩成功')


def jian_joke_img_cai(request, id):
    joke = JokeImg.objects.filter(id=id).first()
    joke.no_like -= 1
    joke.save()
    return HttpResponse('取消踩成功')

# -------------------------------------------------------------------------->

def plus_joke_font_zan(request,id):
    joke = JokeDuanzi.objects.filter(id=id).first()
    joke.like_num += 1
    joke.save()
    return HttpResponse('点赞成功')

def jian_joke_font_zan(request,id):
    joke = JokeDuanzi.objects.filter(id=id).first()
    joke.like_num -= 1
    joke.save()
    return HttpResponse('取消点赞成功')

def plus_joke_font_cai(request,id):
    joke = JokeDuanzi.objects.filter(id=id).first()
    joke.no_like += 1
    joke.save()
    return HttpResponse('踩成功')

def jian_joke_font_cai(request,id):
    joke = JokeDuanzi.objects.filter(id=id).first()
    joke.no_like -= 1
    joke.save()
    return HttpResponse('取消踩成功')






from django.urls import path

# from .views import JokeImgView
from .views import joke_img, JokeDetail, joke_font, JokeFont, JokeHotFont, JokeHotFontDetail, plus_joke_font_zan, \
    plus_joke_img_cai, plus_joke_img_zan, jian_joke_img_cai, jian_joke_font_zan,jian_joke_img_zan,jian_joke_font_cai

urlpatterns = [
    # path('joke_img/', JokeImgView.as_view(),name='joke_img'),
    path('joke_img/', joke_img, name='joke_img'),
    path('joke_detail/<int:id>/', JokeDetail.as_view(), name='joke_detail'),
    path('joke_font/', joke_font, name='joke_font'),
    path('joke_font/<int:pk>/', JokeFont.as_view(), name='JokeFont'),
    path('joke_hot/', JokeHotFont.as_view(), name='joke_hot'),
    path('joke_hot_detail/<int:pk>/', JokeHotFontDetail.as_view(), name='joke_detail_hot'),
    # ------------------------------------------------------------------------------
    path('img_cai/<int:id>/', plus_joke_img_cai),
    path('img_cancel_cai/<int:id>/', jian_joke_img_cai, ),
    path('img_zan/<int:id>/', plus_joke_img_zan),
    path('img_cancel_zan/<int:id>/', jian_joke_img_zan),

    path('font_zan/<int:id>/', plus_joke_font_zan),
    path('cancel_font_zan/<int:id>/', jian_joke_font_zan),
    path('font_cai/<int:id>/', plus_joke_font_zan),
    path('cancel_font_cai/<int:id>/', jian_joke_font_cai),
]

from .models import Goodmenu,Album
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from django.http import HttpResponseRedirect

from django.contrib import messages



# userlike import
from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse

# Create your views here.

class AlbumList(ListView):
    model = Album

class AlbumDetail(DetailView):
    model = Album

class GoodmenuDetail(DetailView):
    model = Goodmenu

class GoodMenuLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:    #로그인확인
            return HttpResponseForbidden()
        else:
            if 'goodmenu_id' in kwargs:
                goodmenu_id = kwargs['goodmenu_id']
                goodmenu = Goodmenu.objects.get(pk=goodmenu_id)
                user = request.user
                if user in goodmenu.like.all():
                    goodmenu.like.remove(user)
                else:
                    goodmenu.like.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class GoodMenuFavorite(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:    #로그인확인
            return HttpResponseForbidden()
        else:
            if 'goodmenu_id' in kwargs:
                goodmenu_id = kwargs['goodmenu_id']
                goodmenu = Goodmenu.objects.get(pk=goodmenu_id)
                user = request.user
                if user in goodmenu.favorite.all():
                    goodmenu.favorite.remove(user)
                else:
                    goodmenu.favorite.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class GoodMenuLikeList(ListView):
    model = Goodmenu
    template_name = 'goodmenu/goodmenu_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(GoodMenuLikeList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # 내가 좋아요한 글을 보여주
        user = self.request.user
        queryset = user.goodmenulike_post.all()
        return queryset


class GoodMenuFavoriteList(ListView):
    model = Goodmenu
    template_name = 'goodmenu/goodmenu_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(GoodMenuFavoriteList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # 내가 좋아요한 글을 보여주기
        user = self.request.user
        queryset = user.goodmenufavorite_post.all()
        return queryset
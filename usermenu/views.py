from django.shortcuts import render,redirect

from .models import UserMenu,UserAlbum,UserArea
from django.views.generic import ListView, DetailView,UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin



from django.http import HttpResponseRedirect

from django.contrib import messages


# userlike import
from django.views.generic.base import View
from django.http import HttpResponseForbidden
from urllib.parse import urlparse



class UserAlbumList(ListView):
    model = UserAlbum

 

class UserAlbumDetail(DetailView):
    model = UserAlbum

class UserMenuCreate(LoginRequiredMixin,CreateView):
    model = UserMenu
    fields = ['useralbum','userarea','userstar', 'title','smallbody','body','smallimg','detailimg']
    template_name_suffix = '_create'
    success_url = '/usermenu/'

    def form_valid(self, form):
        form.instance.userauthor = self.request.user
        return super(UserMenuCreate, self).form_valid(form)
    
    
        
       
class UserMenuUpdate(UpdateView):
    model = UserMenu
    fields = ['useralbum','userarea','userstar', 'title','smallbody','body','smallimg','detailimg']
    template_name_suffix = '_update'
    success_url = '/usermenu/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.userauthor != request.user:
            messages.warning(request, '수정할 권한이 없습니다.')
            return HttpResponseRedirect('/usermenu/')
        else:
            return super(UserMenuUpdate, self).dispatch(request, *args, **kwargs)


class UserMenuDelete(DeleteView):
    model = UserMenu
    template_name_suffix = '_delete'
    success_url = '/usermenu/'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        if object.userauthor != request.user:
            messages.warning(request, '삭제할 권한이 없습니다.')
            return HttpResponseRedirect('/usermenu/')
        else:
            return super(UserMenuDelete, self).dispatch(request, *args, **kwargs)



class UserMenuDetail(DetailView):
    model = UserMenu
    template_name_suffix = '_detail'


class UserMenuLike(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:    #로그인확인
            return HttpResponseForbidden()
        else:
            if 'usermenu_id' in kwargs:
                usermenu_id = kwargs['usermenu_id']
                usermenu = UserMenu.objects.get(pk=usermenu_id)
                user = request.user
                if user in usermenu.like.all():
                    usermenu.like.remove(user)
                else:
                    usermenu.like.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class UserMenuFavorite(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:    #로그인확인
            return HttpResponseForbidden()
        else:
            if 'usermenu_id' in kwargs:
                usermenu_id = kwargs['usermenu_id']
                usermenu = UserMenu.objects.get(pk=usermenu_id)
                user = request.user
                if user in usermenu.favorite.all():
                    usermenu.favorite.remove(user)
                else:
                    usermenu.favorite.add(user)
            referer_url = request.META.get('HTTP_REFERER')
            path = urlparse(referer_url).path
            return HttpResponseRedirect(path)


class UserMenuLikeList(ListView):
    model = UserMenu
    template_name = 'usermenu/usermenu_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(UserMenuLikeList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # 내가 좋아요한 글을 보여주
        user = self.request.user
        queryset = user.like_post.all()
        return queryset


class UserMenuFavoriteList(ListView):
    model = UserMenu
    template_name = 'usermenu/usermenu_list.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(UserMenuFavoriteList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        # 내가 좋아요한 글을 보여주기
        user = self.request.user
        queryset = user.favorite_post.all()
        return queryset

class UserMenuMyList(ListView):
    model = UserMenu
    template_name = 'usermenu/usermenu_mylist.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인확인
            messages.warning(request, '로그인을 먼저하세요')
            return HttpResponseRedirect('/')
        return super(UserMenuMyList, self).dispatch(request, *args, **kwargs)



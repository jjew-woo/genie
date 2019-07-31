from django.contrib import admin
from .models import UserAlbum, UserMenu, UserArea, UserStar

# Register your models here.
class UserMenuInline(admin.StackedInline):
    model = UserMenu
    extra = 0

class UserAlbumAdmin(admin.ModelAdmin):
    inlines = [UserMenuInline]
    list_display = ('name', 'description')

class UserAreaAdmin(admin.ModelAdmin):
    inlines = [UserMenuInline]
    list_display = ('name', 'description')

class UserStarAdmin(admin.ModelAdmin):
    inlines = [UserMenuInline]
    list_display = ('name', 'description')
    

class UserMenuAdmin(admin.ModelAdmin):
    list_display = ('useralbum', 'userauthor','userarea','title')


admin.site.register(UserAlbum, UserAlbumAdmin)
admin.site.register(UserArea, UserAreaAdmin)
admin.site.register(UserStar, UserStarAdmin)
admin.site.register(UserMenu, UserMenuAdmin)


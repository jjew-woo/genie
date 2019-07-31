from django.contrib import admin
from .models import Album, Goodmenu, GoodStar

# Register your models here.
class GoodmenuInline(admin.StackedInline):
    model = Goodmenu
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    inlines = [GoodmenuInline]
    list_display = ('name', 'description')

class GoodStarAdmin(admin.ModelAdmin):
    inlines = [GoodmenuInline]
    list_display = ('name', 'description')


class GoodmenuAdmin(admin.ModelAdmin):
    list_display = ('album', 'author','title')


admin.site.register(Album, AlbumAdmin)
admin.site.register(GoodStar, GoodStarAdmin)
admin.site.register(Goodmenu, GoodmenuAdmin)

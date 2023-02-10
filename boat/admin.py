from django.contrib import admin

from boat.models import Like, Boat


class LikesInline(admin.TabularInline):
    model = Like
    readonly_fields = ('user', 'boat',)
    fields = ('user',)
    can_delete = False
    extra = 0


@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ('owner', 'model', 'length', 'year', 'price',)

    inlines = [
        LikesInline
    ]

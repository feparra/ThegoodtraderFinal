from django.contrib import admin

from .models import Avatar, Profile, Trade,Note,Market,Tradeimagen

class TradeAdmin(admin.ModelAdmin):
    list_display=("fecha","simbolo" , "posicion" , "entrada" , "target" ,"stop")
    search_fields =("fecha","simbolo" , "posicion" , "entrada" , "target" ,"stop")
    
class NoteAdmin(admin.ModelAdmin):
    list_display=("fecha","simbolo" )
    search_fields =("fecha","simbolo")
    
class MarketAdmin(admin.ModelAdmin):
    list_display=("pais","simbolo" )
    search_fields =("pais","simbolo")

admin.site.register(Trade,TradeAdmin)
admin.site.register(Note,NoteAdmin)
admin.site.register(Market,MarketAdmin)


admin.site.register(Avatar)
admin.site.register(Profile)
admin.site.register(Tradeimagen)


from django.urls import path

from . import views #se utiliza el punto por que es la ruta relativa (donde esta la carpeta)

urlpatterns = [
    path('',views.index, name='Home'),
    path('dashboard/',views.Dashboard,name="Dashboard"),
    path('login',views.Login_request,name="Login"),
    path('register',views.Register_request,name="Register"),
    path('logout',views.Logout_request,name="Logout"),
    path('editar_perfil',views.Editar_perfil,name="Editar_perfil"),
    path('agregar_avatar',views.Agregar_avatar,name="Agregar_avatar"),
    path('profile',views.Profile,name="Profile"),
    path('about',views.About,name="About"),
    
    
    
    
    path('eliminar_trade/<trade_id>',views.eliminar_trade,name="Eliminar_trade"),
    path('editar_trade/<trade_id>',views.editar_trade,name="Editar_trade"),
    path('ver_trade/<trade_id>',views.ver_trade,name="Ver_trade"),
    
    #Nuevas URLS
    path('trades/list',views.TradesList.as_view(),name="Trades_list"),
    path('trades/<pk>',views.TradesDetail.as_view(),name="Trades_detail"),
    path('trade/nuevo',views.TradeCreate.as_view(),name="Trades_create"),
    path('trades/editar/<pk>',views.TradeUpdate.as_view(),name="Trades_update"),
    path('trades/eliminar/<pk>',views.TradeDelete.as_view(),name="Trades_delete"),
    
    
    
    
    path('notes/',views.Notes,name="Notes"),
    path('trades/',views.Trades,name="Trades"),
    path('markets/',views.Markets,name="Markets"),
    path('challenge/',views.Challenge,name="Challenge"),
    path('crear_trades/',views.crear_trade,name="crear_trades"),
    path('buscar_trades/',views.buscar_trade,name="buscar_trades"),
    path('buscar_notes/',views.buscar_note,name="buscar_notes"),
    path('buscar_mercados/',views.buscar_mercado,name="buscar_trades"),
    path('crear_notes/',views.crear_notes,name="crear_notes"),
    path('crear_mercados/',views.crear_mercados,name="crear_mercados"),
    
    
    
    
    
    # path('base/', views.base),
    
]

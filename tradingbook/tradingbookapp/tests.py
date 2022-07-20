from django.test import TestCase
from .models import Trade
import datetime


class TradeTest(TestCase):
    def setUp(self): # crear trade
        Trade.objects.create(fecha=datetime.datetime.now(),simbolo="NQ",posicion=2,entrada=20000,target=19800,stop=20100)
        
    def test_trade_simbolo(self): # solicitar trades con ese simbolo 
        trade = Trade.objects.get(posicion =2 )
        self.assertEqual(trade.simbolo, "NQ")

    def test_trade_creado(self): #solicitarlo de nuevo 
        trade = Trade.objects.get(posicion = 2)
        self.assertNotEquals(trade,None)
        
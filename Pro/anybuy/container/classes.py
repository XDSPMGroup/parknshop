from system.models import *
from store.classes import *
import time

class Cart_Class:
	CartCommodityList=[]
	CartQuantityList=[]
	CartDateList=[]
	CartAmout=0
	def __init__(self, cartID):		
		for c in Cart.objects.get(id = cartID):
			CommodityList.append(Commodity_class(k.CommodityID))
		for q in Cart.objects.get(id = cartID):
			QuantityList.append(q.CartCommodityAmount) 
		for q in Cart.objects.get(id = cartID):
			DateList.append(q.CartDate) 
		Amount = 0
		for k in Cart.objects.get(id = cartID):
			Amount = Amount+k.CartCommodityAmount*(Commodity.objects.get(CommodityID=k.CommodityID).SellPrice)
		self.CartCommodityList = CommodityList
		self.CartQuantityList = QuantityList
		self.CartDateList = DateList
		self.CartAmount = Amount

	def AddCommodity(self, customerID, commodityID):
		C = Cart(CartDate = time.strftime('%Y-%m-%d',time.localtime(time.time())), 
			CustomerID = customerID, CommodityID = commodityID)
		C.save()

	def DeleteCommodity(slef, ustomerID, commodityID):
		C = Cart.objects.get(CustomerID = customerID, CommodityID = commodityID)
		C.delete()

	def GetCommodityList():
		CommodityList = Commodity.objects.all()
		return CommodityList

#class Favorite_Class:


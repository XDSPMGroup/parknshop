from system.models import *
import time

class Cart_Class:
	CartCommodityList=[]
	CartQuantityList=[]
	CartDateList=[]
	CartAmout=0
	def __init__(self, customerID):
		CommodityList = Cart.objects.all(id = customerID)
		QuantityList = Cart.objects.all(id = customerID)
		DateList = Cart.objects.all(id = customerID)
		Amount = 0
		for k in CommodityList:
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


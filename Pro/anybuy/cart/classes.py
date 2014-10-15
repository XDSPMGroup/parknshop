from system.models import *
import time

class Cart_Class:
	CartCommodityList=0
	CartNumberList=0
	CartDateLis=0
	CartAmout=0
	def __init__(self, CustomerID):
		CartComList = Cart.objects.get()
		self.CartCommodityList = CartCommodityList
		self.CartNumberList = CartNumberList
		self.CartDateList = CartDateList
		self.CartAmout = CartAmout

	def AddCommodity(self, CustomerID, CommodityID):
		C = Cart(CartDate = time.strftime('%Y-%m-%d',time.localtime(time.time())), 
			CustomerID = CustomerID, CommodityID = CommodityID)
		C.save()

	def DeleteCommodity(slef, CustomerID, CommodityID):
		C = Cart.objects.get(CustomerID = CustomerID, CommodityID = CommodityID)
		C.delete()

	def GetCommodityList():
		CommodityList = Commodity.objects.all()
		return CommodityList


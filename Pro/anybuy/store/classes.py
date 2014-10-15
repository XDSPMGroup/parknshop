from system.models import *

class Commodity_class:
	"""This is Commodity class"""
	CommodityID = 0
	ShopID = 0
	CommodityName = 0
	CommodityType = ""
	CommoditySecondType = ""
	CommodityDescription = ""
	CommodityAmount = 0
	CommoditySoldAmount = 0
	PurchasePrice = 0
	OriginalPrice = 0
	CommodityImage = ""
	CommodityDiscount = 0
	CommentsList = []
	def __init__(self, commodityID):
		self.CommodityID = commodityID
		commodity = Commodity.objects.get(id=commodityID)
		self.ShopID = commodity.ShopID
		self.CommodityName = commodity.CommodityName
		self.CommodityType = commodity.CommodityType
		#self.CommoditySecondType = commodity.CommoditySecondType
		self.CommodityDescription = commodity.CommodityDescription
		self.CommodityAmount = commodity.CommodityAmount
		self.CommoditySoldAmount = commodity.SoldAmount
		self.PurchasePrice = commodity.PurchasePrice
		self.SellPrice = commodity.SellPrice
		self.PurchasePrice = commodity.PurchasePrice
		self.CommodityImage = commodity.CommodityImage
		self.CommodityDiscount = commodity.CommodityDiscount
		self.CommentsList = Comment.objects.get(CommodityID=commodityID)
	def SetDiscount(self, newDiscount):
		commodity = Commodity.objects.get(id=self.CommodityID)
		commodity.CommodityDiscount = newDiscount
		commodity.save()
	def GetDiscount(self):
		return self.CommodityDiscount
	def GetSellPrice(self):
		return self.SellPrice * self.CommodityDiscount
	def GetProfit(self):
		return self.GetSellPrice() - self.PurchasePrice

class Shop_class:
	"""This is Shop class"""
	ShopID = 0
	SellerID = 0
	ShopName = ""
	ShopState = 0 #(0-suspend, 1-open, 2-close)
	CommodityList = []
	ShopBriefInfo = ""
	ShopAds = []
	def __init__(self, shopID):
		self.ShopID = shopID
		shop = Shop.objects.get(id = shopID)
		self.SellerID = shop.SellerID
		self.ShopName = shop.ShopName
		self.ShopState = shop.ShopState #(0-suspend, 1-open, 2-close)
		self.CommodityList = Commodity.objects.get(ShopID = shopID)
		self.ShopBriefInfo = shop.ShopDescription
		#self.ShopAds = []
	def GetOrderList(self):
		orderList = []
		shopOrders = ShopOrder.objects.filter(ShopID = self.ShopID)
		for shopOrder in shopOrders:
			orderlist_temp = OrderList.objects.filter(ShopOrderID = shopOrder.ShopOrderID)
			orderList = orderList + orderlist_temp
		return orderList
	def GetOrder(self, OrderID):
		return OrderList.objects.get(ShopOrderID = OrderID)
	def ShopProfit(ShopID):
		pass
	def ConfirmRefund(OrderID):
		pass
	def RejectRefund(OrderID):
		pass
	def Close():
		pass
	def Open():
		pass
	def ModifyBasicInfo(newShop):
		pass
	def SetAdPage(newAdvertisement):
		pass
	def ViewCommodity(CommodityID):
		pass
	def AddCommodity(newCommodity):
		pass
	def ModifyCommodity(CommodityID):
		pass
	def DeleteCommodity(CommodityID):
		pass

class Advertisement_class(object):
	"""docstring for Advertisement"""
	OwnerID = 0
	CommodityList = []
	ShopList = []
	def __init__(self, arg):
		self.OwnerID = 0
		self.CommodityList = []
		self.ShopList = []
	def GetCommodityList():
		pass
	def GetShopList():
		pass
	def AddCommodity(newCommodity):
		pass
	def AddShop(newShop):
		pass
	def DeleteCommodity(CommodityID):
		pass
	def DeleteShop(ShopID):
		pass

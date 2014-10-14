from system.models import Shop
from system.models import Commodity
from system.models import Advertisement

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
		#self.CommoditySoldAmount = commodity.CommoditySoldAmount
		self.PurchasePrice = commodity.PurchasePrice
		self.OriginalPrice = commodity.OriginalPrice
		self.CommodityImage = commodity.CommodityImage
		self.CommodityDiscount = commodity.CommodityDiscount
		self.CommentsList = commodity.CommentsList

	def SetDiscount(newDiscount):
		pass
	def GetDiscount():
		pass
	def GetSellProce():
		pass
	def GetProfit():
		pass

class Shop:
	"""This is Shop class"""
	ShopID = 0
	SellerID = 0
	ShopName = ""
	ShopState = 0 #(0-suspend, 1-open, 2-close)
	CommodityList = []
	ShopBriefInfo = ""
	ShopAds = []
	def __init__(self):
		self.ShopID = 0
		self.SellerID = 0
		self.ShopName = ""
		self.ShopState = 0 #(0-suspend, 1-open, 2-close)
		self.CommodityList = []
		self.ShopBriefInfo = ""
		self.ShopAds = []
	def GetOrderList():
		pass
	def GetOrder(OrderID):
		pass
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

class Advertisement(object):
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

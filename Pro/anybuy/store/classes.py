#coding=utf-8
from system.models import *

class Commodity_class:
	"""This is Commodity class"""
	# 修改之后：
	#1，__init__函数中加入了多个参数，默认None；
	#2，用if commodityID != None来判断是以哪种方式调用
	#3，若没有传入commodityID，那就新建一个，并调用save()保存至数据库
	def __init__(self, commodityID = None, commodityName = None, shopID =None, commodityType = None, commodityDescription = None, commodityAmount = None, sellPrice = None, purchasePrice = None, commodityImage = None, commodityDiscount = None, commentsList = None,):
		if commodityID != None:
			self.commodityID = commodityID
			commodity = Commodity.objects.get(id=commodityID)
			self.shopID = commodity.ShopID
			self.commodityName = commodity.CommodityName
			self.commodityType = commodity.CommodityType
			#self.CommoditySecondType = commodity.CommoditySecondType
			self.commodityDescription = commodity.CommodityDescription
			self.commodityAmount = commodity.CommodityAmount
			self.commoditySoldAmount = commodity.SoldAmount
			self.purchasePrice = commodity.PurchasePrice
			self.sellPrice = commodity.SellPrice
			self.commodityImage = commodity.CommodityImage
			self.commodityDiscount = commodity.CommodityDiscount
			self.commentsList = Comment.objects.filter(CommodityID=commodityID)
		else:
			self.commodityName = commodityName
			self.commodityType = commodityType
			self.shopID = Shop.objects.get(id = shopID)
			#self.CommoditySecondType = CommoditySecondType
			self.commodityDescription = commodityDescription
			self.commodityAmount = commodityAmount
			self.commoditySoldAmount = 0
			self.purchasePrice = purchasePrice
			self.sellPrice = sellPrice
			self.commodityImage = commodityImage
			self.commodityDiscount = commodityDiscount
			self.save()
			#self.commentsList = commentsList
	def save(self): 
		commodity = Commodity()
		commodity.CommodityName=self.commodityName
		commodity.CommodityType=self.commodityType
		commodity.CommodityDescription=self.commodityDescription
		commodity.CommodityAmount=self.commodityAmount
		commodity.SoldAmount=self.commoditySoldAmount
		commodity.PurchasePrice=self.purchasePrice
		commodity.SellPrice=self.sellPrice
		commodity.CommodityImage=self.commodityImage
		commodity.CommodityDiscount=self.commodityDiscount
		commodity.ShopID = self.shopID
		commodity.save()
	def SetDiscount(self, newDiscount):
		commodity = Commodity.objects.get(id=self.commodityID)
		commodity.CommodityDiscount = newDiscount
		commodity.save()
	def GetDiscount(self):
		return self.commodityDiscount
	def GetSellPrice(self):
		return self.sellPrice * self.commodityDiscount
	def GetProfit(self):
		return self.GetSellPrice() - self.purchasePrice

class Shop_class:
	"""This is Shop class"""
	def __init__(self, shopID):
		self.shopID = shopID
		shop = Shop.objects.get(id = shopID)
		self.sellerID = shop.SellerID
		self.shopName = shop.ShopName
		self.shopState = shop.ShopState #(0-suspend, 1-open, 2-close)
		self.commodityList = Commodity.objects.filter(ShopID = shop)
		self.shopBriefInfo = shop.ShopDescription
		#Adv = []
		self.shopAdv = ShopAdv.objects.filter(OwnerID = shop)
		self.commodityAdv = CommodityAdv.objects.filter(OwnerID = shop)
	def GetOrderList(self): ###
		shop = Shop.objects.get(id = self.shopID)
		orderList = []
		shopOrders = ShopOrder.objects.filter(ShopID = shop)
		for shopOrder in shopOrders:
			orderlist_temp = OrderList.objects.filter(ShopOrderID = shopOrder.ShopOrderID)
			orderList = orderList + orderlist_temp
		return orderList
	def GetOrder(self, orderID): ###
		return OrderList.objects.get(ShopOrderID = orderID)
	def ShopProfit(self, shopID):
		pass
	def ConfirmRefund(self, orderID):
		orderList = OrderList.objects.get(OrderID = orderID)
		if orderList.OrderState == 4:
			orderList.OrderState = 5
			orderList.save()
			return 1
		else:
			return 0
	def RejectRefund(self, orderID):
		orderList = OrderList.objects.get(OrderID = orderID)
		if orderList.OrderState == 4:
			orderList.OrderState = 6
			orderList.save()
			return 1
		else:
			return 0
	def Close(self):
		shop = Shop.objects.get(id = self.shopID)
		if shop.ShopState == 1:
			shop.ShopState = 2
			shop.save()
			return 1
		else: 
			return 0
	def Open(self):
		shop = Shop.objects.get(id = self.shopID)
		if shop.ShopState == 2:
			shop.ShopState = 1
			shop.save()
			return 1
		else: 
			return 0
	def ModifyBasicInfo(self, newShop):  #####! need modify
		shop = Shop.objects.get(id = self.shopID)
		shop = newShop
		shop.save()
	def SetAdPage(newAdvertisement):
		pass
	def ViewCommodity(self, commodityID):
		return Commodity.objects.get(id=commodityID)
	def AddCommodity(self, name = None, description = None, camount = None, samount = None, pprice = None, sprice = None, ctype = None, img = None, dicount = None):
		shop = Shop.objects.get(ShopID = self.shopID)
		Commodity.objects.create(CommodityName = name, CommodityDescription = description, CommodityAmount = camount, SoldAmount = samount, PurchasePrice = pprice, SellPrice = sprice, CommodityType = ctype, CommodityImage = img, CommodityDiscount = dicount, ShopID = shop)
	def ModifyCommodity(self, name = None, description = None, camount = None, samount = None, pprice = None, sprice = None, ctype = None, img = None, dicount = None):
		commodity = Commodity.objects.get(id=commodityID)
		##### commodity.
	def DeleteCommodity(self, commodityID):
		Commodity.objects.get(id=commodityID).delete()

class Adv_class(object):
	"""docstring for Advertisement"""
	def __init__(self, ownerType, ownerID):
		self.ownerID = ownerID
		self.Type = ownerType
		if self.Type == "HomePage":
			self.ownerID = Administrator.objects.get(id = ownerID)
			self.shopList = HomeShopAdv.objects.filter(ownerID = self.ownerID)
			self.commodityList = HomeCommodityAdv.objects.filter(ownerID = self.ownerID)
		else:
			self.ownerID = Seller.objects.get(id = ownerID)
			self.shopList = ShopAdv.objects.filter(ownerID = self.ownerID)
			self.commodityList = CommodityAdv.objects.filter(ownerID = self.ownerID)
	def GetCommodityList(self):
		pass
	def GetShopList(self):
		pass
	def AddCommodity(self, commodity, description = None): #here commodity is a existed Commodity_class
		if self.Type == "HomePage":
			owner = Administrator.objects.get(id = self.ownerID)
			HomeCommodityAdv.objects.create(CommodityID = commodity, OwnerID = owner, AdvertisementContent = description)
		else:
			owner = Seller.objects.get(id = self.ownerID)
			HomeCommodityAdv.objects.create(CommodityID = commodity, OwnerID = owner, AdvertisementContent = description)
	def AddShop(self, shop, description = None): #here shop is a existed shop_classes
		if self.Type == "HomePage":
			owner = Administrator.objects.get(id = self.ownerID)
			HomeShopAdv.objects.create(ShopID = shop, OwnerID = owner, AdvertisementContent = description)
		else:
			owner = Seller.objects.get(id = self.ownerID)
			HomeShopAdv.objects.create(ShopID = shop, OwnerID = owner, AdvertisementContent = description)
	def DeleteCommodity(self, commodity):
		if self.Type == "HomePage":
			owner = Administrator.objects.get(id = self.ownerID)
			HomeCommodityAdv.objects.get(CommodityID = commodity, ownerID = owner).delete()
		else:
			owner = Seller.objects.get(id = self.ownerID)
			HomeCommodityAdv.objects.get(CommodityID = commodity, OwnerID = owner).delete()
	def DeleteShop(self, ShopID):
		if self.Type == "HomePage":
			owner = Administrator.objects.get(id = self.ownerID)
			HomeShopAdv.objects.get(CommodityID = commodity, ownerID = owner).delete()
		else:
			owner = Seller.objects.get(id = self.ownerID)
			HomeShopAdv.objects.get(CommodityID = commodity, OwnerID = owner).delete()

#encoding:UTF-8
from system.models import *
from store.classes import *
import time

class Cart_class:
	CartCommodityList=[]
	CartQuantityList=[]
	CartDateList=[]
	CartAmount=0
	def __init__(self, cartID):		
		CommodityList = []
		QuantityList = []
		DateList = []
		Amount = 0
		# Commodity List
		for c in Cart.objects.filter(id = cartID):
			#CommodityList.append(Commodity_class(c.CommodityID.id))
			CommodityList.append(c)
		# Quantity List
		for q in Cart.objects.filter(id = cartID):
			QuantityList.append(q.CartCommodityAmount) 
		# Date List
		for d in Cart.objects.filter(id = cartID):
			DateList.append(d.CartDate) 
		# Commodity total value
		for k in Cart.objects.filter(id = cartID):
			Amount = Amount+k.CartCommodityAmount*\
				((Commodity.objects.get(id=k.CommodityID.id)).SellPrice)
		self.CartCommodityList = CommodityList
		self.CartQuantityList = QuantityList
		self.CartDateList = DateList
		self.CartAmount = Amount
	
	# 在购物车添加商品
	def AddCommodity(self, customerID, commodityID):
		C = Cart(CartDate = time.strftime('%Y-%m-%d',time.localtime(time.time())),\
			CustomerID = Customer.objects.get(id = customerID), \
			CommodityID = Commodity.objects.get(id = commodityID))
		C.save()

	#在购物车删除商品
	def DeleteCommodity(self, customerID, commodityID):
		C = Cart.objects.get(CustomerID = Customer.objects.get(id = customerID),\
			CommodityID=Commodity.objects.get(id = commodityID))
		C.delete()

	#获得购物车的商品列表
	def GetCommodityList(self):
		#CommodityList = Commodity.objects.all()
		return self.CartCommodityList

		
class Favorite_class:
	CommodityList=[]
	DateList=[]
	def __init__(self, favoriteID):		
		CommodityListTemp = []
		DateListTemp = []
		# Commodity List
		for c in Favorite.objects.filter(id = favoriteID):
			CommodityListTemp.append(Commodity_class(c.CommodityID.id))
		# Date List
		for d in Favorite.objects.filter(id = favoriteID):
			DateListTemp.append(d.FavoriteDate) 
		self.CommodityList = CommodityListTemp
		self.DateList = DateListTemp
	
	# 在收藏夹添加商品
	def AddCommodity(self, customerID, commodityID):
		C = Favorite(FavoriteDate = time.strftime('%Y-%m-%d',time.localtime(time.time())),\
			CustomerID = Customer.objects.get(id = customerID), \
			CommodityID = Commodity.objects.get(id = commodityID))
		C.save()

	#在收藏夹删除商品
	def DeleteCommodity(self, customerID, commodityID):
		C = Favorite.objects.get(CustomerID = Customer_class(customerID),\
			CommodityID=Commodity_class(commodityID))
		C.delete()

	#获得收藏夹的商品列表
	def GetCommodityList(self):
		#CommodityList = Commodity.objects.all()
		return self.CommodityList

class Order_class:
	OrderID=0
	OrderDate=time.strftime('%Y-%m-%d',time.localtime(time.time()))
	OrderState=0  
	OrderExpressID=""
	OrderTransfee=0
	OrderCost=0.0
	OrderProfit=0
	OrderCommodityList=[]
	OrderCommodityNumberList=[]
	def __init__(self,shopID,orderID):	
   		CommodityList=[]
		CommodityNumberList =[]
		Cost=0
		for o in Commodity.objects.filter( ShopID=Shop.objects.get(id=shopID)):
			CommodityList.append(o)    
		self.OrderCommodityList= CommodityList
		for n in Commodity.objects.filter( ShopID=Shop.objects.get(id=shopID)):
			CommodityNumberList.append(n.CommodityAmount)
		self.OrderCommodityNumberList=CommodityNumberList
		for n in Commodity.objects.filter( ShopID=Shop.objects.get(id=shopID)):
			Cost+=n.CommodityAmount*n.SellPrice
		self.OrderCost=Cost
		self.OrderID=orderID
		order=OrderList.objects.get(id=orderID)
		self.OrderDate=order.OrderListDate
		self. OrderState=order. OrderListState
		self.OrderExpressID=  ""
		# self.OrderTransfee=OrderTransfee
		self.OrderProfit=0

	def GetCommodityList(self,orderID):
		OrderCommodityList=[]
		OrderCommodityList.append(OrderList.objects.get(id=orderID).CommodityID)
		return OrderCommodityList

	def SetOrderState(self,orderState):
		order=OrderList.objects.get(id=self.OrderID)
		order.OrderListState=orderState
		order.save()

	def GetOrderProfit(self):
		TotalCost=0
		for commodity in self.OrderCommodityList: 
			TotalCost+= (commodity.SoldAmount * (commodity.SellPrice-commodity.PurchasePrice))
		return TotalCost


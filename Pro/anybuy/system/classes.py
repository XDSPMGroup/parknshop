#encoding:utf-8

from system.models import *
from store.classes import *
class Administrator_class:
	#管理员ID编号
	AdministratorID = 0
	#管理员帐号
	AdministratorAccount = ""
	#管理员密码
	AdministratorPassword = ""
	#管理员昵称
	AdministratorName = ""
	#管理员电话    
	AdministratorTelephone = 0 
	#管理员邮件 
	AdministratorEmail = ""
	#主页店铺广告   
	HomeShopAdvList = []
	#主页商品广告     
	HomeCommodityAdvList = []
	#卖家黑名单     
	SellerBlackList = []
	 #买家黑名单      
	CustomerBlackList = []

	def __init__(self, administratorID):
		self.AdministratorID = administratorID
		admin = Administrator.objects.get(id = administratorID)
		self.AdministratorAccount = admin.AdministratorAccount
		self.AdministratorPassword = admin.AdministratorPassword
		self.AdministratorName = admin.AdministratorName
		self.AdministratorTelephone = admin.AdministratorTelephone
		self.AdministratorEmail = admin.AdministratorEmail
		#Advertisement
		self.HomeShopAdvList = HomeShopAdv.objects.filter(OwnerID = administratorID)
		self.HomeCommodityAdvList = HomeCommodityAdv.objects.filter(OwnerID = administratorID)
		#BlackList
		self.SellerBlackList = BlacklistSeller.objects.get(AdministratorID = administratorID)
		self.CustomerBlackList = BlacklistCustomer.objects.get(AdministratorID = administratorID)
	        
	def GetOrderList(self):    #获得所有订单以查看销售历史。
		return OrderList.objects.filter(OrderListState = 3)
	
	def GetCommission(self):   #计算出每一笔交易的佣金。
		ComissionList = []
		for c in OrderList.objects.filter(OrderListState = 3):
			ComissionList.append((Commodity.objects.get(id=c.CommodityID.id).SellPrice)*\
				(System.objects.get(id=1)).ComissionRate)
		return ComissionList

	def GetSpecificOrder(self, orderListID):       #获得特定订单
		return OrderList.objects.get(id = orderListID)

	def Login(self, account, password):       #管理员登录
		admin = Administrator.objects.get(AdministratorAccount = account)
		if (password == admin.AdministratorPassword):
			return 1

	def BackupDB(self):   #备份数据库
		pass
	
	def RestoreDB(self):  #恢复数据库
		pass

	def ShopListDealShopApply(self):  #处理店铺申请,从数据库中选择所有店铺状态为’待审核’的店铺。
		return Shop.objects.filter(ShopState = 0)
	
	def PassApply(self, shopID):    #审核通过
		state = (Shop.objects.get(id = shopID)).ShopState
		if(state == 1 or state == 2):
			print "The shop has pass audit!"
		else:
			s = Shop.objects.get(id = shopID)
			s.ShopState = 1
			s.save()
	
	def RejectApply(self, shopID):  #审核不通过
		state = (Shop.objects.get(id = shopID)).ShopState
		if(state == 1 or state == 2):
			print "The shop has pass audit!"
		else:
			print "Reject! Please modify your info!"
	
	def BlacklistCustomer(self, customerID):  #拉黑买家,参数为买家ID
		r = raw_input("input:")  #input BlacklistReason
		b = BlacklistCustomer(BlacklistCustomerReason = r,\
			AdministratorID = Administrator.objects.get(id = self.AdministratorID), \
			CustomerID = Customer.objects.get(id = customerID))
		b.save()
	
	def BlacklistSeller(self, sellerID):    #拉黑卖家,参数为卖家ID
		r = raw_input("input:")   #input BlacklistReason
		b = BlacklistSeller(BlacklistSellerReason = r,
			AdministratorID = Administrator.objects.get(id = self.AdministratorID), \
			SellerID = Seller.objects.get(id = sellerID))
		b.save()

	def GetBlacklistCustomer(self):  #查看买家黑名单信息
		return BlacklistCustomer.objects.all()

	def GetBlacklistSeller(self):  #查看卖家黑名单信息
		return BlacklistSeller.objects.all()

	def RestoreCustomer(self, customerID):  #恢复买家帐号
		c = BlacklistCustomer.objects.get(id = customerID)
		c.delete()

	def RestoreSeller(self, sellerID):    #恢复卖家帐号
		s = BlacklistSeller.objects.get(id = sellerID)
		s.delete()
	
	def DeleteCustomer(self, customerID):   #删除买家帐号
		c = Customer.objects.get(id = customerID)
		c.delete()
	
	def DeleteSeller(self, sellerID):     #删除卖家帐号
		s = Seller.objects.get(SellerID = sellerID)
		s.delete()
	
	def SetHomeShopAdv(self, shopID, ownerID):  #配置主页店铺广告
		r = raw_input("input:")   #input AdvertisementContent
		Adv = HomeShopAdv(ShopID = Shop_class(shopID), \
			OwnerID = self.AdministratorID, AdvertisementContent = r)
		Adv.save()
	        
	def SetHomeCommodityAdv(self, commodityID, ownerID):  #配置主页商品广告
		r = raw_input("input:")   #input AdvertisementContent
		Adv = HomeShopAdv(CommodityID = Commodity_class(commodityID), \
			OwnerID = self.AdministratorID, AdvertisementContent = r)
		Adv.save()




class System_class:
	"""This is System class"""
	Announcement = ""        #公告(String)
	AnnouncementDate = ""    #公告时间
	CommissionRate = 0       #交易佣金率(每一笔交易都要收取)
	def __init__(self, systemID):
		self.Announcement = (System.objects.get(id = 1)).BulletinBoardDescription
		self.AnnouncementDate = (System.objects.get(id = 1)).BulletinBoardDate
		self.CommissionRate = (System.objects.get(id = 1)).ComissionRate
	

	def GetAnnouncement(self):  #查看公告板(公共API)
		return (System.objects.get(id = 1)).BulletinBoardDescription 
	
	def ModifyAnnouncement(self):       #修改公告(系统管理员权限)
		r = raw_input("input:")
		p = System.objects.get(id = 1)
		p.BulletinBoardDescription = r                         
		p.save()
	
	def GetCommissionRate(self):
		return (System.objects.get(id = 1)).ComissionRate
	
	def SetCommissionRate(self, commissionRate):
		s = System.objects.get(id = 1)
		s.ComissionRate = commissionRate
		s.save()

	























        

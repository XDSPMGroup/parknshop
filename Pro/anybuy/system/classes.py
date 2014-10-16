from system.models import Administrator
from system.models import System
from system.models import Advertisement
from system.models import OrderList
from system.models import Shop
from system.models import Seller
from system.models import Customer
from system.models import BlacklistSeller
from system.models import BlacklistCustomer



class Administrator_class:
        """This is Administrator class"""
        AdministratorID = 0           #管理员ID编号
	AdministratorAccount = ""     #管理员帐号
	AdministratorPassword = ""    #管理员密码
	AdministratorName = ""        #管理员昵称
	AdministratorTelephone = 0    #管理员电话
	AdministratorEmail = ""       #管理员邮件
	Advertisement                 #广告
	SellerBlackList = []          #卖家黑名单
	CustomerBlackList = []        #买家黑名单
	def __init__(self,administratorID):
	        self.AdministratorID = administratorID
	        admin = Administrator.objects.get(id=administratorID)
	        self.AdministratorAccount = admin.AdministratorAccount
	        self.AdministratorPassword = admin.AdministratorPassword
	        self.AdministratorName = admin.AdministratorName
	        self.AdministratorTelephone = admin.AdministratorTelephone
	        self.AdministratorEmail = admin.AdministratorEmail
	        #Advertisement
	        self.SellerBlackList = SellerBlackList.object.get(AdministratorID = administratorID)
	        self.CustomerBlackList = CustomerBlackList.object.get(AdministratorID = administratorID)
	        
	def GetOrderList():    #获得所有订单以查看销售历史。
	        return OrderList.objects.filter(OrderState = 3)
	
	def GetCommission():   #计算出每一笔交易的佣金。
	        a = []
	        b = OrderList.objects.filter(OrderState = 3)
	        for c in b.OrderProfit
	            a.append(c * System.ComissionRate)
	        return a

	def GetOrder(i):       #获得特定订单
	        return OrderList.objects.filter(OrderID = i)

	def Login(a, p):       #管理员登录
                b = Administrator.objects.filter(AdministratorAccount = a)
                if p = b.AdministratorPassword
                    return 1

	def BackupDB():   #备份数据库
	        pass
	
	def RestoreDB():  #恢复数据库
	        pass

	def ShopList DealShopApply():  #处理店铺申请,从数据库中选择所有店铺状态为’待审核’的店铺。
	        return Shop.objects.filter(ShopState = 0)
	
	def PassApply(i):    #审核通过
	        s = Shop.objects.filter(ShopID = i)
	        s.ShopState = 1
	        s.save()
	        return 1
	
	def RejectApply(i):  #审核不通过
	        s = Shop.objects.filter(ShopID = i)
	        s.ShopState = 2
	        s.save()
	        return 1
	
	def BlacklistCustomer(self, c):  #拉黑买家,参数为买家ID
	        r = raw_input("input:")
	        b = BlacklistCustomer(BlacklistCustomerID = ,
                                      AdministratorID = self.AdministratorID,
                                      CustomerID = c ,
                                      BlacklistCustomerReason = r)
	
	def BlacklistSeller(self, s):    #拉黑卖家,参数为卖家ID
	        r = raw_input("input:")
	        b = BlacklistCustomer(BlacklistCustomerID = ,
                                      AdministratorID = self.AdministratorID,
                                      CustomerID = s ,
                                      BlacklistCustomerReason = r)

	def GetBlacklist():  #查看黑名单信息,返回账户列表。
	        return SellerBlackList.objects.all(),CustomerBlackList.objects.all()

	def RestoreCustomer(c):  #恢复帐号
	        p = CustomerBlackList.object.get(CustomerID = c)
	        p.delete()

	def RestoreSeller(s):    #恢复帐号
	        p = SellerBlackList.object.get(CustomerID = s)
	        p.delete()
	
	def DeleteCustomer(c):   #删除帐号
	        p = Customer.object.get(CustomerID = c)
	        p.delete()
	
	def DeleteSeller(s):     #删除帐号
	        p = Seller.object.get(SellerID = s)
	        p.delete()
	
	def SetAd(Advertisement Ad):  #配置主页广告
	        pass
	        
 





class System_class:
        """This is System class"""
        Announcement = ""        #公告(String)
        Date = 0                 #公告时间
	CommissionRate = 0       #交易佣金率(每一笔交易都要收取)
	def __init__(self)
		self.Announcement = Announcement
		self.Date = Date
		self.CommissionRate = CommissionRate
	
	def GetAnnouncement(self):      #查看公告板(公共API)
		return self.Announcement 
	
	def ModifyAnnouncement():       #修改公告(系统管理员权限)
                r = raw_input("input:")
		p = System.objects.get(BulletinBoardContent=String)
		p.BulletinBoardContent = r                         
		p.save()
	
	def GetCommissionRate(self):
		return self.CommissionRate 
	
	def SetCommissionRate(self, n):
		self.CommissionRate = n
		return self.CommissionRate

	























        

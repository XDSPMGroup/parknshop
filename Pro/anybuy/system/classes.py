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
        AdministratorID = 0           #����ԱID���
	AdministratorAccount = ""     #����Ա�ʺ�
	AdministratorPassword = ""    #����Ա����
	AdministratorName = ""        #����Ա�ǳ�
	AdministratorTelephone = 0    #����Ա�绰
	AdministratorEmail = ""       #����Ա�ʼ�
	Advertisement                 #���
	SellerBlackList = []          #���Һ�����
	CustomerBlackList = []        #��Һ�����
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
	        
	def GetOrderList():    #������ж����Բ鿴������ʷ��
	        return OrderList.objects.filter(OrderState = 3)
	
	def GetCommission():   #�����ÿһ�ʽ��׵�Ӷ��
	        a = []
	        b = OrderList.objects.filter(OrderState = 3)
	        for c in b.OrderProfit
	            a.append(c * System.ComissionRate)
	        return a

	def GetOrder(i):       #����ض�����
	        return OrderList.objects.filter(OrderID = i)

	def Login(a, p):       #����Ա��¼
                b = Administrator.objects.filter(AdministratorAccount = a)
                if p = b.AdministratorPassword
                    return 1

	def BackupDB():   #�������ݿ�
	        pass
	
	def RestoreDB():  #�ָ����ݿ�
	        pass

	def ShopList DealShopApply():  #�����������,�����ݿ���ѡ�����е���״̬Ϊ������ˡ��ĵ��̡�
	        return Shop.objects.filter(ShopState = 0)
	
	def PassApply(i):    #���ͨ��
	        s = Shop.objects.filter(ShopID = i)
	        s.ShopState = 1
	        s.save()
	        return 1
	
	def RejectApply(i):  #��˲�ͨ��
	        s = Shop.objects.filter(ShopID = i)
	        s.ShopState = 2
	        s.save()
	        return 1
	
	def BlacklistCustomer(self, c):  #�������,����Ϊ���ID
	        r = raw_input("input:")
	        b = BlacklistCustomer(BlacklistCustomerID = ,
                                      AdministratorID = self.AdministratorID,
                                      CustomerID = c ,
                                      BlacklistCustomerReason = r)
	
	def BlacklistSeller(self, s):    #��������,����Ϊ����ID
	        r = raw_input("input:")
	        b = BlacklistCustomer(BlacklistCustomerID = ,
                                      AdministratorID = self.AdministratorID,
                                      CustomerID = s ,
                                      BlacklistCustomerReason = r)

	def GetBlacklist():  #�鿴��������Ϣ,�����˻��б�
	        return SellerBlackList.objects.all(),CustomerBlackList.objects.all()

	def RestoreCustomer(c):  #�ָ��ʺ�
	        p = CustomerBlackList.object.get(CustomerID = c)
	        p.delete()

	def RestoreSeller(s):    #�ָ��ʺ�
	        p = SellerBlackList.object.get(CustomerID = s)
	        p.delete()
	
	def DeleteCustomer(c):   #ɾ���ʺ�
	        p = Customer.object.get(CustomerID = c)
	        p.delete()
	
	def DeleteSeller(s):     #ɾ���ʺ�
	        p = Seller.object.get(SellerID = s)
	        p.delete()
	
	def SetAd(Advertisement Ad):  #������ҳ���
	        pass
	        
 





class System_class:
        """This is System class"""
        Announcement = ""        #����(String)
        Date = 0                 #����ʱ��
	CommissionRate = 0       #����Ӷ����(ÿһ�ʽ��׶�Ҫ��ȡ)
	def __init__(self)
		self.Announcement = Announcement
		self.Date = Date
		self.CommissionRate = CommissionRate
	
	def GetAnnouncement(self):      #�鿴�����(����API)
		return self.Announcement 
	
	def ModifyAnnouncement():       #�޸Ĺ���(ϵͳ����ԱȨ��)
                r = raw_input("input:")
		p = System.objects.get(BulletinBoardContent=String)
		p.BulletinBoardContent = r                         
		p.save()
	
	def GetCommissionRate(self):
		return self.CommissionRate 
	
	def SetCommissionRate(self, n):
		self.CommissionRate = n
		return self.CommissionRate

	























        

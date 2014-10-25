#coding=utf-8
from system.models import *
from store.classes import *
    
class Customer_class():
    def __init__(self, customerid):
        self.id = customerid
        customer = Customer.objects.get(id = customerid)
        self.account = customer.CustomerAccount
        self.password = customer.CustomerPassword
        self.name = customer.CustomerName
        self.tel = customer.CustomerTelephone
        self.email = customer.CustomerEmail
        self.add = customer.CustomerAddress
        self.customerOrderList = CustomerOrder.objects.filter(CustomerID = customer)
    def ModifyBasicInfo(self): #修改基本信息，用户昵称，电话，邮件，邮寄地址。返回成功与否。
        pass
    #def ModifyPassword(Sting Old,String New)# 修改密码
    #               参数为旧密码与新密码，先匹配旧密码，旧密码匹配成功则修改新密码至数据库。修改成功返回1.失败返回0.
    def DeleteOrder(self, orderid): #删除订单,根据OrderID删除对应订单。返回成功与否。
        CustomerOrder.objects.get(orderid).delete
    def PayOrder(self, orderid): #确认订单付款.
        pass
    def Refund(self, orderid): # 申请订单退款
        pass
    #def CommentOrder(self, orderid, string): # 评论订单商品，传入OrderID, 依次对每个商品进行评论。
    def CommentCommodity(self, commodityid, comment):# 评论特定商品。返回成功与否。
        Comment.objects.create(
            CommentContent = comment, 
            CustomerID = Customer.objects.get(id=self.id), 
            CommodityID = Commodity.objects.get(id=commodityid))
    def GenerateOrder(self):# 生成订单(根据购物车),添加新订单至CustomerOrderList, 并返回新OrderID.
        pass
    def GetShop(self, shopid): # 进入具体店铺
        return Shop_class(shopid)
    def ApplyNewShop(Shop): # 申请新店铺,用户填写申请表，写入基本店铺信息，生成new Shop, 店铺状态为待审核。返回申请提交成功与否。
        pass

class Seller:
    def __init__(self, sellerid):
        self.id = sellerid
        seller = Seller.objects.get(id=sellerid)
        self.account=seller.SellerAccount
        self.pw=seller.SellerPassword #密码
        self.name=seller.SellerName #用户昵称
        self.realname=seller.SellerRealName #卖家实名
        self.realid=seller.SellerRealID #身份证号
        self.tel=seller.SellerTelephone #电话
        self.email=seller.SellerEmail #邮件地址
        self.shopList = Shop.objects.filter(SellerID = seller)
    def GetShop(self, shopid):# 进入具体店铺
        return Shop_class(shopid)
    def ApplyNewShop(self, shopdescription, shopname): # 申请新店铺,用户填写申请表，写入基本店铺信息，生成new Shop, 店铺状态为待审核。返回申请提交成功与否。
        Shop.objects.create(
        ShopDescription = shopdescription, 
        SellerID = Seller.objects.get(id=self.id), 
        ShopName = shopname, 
        ShopState = 0)
    def ModifyPassword(self, Old, New):# 修改密码
        pass            #参数为旧密码与新密码，先匹配旧密码，旧密码匹配成功则修改新密码至数据库。修改成功返回1.失败返回0.
    def ModifyBasicInfo(Seller):# 修改基本信息，用户昵称，电话，邮件等。返回成功与否。
        pass

'''class Administrator
    def __init__(self, admid):
        self.id =admid
        adm = Administrator.objects.get(id=admid)
        self.account = adm.AdministratorAccount
        self.pw = adm.AdministratorPassword
        self.name = adm.AdministratorName
        self.tel = adm.AdministratorTelephone
        self.email = adm.AdministratorEmail 
        self.adv = Adv_class('Homepage', admid)
        #self.sellerBlackList = 
        #self.customerBlackList = 
        OrderList GetOrderList()# 获得所有订单以查看销售历史。并计算出每一笔交易的佣金。
        Order GetOrder(integer OrderID)# 获得特定订单
        int Login(Account, Password)# 管理员登录
        int BackupDB()# 备份数据库
        int RestoreDB()# 恢复数据库
        ShopList DealShopApply()# 处理店铺申请,从数据库中选择所有店铺状态为’待审核’的店铺。
        int PassApply(ShopID)# 审核通过
        int RejectApply(ShopID)# 审核不通过 
        int BlacklistCustomer(integer CustomerID)# 拉黑用户, 参数为用户ID
        int BlacklistSeller(integer SellerID)#
        GuestList GetBlacklist()# 查看黑名单信息,返回账户列表。
        int RestoreCustomer(integer CustomerID)# 恢复帐号
        int RestoreSeller(integer SellerID)# 恢复帐号
        int DeleteCustomer(integer CustomerID)# 删除帐号
        int DeleteSeller(integer SellerID)# 删除帐号
        int SetAd(Advertisement Ad)# 配置主页广告
'''
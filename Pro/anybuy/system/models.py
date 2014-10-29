#encoding:utf-8
from django.db import models


# Create your models here.

class HelpCenter(models.Model):
	HelpCenterName = models.CharField(max_length=64)
	HelpCenterContent = models.TextField(blank=True)
	def __unicode__(self):
		return self.HelpCenterName

class Seller(models.Model):
	SellerTypeChoices=(
		(0,'limited user'),
		(1,'normal user'),
	)
	SellerAccount = models.CharField(max_length=64)
	SellerPassword = models.CharField(max_length=32)
	SellerName = models.CharField(max_length=64)
	SellerType = models.CharField(max_length=1,choices=SellerTypeChoices,blank=True)
	SellerRealName = models.CharField(max_length=64,null=True)
	SellerRealID = models.IntegerField(null=True)
	SellerTelephone = models.CharField(max_length=64,blank=True)
	SellerEmail = models.EmailField(blank=True)
	SellerAddress = models.CharField(max_length=64,blank=True)
	def __unicode__(self):
		return '%s %s' %(self.SellerAccount,self.SellerName)

class Shop(models.Model):
	States=(
		(0, 'checking'),
		(1, 'open'),
		(2, 'close')
	)
	ShopDescription = models.TextField(blank=True)
	SellerID = models.ForeignKey(Seller)
	ShopName = models.CharField(max_length=64,blank=True)
	#店铺状态：0-待审核，1-营业，2-歇业
	ShopState = models.IntegerField(choices=States)
	BigImage = models.ImageField(upload_to='images',max_length=255,blank=True,null=True)
	ShopImage = models.ImageField(upload_to='images',max_length=255,blank=True,null=True)
	IsAdv = models.BooleanField()
	IsHomeAdv = models.BooleanField()
	def __unicode__(self):
		return self.ShopName

class Commodity(models.Model):
	CommodityTypeChoices=(
		('C','Clothing'),
		('A','Accesory'),
		('S','Sport'),
		('J','Jewelry'),
		('D','Digit'),
		('H','Household appliances'),
		('M','Makeup'),
		('F','Food'),
		('E','Entertainment'),
		('O','Others')
	)
	CommodityName = models.CharField(max_length=64)
	CommodityDescription = models.TextField(blank=True)
	CommodityAmount = models.IntegerField(blank=True,null=True)
	SoldAmount = models.IntegerField(blank=True)
	PurchasePrice = models.FloatField(blank=True)
	SellPrice = models.FloatField(blank=True)
	CommodityType = models.CharField(max_length=1,choices=CommodityTypeChoices,blank=True)
	CommodityImage = models.ImageField(upload_to='images',max_length=255,blank=True,null=True)
	CommodityDiscount = models.FloatField(null=True,blank=True)
	ShopID = models.ForeignKey(Shop)
	IsAdv = models.BooleanField()
	IsHomeAdv = models.BooleanField()
	def __unicode__(self):
		return '%s %s %s' %(self.CommodityName, self.CommodityType, self.CommodityAmount)

class Administrator(models.Model):
	AdministratorAccount = models.CharField(max_length=64)
	AdministratorName = models.CharField(max_length=64)
	AdministratorPassword = models.CharField(max_length=16)
	AdministratorTelephone = models.CharField(max_length=64,blank=True)
	AdministratorEmail = models.EmailField()
	def __unicode__(self):
		return self.AdministratorName

class ShopAdv(models.Model):
	ShopID = models.ForeignKey(Shop)
	OwnerID = models.ForeignKey(Seller)
	AdvertisementContent = models.TextField()

class CommodityAdv(models.Model):
	CommodityID = models.ForeignKey(Commodity)
	OwnerID = models.ForeignKey(Seller)
	AdvertisementContent = models.TextField()

class HomeShopAdv(models.Model):
	ShopID = models.ForeignKey(Shop)
	OwnerID = models.ForeignKey(Administrator)
	AdvertisementContent = models.TextField()

class HomeCommodityAdv(models.Model):
	CommodityID = models.ForeignKey(Commodity)
	OwnerID = models.ForeignKey(Administrator)
	AdvertisementContent = models.TextField()

class System(models.Model):
	BulletinBoardContent = models.CharField(max_length=64,blank=True)
	BulletinBoardDescription = models.TextField(blank=True)
	BulletinBoardDate = models.DateField(blank=True)
	ComissionRate = models.FloatField(blank=True)
	def __unicode__(self):
		return '%s %s' %(self.BulletinBoardDate,self.BulletinBoardContent)

class BlacklistSeller(models.Model):
	BlacklistSellerReason = models.TextField()
	SellerID = models.ForeignKey(Seller)
	AdministratorID = models.ForeignKey(Administrator)
	def __unicode__(self):
		return self.BlacklistSellerReason

class Discount(models.Model):
	DiscountRate = models.FloatField(blank=True)
	SellerID = models.ForeignKey(Seller)
	ShopID = models.ForeignKey(Shop)
	def __unicode__(self):
		return '%s' %(self.DiscountRate)

class ShopOrder(models.Model):
	StateChoices=(
		(0, 'paying'),
		(1, 'shipping'),
		(2, 'signing'),
		(3, 'commenting'),
		(4, 'refunding'),
		(5, 'refunded'),
		(6, 'refund refuded'),
		(7, 'finish'),
	)
	ShopOrderState = models.IntegerField(choices=StateChoices)
	ShopOrderDate = models.DateField()
	ShopID = models.ForeignKey(Shop)
	def __unicode__(self):
		return '%s %s' %(self.ShopOrderDate, self.ShopOrderState)

class Customer(models.Model):
	CustomerTypeChoices=(
		(0,'limited user'),
		(1,'normal user'),
	)
	CustomerAccount = models.CharField(max_length=64)
	CustomerName = models.CharField(max_length=64)
	CustomerPassword = models.CharField(max_length=32)
	CustomerType = models.CharField(max_length=1,choices=CustomerTypeChoices,blank=True)
	CustomerTelephone = models.CharField(max_length=64,blank=True)
	CustomerEmail = models.EmailField()
	CustomerAddress = models.TextField(blank=True)
	def __unicode__(self):
		return u'%s %s' %(self.CustomerAccount, self.CustomerName)

class CustomerOrder(models.Model):
	StateChoices=(
		(0, 'paying'),
		(1, 'shipping'),
		(2, 'signing'),
		(3, 'commenting'),
		(4, 'refunding'),
		(5, 'refunded'),
		(6, 'refund refuded'),
		(7, 'finish'),
	)
	CustomerOrderState = models.IntegerField(choices=StateChoices)
	CustomerOrderDate = models.DateField()
	CustomerID = models.ForeignKey(Customer)
	def __unicode__(self):
		return '%s %s' %(self.CustomerOrderState, self.CustomerOrderDate)

class OrderList(models.Model):
	#OrderListAccount = models.CharField(max_length=64)
	#订单状态：0-待付款，1-已付款待发货，2-待签收，
	# 3-待评价，4-待退款，5-退款成功，6-卖家拒绝退款
	StateChoices=(
		(0, 'paying'),
		(1, 'shipping'),
		(2, 'signing'),
		(3, 'commenting'),
		(4, 'refunding'),
		(5, 'refunded'),
		(6, 'refused refunded'),
		(7, 'finish'),
	)
	OrderListState = models.IntegerField(choices=StateChoices)
	OrderListDate = models.DateField()
	OrderAmount = models.IntegerField(blank=True, null=True)
	#SellerID = models.ForeignKey(Seller)
	ShopOrderID = models.ForeignKey(ShopOrder)
	CustomerOrderID = models.ForeignKey(CustomerOrder)
	CommodityID = models.ForeignKey(Commodity)
	def __unicode__(self):
		return '%s %s' %(self.OrderListDate, self.OrderListState)

class Comment(models.Model):
	CommentContent = models.TextField(blank=True)
	CustomerID = models.ForeignKey(Customer)
	CommodityID = models.ForeignKey(Commodity)
	def __unicode__(self):
		return self.CommentContent

class Cart(models.Model):
	CartDate = models.DateField()
	CustomerID = models.ForeignKey(Customer)
	CommodityID = models.ForeignKey(Commodity)
	CartCommodityAmount = models.IntegerField(blank=True, default=1)
	def __unicode__(self):
		return '%s %s' %(self.CartCommodityAmount, self.CartDate)

class Favorite(models.Model):
	FavoriteDate = models.DateField()
	CustomerID = models.ForeignKey(Customer)
	CommodityID = models.ForeignKey(Commodity)
	def __unicode__(self):
		return '%s' %(self.FavoriteDate)


class BlacklistCustomer(models.Model):
	BlacklistCustomerReason = models.TextField()
	AdministratorID = models.ForeignKey(Administrator)
	CustomerID = models.ForeignKey(Customer)
	def __unicode__(self):
		return self.BlacklistCustomerReason
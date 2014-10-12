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
		('J','Junior seller'),
		('I','Intermediate seller'),
		('S','Senior seller'),
	)
	SellerAccount = models.CharField(max_length=64)
	SellerPassword = models.CharField(max_length=16)
	SellerName = models.CharField(max_length=64)
	SellerType = models.CharField(max_length=1,choices=SellerTypeChoices,blank=True)
	SellerRealName = models.CharField(max_length=64)
	SellerRealID = models.IntegerField()
	SellerTelephone = models.CharField(max_length=64,blank=True)
	SellerEmail = models.EmailField(blank=True)
	def __unicode__(self):
		return '%s %s' %(self.SellerAccount,self.SellerName)

class Shop(models.Model):
	ShopDescription = models.TextField(blank=True)
	SellerID = models.ForeignKey(Seller)
	ShopName = models.CharField(max_length=64,blank=True)
	ShopState = models.BooleanField(blank=True)
	def __unicode__(self):
		return self.ShopName

class Advertisement(models.Model):
	AdvertisementTypeChoice=(
		('S','ShopAdvertisement'),
		('C','CommodityAdvertisement'),
	)
	AdvertisementAccount = models.CharField(max_length=64)
	ShopID = models.ForeignKey(Shop)
	Type = models.CharField(max_length=1,choices=AdvertisementTypeChoice)
	def __unicode__(self):
		return '%s %s' %(self.AdvertisementAccount, self.Type)

class Administrator(models.Model):
	AdministratorAccount = models.CharField(max_length=64)
	AdministratorName = models.CharField(max_length=64)
	AdministratorPassword = models.CharField(max_length=16)
	AdministratorTelephone = models.CharField(max_length=64,blank=True)
	AdministratorEmail = models.EmailField()
	def __unicode__(self):
		return self.AdministratorName

class System(models.Model):
	BulletinBoardContent = models.CharField(max_length=64,blank=True)
	BulletinBoardDescription = models.TextField(blank=True)
	BulletinBoardDate = models.DateField(blank=True)
	ComissionRate = models.FloatField(blank=True)
	def __unicode__(self):
		return '%s %s' %(self.BulletinBoardDate,self.BulletinBoardContent)

class BlacklistSeller(models.Model):
	BlacklistSellerReason = models.TextField(blank=True)
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
	ShopOrderState = models.CharField(max_length=64)
	ShopOrderDate = models.DateField()
	ShopID = models.ForeignKey(Shop)
	def __unicode__(self):
		return '%s %s' %(self.ShopOrderDate, self.ShopOrderState)

class Customer(models.Model):
	CustomerTypeChoices=(
		('J','Junior customer'),
		('I','Intermediate customer'),
		('S','Senior customer'),
	)
	CustomerAccount = models.CharField(max_length=64)
	CustomerName = models.CharField(max_length=64)
	CustomerPassword = models.CharField(max_length=16)
	CustomerType = models.CharField(max_length=1,choices=CustomerTypeChoices,blank=True)
	CustomerTelephone = models.CharField(max_length=64,blank=True)
	CustomerEmail = models.EmailField()
	CustomerAddress = models.TextField(blank=True)

	def __unicode__(self):
		return u'%s %s' %(self.CustomerAccount, self.CustomerName)

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
	#CommoditySecondType = models.IntegerField(blank=True)
	CommodityImage = models.ImageField(upload_to='images',max_length=255,blank=True,null=True)
	CommodityDiscount = models.FloatField(null=True,blank=True)
	ShopID = models.ForeignKey(Shop)
	def __unicode__(self):
		return '%s %s %s' %(self.CommodityName, self.CommodityType, self.CommodityAmount)

class OrderList(models.Model):
	OrderListAccount = models.CharField(max_length=64)
	OrderListState = models.CharField(max_length=64)
	OrderListDate = models.DateField()
	SellerID = models.ForeignKey(Seller)
	ShopID = models.ForeignKey(Shop)
	CustomerID = models.ForeignKey(Customer)
	CommodityID = models.ForeignKey(Commodity)
	def __unicode__(self):
		return '%s %s %s' %(self.OrderListAccount,self.OrderListDate, self.OrderListState)

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
	CartCommodityAccount = models.CharField(max_length=64,blank=True)
	def __unicode__(self):
		return '%s %s' %(self.CartCommodityAccount, self.CartDate)

class Favorite(models.Model):
	FavoriteDate = models.DateField()
	CustomerID = models.ForeignKey(Customer)
	CommodityID = models.ForeignKey(Commodity)
	def __unicode__(self):
		return '%s' %(self.FavoriteDate)

class CustomerOrder(models.Model):
	CustomerOrderState = models.CharField(max_length=64)
	CustomerOrderDate = models.DateField()
	CustomerID = models.ForeignKey(Customer)
	def __unicode__(self):
		return '%s %s' %(self.CustomerOrderState, self.CustomerOrderDate)

class NotificationCustomer(models.Model):
	NotificationContent = models.TextField()
	CustomerID = models.ForeignKey(Customer)
	SellerID = models.ForeignKey(Seller)
	def __unicode__(self):
		return self.NotificationContent

class BlacklistCustomer(models.Model):
	BlacklistCustomerReason = models.TextField()
	AdministratorID = models.ForeignKey(Administrator)
	CustomerID = models.ForeignKey(Customer)
	def __unicode__(self):
		return self.BlacklistCustomerReason
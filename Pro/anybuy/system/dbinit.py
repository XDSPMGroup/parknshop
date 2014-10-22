#encoding:utf-8
from system.models import *
import hashlib
Customer.objects.create(
	CustomerAccount = 'customer1', 
	CustomerName = 'customer1', 
	CustomerPassword = hashlib.md5('123456').hexdigest(), 
	CustomerTelephone = '11111111', 
	CustomerEmail = '111@qq.com', 
	CustomerAddress = 'far away')

Customer.objects.create(
	CustomerAccount = 'cccc', 
	CustomerName = 'ccc', 
	CustomerPassword = hashlib.md5('123456').hexdigest(), 
	CustomerTelephone = '11111111', 
	CustomerEmail = '111@qq.com', 
	CustomerAddress = 'far away')

Seller.objects.create(
	SellerAccount = 'Seller1', 
	SellerName = 'Seller1', 
	SellerPassword = hashlib.md5('123456').hexdigest(), 
	SellerTelephone = '11111111', 
	SellerEmail = '111@qq.com', 
	SellerAddress = 'far away')


HelpCenter.objects.create(
	HelpCenterName = 'hcname1', 
	HelpCenterContent = 'hccotent1')

Shop.objects.create(
	ShopDescription = 'ShopDescription1', 
	SellerID = Seller.objects.get(id=1), 
	ShopName = 'shopname1', 
	ShopState = 1)

#images/1.png
Commodity.objects.create(
	CommodityName = 'Commodity1', 
	CommodityDescription = 'This is Commodity1', 
	CommodityAmount = 100, 
	SoldAmount = 0, 
	PurchasePrice = 10, 
	SellPrice = 15, 
	CommodityType = 'C', 
	CommodityImage = 'images/1.png', 
	CommodityDiscount = 0.9, 
	ShopID = Shop.objects.get(id=1))

Administrator.objects.create(
	AdministratorAccount = 'aaaddd',
	AdministratorName = 'eric',
	AdministratorPassword = hashlib.md5('123456').hexdigest(), 
	AdministratorTelephone = '12121212',
	AdministratorEmail = 'sda@w.com')

ShopAdv.objects.create(
	ShopID = Shop.objects.get(id=1),
	OwnerID = Seller.objects.get(id=1),
	AdvertisementContent = 'This is shopadv')

CommodityAdv.objects.create(
	CommodityID = Commodity.objects.get(id=1),
	OwnerID = Seller.objects.get(id=1),
	AdvertisementContent = 'This is adv')

HomeShopAdv.objects.create(
	ShopID = Shop.objects.get(id=1),
	OwnerID = Administrator.objects.get(id=1),
	AdvertisementContent = 'This is adv')

HomeCommodityAdv.objects.create(
	CommodityID = Commodity.objects.get(id=1),
	OwnerID = Administrator.objects.get(id=1),
	AdvertisementContent = 'This is adv')

System.objects.create(
	BulletinBoardContent = 'This is BulletinBoardContent',
	BulletinBoardDescription = 'This is BulletinBoardDescription',
	BulletinBoardDate = '2014-10-17',
	ComissionRate = 0.01)
	
BlacklistSeller.objects.create(
	BlacklistSellerReason = 'yanchou',
	SellerID = Seller.objects.get(id=1),
	AdministratorID = Administrator.objects.get(id=1))

Discount.objects.create(
	DiscountRate = 0.9, 
	SellerID = Seller.objects.get(id=1), 
	ShopID = Shop.objects.get(id=1))

ShopOrder.objects.create(
	ShopOrderState = 0,
	ShopOrderDate = '2014-10-17',
	ShopID = Shop.objects.get(id=1))


CustomerOrder.objects.create(
	CustomerOrderState = '0',
	CustomerOrderDate = '2014-10-17',
	CustomerID = Customer.objects.get(id=1))

#订单状态：0-待付款，1-已付款待发货，2-待签收，
# 3-待评价，4-待退款，5-退款成功，6-卖家拒绝退款
OrderList.objects.create(
	OrderListState = 0,
	OrderListDate = '2014-10-17',
	#SellerID = Seller.objects.get(id=2),
	ShopOrderID = ShopOrder.objects.get(id=1),
	CustomerOrderID = CustomerOrder.objects.get(id=1),
	CommodityID = Commodity.objects.get(id=1))

Comment.objects.create(
	CommentContent = 'This is comment', 
	CustomerID = Customer.objects.get(id=1), 
	CommodityID = Commodity.objects.get(id=1))

Cart.objects.create(
	CartDate = '2014-10-17',
	CustomerID = Customer.objects.get(id=1),
	CommodityID = Commodity.objects.get(id=1),
	CartCommodityAmount = 1)

Favorite.objects.create(
	FavoriteDate = '2014-10-17',
	CustomerID = Customer.objects.get(id=1),
	CommodityID = Commodity.objects.get(id=1))
	

	
NotificationCustomer.objects.create(
	NotificationContent = 'well this is..')
	
BlacklistCustomer.objects.create(
	BlacklistCustomerReason = 'you dare',
	AdministratorID = Administrator.objects.get(id=1),
	CustomerID = Customer.objects.get(id=1))
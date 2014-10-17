from system.models import *

class Guest(object):
	"""docstring for Guest"""
	def __init__(self, arg):
		authority = 1 #用户权限(int,0-禁止登录,1-可登录)
		alive = 0#用户登录标识(int,0-Guset,1-Customer,2-Seller)
		Guest RegisterCustomer(Customer); 注册买家帐号,传入买家信息, 注册特定帐号, 写入数据库，返回基类引用。
		Guest RegisterSeller(Seller); 注册卖家帐号,传入卖家信息, 注册特定帐号, 写入数据库，返回基类引用。
			* int Login(integer,Account,Password); 登录帐号,根据标识选择买家/卖家登录，根据帐号密码进行登录，返回成功与否。
			* int RetrievePassword(integer,Account,Email); 
					找回密码,先验证身份(输入对应帐号与邮箱)。系统重置密码，新密码写入数据库，将新密码发送至邮箱。第一个参数表明身份为买家/卖家。
			* int ModifyPassword(Old,New); 修改密码,用于买家/卖家两个子类, 基类本身不用。用户填写旧密码与新密码，进行修改操作，写入数据库。
			* CommodityList SearchCommodity(String); 根据用户输入的字符串，搜索商品，返回商品列表。查看商品详情可以直接读取特定商品信息
			* Commodity GetCommodity(integer); 根据商品ID,返回特定商品。
			* StringList GetCommodityComments(integer); 获得商品评论,参数为CommodityID，内部调用Commodity类的API。返回商品评论列表。
			* int GetAlive(); 查看用户是否登录,返回登录标识
			* int GetAuthority(); 查看用户权限

Customer
			* CustomerID 买家编号
			* CustomerAccount 帐号(String)
			* CustomerPassword 密码
			* CustomerName 用户昵称(可修改)
			* authority 用户权限(int,0-禁止登录,1-可登录) (继承自Guest)
			* alive 用户登录标识(int,0-Guset,1-Customer,2-Seller) (继承自Guest)
			* CustomerTelephone 电话
			* CustomerEmail 邮件地址
			* CustomerAddress 默认邮寄地址
			* CustomerOrderList 买家订单列表
			* int ModifyBasicInfo(Customer ); 修改基本信息，用户昵称，电话，邮件，邮寄地址。返回成功与否。
			* int ModifyPassword(Sting Old,String New); 修改密码
					参数为旧密码与新密码，先匹配旧密码，旧密码匹配成功则修改新密码至数据库。修改成功返回1.失败返回0.
			* int CustomerInit(); 买家对象初始化。根据Account的值，从数据库中检索出对应信息，实现对象的初始化。  
			* int DeleteOrder(integer); 删除订单,根据OrderID删除对应订单。返回成功与否。
			* int PayOrder(integer); 确认订单付款.
			* int Refund(integer); 申请订单退款
			* int CommentOrder(integer); 评论订单商品，传入OrderID, 依次对每个商品进行评论。
			* int CommentCommodity(integer CommodityID,String comment); 评论特定商品。返回成功与否。
			* integer GenerateOrder(); 生成订单(根据购物车),添加新订单至CustomerOrderList, 并返回新OrderID.
			* int Logout(); 用户登出.返回成功与否。
			* 类图备注：Cart & Favorite均为Customer的内部类。
		2. Seller
			* SellerID 卖家编号
			* SellerAccount 帐号
			* SellerPassword 密码
			* authority 用户权限(int,0-禁止登录,1-可登录) (继承自Guest)
			* alive 用户登录标识(int,0-Guset,1-Customer,2-Seller) (继承自Guest)
			* SellerName 用户昵称
			* SellerRealName 卖家实名
			* SellerRealID 身份证号
			* SellerTelephone 电话
			* SellerEmail 邮件地址
			* ShopList 店铺列表
			* Shop GetShop(integer); 进入具体店铺
			* int ApplyNewShop(Shop); 申请新店铺,用户填写申请表，写入基本店铺信息，生成new Shop, 店铺状态为待审核。返回申请提交成功与否。
			* int ModifyPassword(Sting Old,String New); 修改密码
					参数为旧密码与新密码，先匹配旧密码，旧密码匹配成功则修改新密码至数据库。修改成功返回1.失败返回0.
			* int ModifyBasicInfo(Seller); 修改基本信息，用户昵称，电话，邮件等。返回成功与否。
			* void Logout(); 用户登出

			Administrator
			* AdministratorID 管理员ID编号
			* AdministratorAccount 管理员帐号
			* AdministratorPassword 管理员密码
			* AdministratorName 管理员昵称
			* AdministratorTelephone 管理员电话
			* AdministratorEmail 管理员邮件
			* Advertisement 广告
			* SellerBlackList 卖家黑名单
			* CustomerBlackList 买家黑名单
			* OrderList GetOrderList(); 获得所有订单以查看销售历史。并计算出每一笔交易的佣金。
			* Order GetOrder(integer OrderID); 获得特定订单
			* int Login(Account, Password); 管理员登录
			* int BackupDB(); 备份数据库
			* int RestoreDB(); 恢复数据库
			* ShopList DealShopApply(); 处理店铺申请,从数据库中选择所有店铺状态为’待审核’的店铺。
			* int PassApply(ShopID); 审核通过
			* int RejectApply(ShopID); 审核不通过 
			* int BlacklistCustomer(integer CustomerID); 拉黑用户, 参数为用户ID
			* int BlacklistSeller(integer SellerID);
			* GuestList GetBlacklist(); 查看黑名单信息,返回账户列表。
			* int RestoreCustomer(integer CustomerID); 恢复帐号
			* int RestoreSeller(integer SellerID); 恢复帐号
			* int DeleteCustomer(integer CustomerID); 删除帐号
			* int DeleteSeller(integer SellerID); 删除帐号
			* int SetAd(Advertisement Ad); 配置主页广告

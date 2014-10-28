
## Programmer 29 Oct.前的任务

任务 | 详情 | html文件 | url | status
----|-----|----------|----- | ---
entershop|查看商品list、（entershop上面显示店铺广告，下面显示shop的广告）| |url:/seller/ | done
管理shop|添加修改（包括折扣）商品页面|manageCommodity.html| url:/seller/modify |
管理广告|改成选择商品和店铺（广告显示在entershop页面）|：manageAD.html |/seller/ad |
管理订单|把action里面的按钮改成一个confirm，confirm之后状态改为shipping |用favorite页面|/seller/order |
statistics|查看销售记录|checksaleshistory.html|/seller/statistics
refund|查看退款：refund 页面全部设置初值为refuse，右下角添加一个提交按钮 ||/seller/refund
apply|申请shop：申请之后在下面弹出一句话：congratulations|applyshop| url/myshop/applyshop

1、2、3李爽，4、5王腾，6、7寇苗娟

1. logout->homepage 
2. help center(TA)做一个静态页面 done
3. sellerbase!! done
4. 顾客注册成功之后进入homepage，卖家注册成功之后进入entershop
5. refund+comment
6. 查看顾客历史订单（王腾）
7. check out 

#Instruction
- Write class Order, Cart, Favorate in ./container
- Write class store, Adv, commodity in ./store
- Write class system_class, admin_class in ./system
- Write class Guset, Customer, Seller in ./account

#Due
Task	| Deadline | Programmer
----	| -----|-----
Model	| Oct 13 | 王腾
URL | Oct 14 | 李爽
store classes | Oct 14 | 李爽
container classes | Oct 16 | 王腾，寇苗娟
system classes | Oct 16 | 陈文康，曹兵
account classes | Oct 20 | 李爽，郭枭鹏
Guest views | Oct 21 | 李爽
Customer views | Oct 27 | 陈文康，曹冰
Seller views | Oct 27 | 寇苗娟，王腾
Admin views | Oct 24 | 郭枭鹏，李爽

#PS: 
Reference book: [Beginning Django e-commerce](http://pan.baidu.com/s/1mgDmHpY)

You need to install Python Imaging Library 

    cd parknshop/Pro/anybuy/files/framework/Imaging-1.1.7
    python setup.py install


关于图片，存在file/img目录下然后通过下面的形式访问：

    <img src="/file/{{msg.imageurl}}"</img>

css/js, saved in base_template:

     <link href="/base_template/css/style.css" rel="stylesheet">

setup Django REST framework to implement RESTful web service

    cd parknshop/Pro/anybuy/files/framework/djangorestframework-0.3.2
    python setup.py install 
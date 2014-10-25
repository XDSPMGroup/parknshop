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
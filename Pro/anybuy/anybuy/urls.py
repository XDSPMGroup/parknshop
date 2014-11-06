#coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from anybuy import settings
#from account.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anybuy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^help_center/$', 'store.views.helpcenter'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'^index/$', 'account.views.index',name = 'index'),
    url(r'^$', 'account.views.index'),
    url(r'^register/$','account.views.register', name = 'register'),
    url(r'^addshop/$', 'store.views.add_and_modify_shop'),
    url(r'^login/$','account.views.login',name = 'login'),
    url(r'^logout/$','account.views.logout' ,name = 'logout'),
    url(r'^search/(?P<keyword>\w*)/$', 'store.views.search'),
    url(r'^myinfo/$', 'account.views.info'),
    url(r'^commodity/id/(?P<cid>\d*)/$', 'store.views.getCommodity'),
    url(r'^file/(?P<path>.*)','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^base_template/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
    url(r'^shop/id/(?P<cid>\d*)/$', 'store.views.getShop'),
    url(r'^favorite/$', 'store.views.favorite'),
    url(r'^cart/$', 'store.views.cart'),
    url(r'^addtocart/(?P<cid>\d*)/(?P<amount>\d*)/(?P<source>\w*)', 'store.views.add_to_cart'),
    url(r'^addtofavorite/$', 'store.views.add_to_favorite'),
    url(r'^rmfromcart/$', 'store.views.rm_from_cart'),
    url(r'^refreshcart/$', 'store.views.refreshcart'),
    url(r'^rmfromfavorite/$', 'store.views.rm_from_favorite'),
    url(r'^customer/statistics/(?P<time>.*)$', 'store.views.buysHistory'),  
    url(r'^customer/order/$', 'store.views.manageOrder'), 
    url(r'^apply_refund/$', 'store.views.apply_refund'), 
    url(r'^add_comment/$', 'store.views.add_comment'), 
    url(r'^seller/statistics/(?P<time>.*)$', 'account.views.salesHistory'),  
    url(r'^seller/home/$', 'store.views.sellerentershop'),
    url(r'^seller/order/$', 'account.views.checkOrder'),
    url(r'^seller/refund/$', 'account.views.refund'),
    url(r'^seller/ad/$', 'store.views.manageAD'),
    url(r'^seller/changead/$', 'store.views.changead'),
    url(r'^seller/delete/(?P<cid>\d*)', 'store.views.delfromshop'),
    url(r'^removeOrderList/$', 'account.views.removeOrderList'),
    url(r'^checkout/$', 'store.views.checkoutcart'),
    url(r'^bank/$', 'store.views.bank'),
    url(r'^modifyOrderList1/$', 'account.views.modifyOrderList1'),
    url(r'^modifyOrderList2/$', 'account.views.modifyOrderList2'),
    url(r'^seller/ad/$', 'store.views.manageAD'),
    url(r'^seller/changead/$', 'store.views.changead'),
    url(r'^seller/modify/(?P<cid>\d*)/$', 'store.views.add_and_modify'), #cid==0时添加新项目， !=0时修改cid的项目
    #url(r'^account/$', views.register, name='register'),
    #url(r'^account/register/$',views.register, name = 'register'),
)

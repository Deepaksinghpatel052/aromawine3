"""aromawine3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_login
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django_filters.views import FilterView
from admin_manage_products.models import AwProductPrice

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('superadmin/', admin.site.urls),
    path('admin', include('admin_dashboard.urls')),
    # path('admin/dashboard', include(('admin_dashboard.urls','admin_dashboard'),namespace='admin_dashboard')),
    path('admin/dashboard/', include(('admin_dashboard.urls','admin_dashboard'),namespace='admin_dashboard')),

    path('admin/producer/', include(('admin_manage_producer.urls','admin_manage_producer'),namespace='admin_manage_producer')),
    # path('admin/producer/', include(('admin_manage_producer.urls','admin_manage_producer'),namespace='admin_manage_producer')),

    path('admin/color/', include(('admin_manage_color.urls','admin_manage_color'),namespace='admin_manage_color')),

    # ------------------------------------------------------------------------------------------------------------------
    path('admin/admin-manage-order/', include(('admin_manage_order.urls','admin_manage_order'),namespace='admin_manage_order')),
    # ==================================================================================================================
    path('admin/country/', include(('admin_manage_country.urls','admin_manage_country'),namespace='admin_manage_country')),

    path('admin/appellation/', include(('admin_manage_appellation.urls','admin_manage_appellation'),namespace='admin_manage_appellation')),

    path('admin/size/', include(('admin_manage_size.urls','admin_manage_size'),namespace='admin_manage_size')),

    path('admin/classification/', include(('admin_manage_classification.urls','admin_manage_classification'),namespace='admin_manage_classification')),

    path('admin/vintages/', include(('admin_manage_Vintages.urls','admin_manage_Vintages'),namespace='admin_manage_Vintages')),

    path('admin/varietals/', include(('admin_manage_varietals.urls','admin_manage_varietals'),namespace='admin_manage_varietals')),

    path('admin/region/', include(('admin_manage_region.urls','admin_manage_region'),namespace='admin_manage_region')),

    path('admin/grape/', include(('admin_manage_grape.urls','admin_manage_grape'),namespace='admin_manage_grape')),

    path('admin/products/', include(('admin_manage_products.urls','admin_manage_products'),namespace='admin_manage_products')),


    path('admin/categoryes/', include(('admin_manage_categoryes.urls','admin_manage_categoryes'),namespace='admin_manage_categoryes')),
    # path('admin/categoryes/', include(('admin_manage_categoryes.urls','admin_manage_categoryes'),namespace='admin_manage_categoryes')),

    path('admin/banners/', include(('admin_manage_banners.urls','admin_manage_banners'),namespace='admin_manage_banners')),
    # path('admin/categoryes/', include(('admin_manage_banners.urls','admin_manage_banners'),namespace='admin_manage_banners')),

    # path('admin/login', include(('account.urls','account'),namespace='account')),
    path('logout', auth_login.LogoutView.as_view() ,name="logout"),
    path('admin/login/', auth_login.LoginView.as_view(template_name='admin/login/index.html')),
    path('accounts/login/', auth_login.LoginView.as_view(template_name='admin/login/index.html')),
    path('admin/manage-custom-page/', include(('admin_manage_content_page.urls','admin_manage_content_page'),namespace='admin_manage_content_page')),

    path('summernote/', include('django_summernote.urls')),


    # ====================================set url for web frentend START==============================================
    path('', include(('home.urls','home'),namespace='home')),
    path('<slug:product_id>/product-detail/<slug:product_slug>/<slug:vintage_year>', include(('product_detail.urls','product_detail'),namespace='product_detail')),
    path('shop/', include(('wine_shop.urls','wine_shop'),namespace='wine_shop')),
    # path('shop/<slug:short_by>/', include(('wine_shop.urls','wine_shop'),namespace='wine_shop')),

    path('filters', FilterView.as_view(model=AwProductPrice)),

    path('', include('django.contrib.auth.urls')),

    path('account/', include(('account.urls','account'),namespace='account')),
    path('page/', include(('pages.urls','pages'),namespace='pages')),


    path('user/orders/', include(('orders.urls','orders'),namespace='orders')),
    path('user/dashboard/', include(('dashboard_user.urls','dashboard_user'),namespace='dashboard_user')),
    path('user/addressbook/', include(('addressbook_user.urls','addressbook_user'),namespace='addressbook_user')),
    path('user/profile/', include(('profile_user.urls','profile_user'),namespace='profile_user')),
    # ====================================set url for web frentend END==============================================

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

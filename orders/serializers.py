from rest_framework import serializers
from django.contrib.auth.models import User
from admin_manage_products.models import AwProductPrice,AwProducts,AwProductImage
from orders.models import AwAddToCard,AwAddToCard,AwOrders,AwOrederItem
from django.shortcuts import get_object_or_404
from rest_framework import  exceptions
from admin_manage_cupon_code.models import AwCuponCode
from datetime import datetime
from datetime import date
from admin_manage_setting.models import AwManageShipping



class AwOrederItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = AwOrederItem
        fields = '__all__'
        depth = 2

class AwOrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model = AwOrders
        fields = '__all__'
        depth = 2



class AwManageShippingSerializers(serializers.ModelSerializer):
    class Meta:
        model = AwManageShipping
        fields = ('id', 'Country', 'min_ordr_amount', 'Shiping_Fees_min_order_amount', 'Create_date', 'Created_by')


class ProductPriceSeriSerializer(serializers.ModelSerializer):
    class Meta:
        model =  AwProductPrice
        fields = ('id', 'Product','Vintage_Year','Bottle', 'Retail_Cost','Retail_Stock', 'Descount_Cost' ,'Duty','GST','Bond_Cost','Bond_Stock','Bond_Descount_Cost','Other_info','Created_by','Created_date','Updated_by','Updated_date')



class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    parent_id = serializers.PrimaryKeyRelatedField(queryset=AwProducts.objects.all(), source='AwAddToCard.Product.id')

    class Meta:
        model = AwProductImage
        fields = ('id', 'Image_Type', 'Image', 'Product','parent_id')

    def create(self, validated_data):
        subject = AwProductImage.objects.create(Product=validated_data['AwAddToCard']['Product']['id'], Image_Type=validated_data['Type'])
        return child




class AwAddToCardSerializer(serializers.ModelSerializer):
    class Meta:
        model =  AwAddToCard
        fields = ('id', 'User','Cookies_id','Order_Type', 'Product_Cellar','Product_Delivered', 'order_item_id' ,'Event_Ticket','Event_Ticket','Year','Type','Old_Cost','Case_Formate','Quentity','Date')
        depth = 2




class CheckCouponCodeSerializers(serializers.Serializer):
    coupon_code = serializers.CharField(style={"inpupt_type": "text"}, write_only=True, required=True, allow_blank=True)

    def validate(self, data):
        status = 0
        message = "Check coupon"
        datat = {}
        data['status'] = status
        data['message'] = message

        coupon_code = data.get("coupon_code", "")
        if coupon_code !="":
            if AwCuponCode.objects.filter(CouponCode=coupon_code).exists():
                get_code_ins = get_object_or_404(AwCuponCode,CouponCode=coupon_code)
                if get_code_ins.Valid_from <= datetime.today().date():
                    if get_code_ins.Valid_to >= datetime.today().date():
                        status = "1"
                        data["type"] = get_code_ins.Type
                        data["count"] = get_code_ins.Amount
                        data['status'] = 1
                        data['message'] = "Coupon Code is applicbel."

                    else:
                        mes = "coupon_code expayer."
                        raise exceptions.ValidationError(mes)
                else:
                    mes = "This code is not usefull at this time."
                    raise exceptions.ValidationError(mes)
            else:
                mes = "coupon_code is reqired."
                raise exceptions.ValidationError(mes)
        else:
            mes = "coupon_code is incorrect."
            raise exceptions.ValidationError(mes)
        return data

class CookiesToUserIdValidetorSerializers(serializers.Serializer):
    User_id = serializers.CharField(style={"inpupt_type": "text"}, write_only=True, required=True, allow_blank=True)
    Cookies_id = serializers.CharField(style={"inpupt_type": "text"}, write_only=True, required=True, allow_blank=True)

    def validate(self, data):
        datat = {"status":0,"message":""}
        User_id = data.get("User_id", "")
        Cookies_id = data.get("Cookies_id", "")
        if User.objects.filter(id=User_id):
            get_user_ins = get_object_or_404(User, id=User_id)
            if AwAddToCard.objects.filter(Cookies_id=Cookies_id).exists():
                AwAddToCard.objects.filter(Cookies_id=Cookies_id).update(User=get_user_ins)
                data['status'] = 1
                data['message'] = "User_id update with cookies."
            else:
                mes = "Your Cookies_id is incorrect."
                raise exceptions.ValidationError(mes)
        else:
            mes = "Your User_id is incorrect."
            raise exceptions.ValidationError(mes)
        return data

class GetAddToCartProductVarifiedSerializers(serializers.Serializer):
    User_id = serializers.CharField(style={"inpupt_type": "text"}, write_only=True, required=False, allow_blank=True)
    Cookies_id = serializers.CharField(style={"inpupt_type": "text"}, write_only=True, required=False, allow_blank=True)

    def validate(self, data):
        User_id = data.get("User_id", "")
        Cookies_id = data.get("Cookies_id", "")
        data= {}
        if User_id != "":
            if User.objects.filter(id=User_id):
                get_user_ins = get_object_or_404(User,id=User_id)
                data["user_ins"] = get_user_ins
                data["Cookies_id"] = ""
            else:
                mes = "Your User_id is incorrect."
                raise exceptions.ValidationError(mes)
        elif Cookies_id != "":
            if AwAddToCard.objects.filter(Cookies_id=Cookies_id).exists():
                data["user_ins"] = ""
                data["Cookies_id"] = Cookies_id
            else:
                mes = "Your Cookies_id is incorrect."
                raise exceptions.ValidationError(mes)
        else:
            mes = "User_id/Cookies_id is reqired."
            raise exceptions.ValidationError(mes)
        return data


class GetidvalidationAPI(serializers.Serializer):
    user_ins = serializers.CharField(style={"inpupt_type": "text"}, write_only=True, required=False, allow_blank=True)

    def validate(self, data):

        user_id = data.get("user_ins", "")

        User_id_data = None
        if user_id:
            if User.objects.filter(id=user_id).exists():
                User_id_data = get_object_or_404(User, id=user_id)
                # User_id_data = User.objects.get(id=user_id)
            else:
                mes = "id is incorrect "
                raise exceptions.ValidationError(mes)
        else:
            User_id_data = ""
        return User_id_data




class AwAddToCardSerializer(serializers.ModelSerializer):

    AwProductImage_Product = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model =  AwAddToCard
        fields = ('id','User','Order_Type','Product_Cellar','Product_Delivered','Case_Formate','Event_Ticket','Year','Type','Old_Cost','Case_Formate','Quentity','Date','AwProductImage_Product')
        depth = 3
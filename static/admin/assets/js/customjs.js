$(document).ready(function(){


var geturl = window.location.href;
var url_in_array = geturl.split("/");
var page_name = "";


if(jQuery.inArray("categoryes", url_in_array) != -1 && jQuery.inArray("add-categoryes", url_in_array) == -1)
{
	$("#Manage_Categoryes").addClass("active_dsp");
	$("#Category").addClass("active");
}

if(jQuery.inArray("add-categoryes", url_in_array) != -1)
{
	$("#Add_Categoryes").addClass("active_dsp");
	$("#Category").addClass("active");
}


if(jQuery.inArray("products", url_in_array) != -1 && jQuery.inArray("add-product", url_in_array) == -1)
{
	$("#Manage_Product").addClass("active_dsp");
	$("#Products").addClass("active");
}

if(jQuery.inArray("add-product", url_in_array) != -1)
{
	$("#Add_Product").addClass("active_dsp");
	$("#Products").addClass("active");
}






if(jQuery.inArray("settings", url_in_array) != -1 && jQuery.inArray("fee-shipping", url_in_array) == -1)
{
	$("#General_Setting").addClass("active_dsp");
	$("#Setting").addClass("active");
}

if(jQuery.inArray("fee-shipping", url_in_array) != -1)
{
	$("#Manage_Shipping").addClass("active_dsp");
	$("#Setting").addClass("active");
}







if(jQuery.inArray("banners", url_in_array) != -1 && jQuery.inArray("add-banner", url_in_array) == -1)
{
	$("#Manage_Banner").addClass("active_dsp");
	$("#Banner").addClass("active");
}

if(jQuery.inArray("add-banner", url_in_array) != -1)
{
	$("#Add_Banner").addClass("active_dsp");
	$("#Banner").addClass("active");
}








if(jQuery.inArray("manage-event", url_in_array) != -1 && jQuery.inArray("add-event", url_in_array) == -1)
{
	$("#Manage_Event").addClass("active_dsp");
	$("#Event").addClass("active");
}

if(jQuery.inArray("add-event", url_in_array) != -1)
{
	$("#Add_Event").addClass("active_dsp");
	$("#Event").addClass("active");
}


// =====================Recipes styart=============
if(jQuery.inArray("wine-recipes", url_in_array) != -1 && jQuery.inArray("add-recipe", url_in_array) == -1)
{
	$("#Manage_Recipes").addClass("active_dsp");
	$("#Recipes").addClass("active");
}

if(jQuery.inArray("add-recipe", url_in_array) != -1)
{
	$("#Add_Recipe").addClass("active_dsp");
	$("#Recipes").addClass("active");
}
// =====================Recipes end=============





if(jQuery.inArray("dinner", url_in_array) != -1 && jQuery.inArray("add-dinner", url_in_array) == -1)
{
	$("#Manage_Dinner").addClass("active_dsp");
	$("#Dinner").addClass("active");
}

if(jQuery.inArray("add-dinner", url_in_array) != -1)
{
	$("#Add_Dinner").addClass("active_dsp");
	$("#Dinner").addClass("active");
}



if(jQuery.inArray("manage-wine-testing", url_in_array) != -1 && jQuery.inArray("add-testing-wine", url_in_array) == -1)
{
	$("#Manage_Wine_Testing").addClass("active_dsp");
	$("#Wine_Testing").addClass("active");
}

if(jQuery.inArray("add-testing-wine", url_in_array) != -1)
{
	$("#Add_Wine_Testing").addClass("active_dsp");
	$("#Wine_Testing").addClass("active");
}




if(jQuery.inArray("manage-order", url_in_array) != -1 && jQuery.inArray("refunded", url_in_array) == -1 && jQuery.inArray("cancelled", url_in_array) == -1 && jQuery.inArray("failled", url_in_array) == -1 && jQuery.inArray("active", url_in_array) == -1 && jQuery.inArray("caller", url_in_array) == -1 && jQuery.inArray("delivery", url_in_array) == -1 && jQuery.inArray("complete", url_in_array) == -1)
{
	$("#Manage_Orders").addClass("active_dsp");
	$("#Orders").addClass("active");
}

if(jQuery.inArray("edit-order", url_in_array) != -1 && jQuery.inArray("refunded", url_in_array) == -1 && jQuery.inArray("cancelled", url_in_array) == -1 && jQuery.inArray("failled", url_in_array) == -1 && jQuery.inArray("caller", url_in_array) == -1 && jQuery.inArray("delivery", url_in_array) == -1 && jQuery.inArray("complete", url_in_array) == -1)
{
	$("#Manage_Orders").addClass("active_dsp");
	$("#Orders").addClass("active");
}

if(jQuery.inArray("caller", url_in_array) != -1)
{
	$("#Caller_Orders").addClass("active_dsp");
	$("#Orders").addClass("active");
}

if(jQuery.inArray("delivery", url_in_array) != -1)
{
	$("#Delivery_Orders").addClass("active_dsp");
	$("#Orders").addClass("active");
}


if(jQuery.inArray("refunded", url_in_array) != -1)
{
	$("#Refunded_Orders").addClass("active_dsp");
	$("#Orders").addClass("active");
}
if(jQuery.inArray("cancelled", url_in_array) != -1)
{
	$("#Cancelled_orders").addClass("active_dsp");
	$("#Orders").addClass("active");
}

if(jQuery.inArray("failled", url_in_array) != -1)
{
	$("#Failled_orders").addClass("active_dsp");
	$("#Orders").addClass("active");
}

if(jQuery.inArray("complete", url_in_array) != -1)
{
	$("#Complete_Orders").addClass("active_dsp");
	$("#Orders").addClass("active");
}



if(jQuery.inArray("region", url_in_array) != -1 && jQuery.inArray("add-region", url_in_array) == -1)
{
	$("#Manage_Region").addClass("active_dsp");
	$("#Region").addClass("active");
}

if(jQuery.inArray("add-region", url_in_array) != -1)
{
	$("#Add_Region").addClass("active_dsp");
	$("#Region").addClass("active");
}



if(jQuery.inArray("coupons", url_in_array) != -1 && jQuery.inArray("add-coupon", url_in_array) == -1)
{
	$("#Manage_Coupons").addClass("active_dsp");
	$("#Coupons").addClass("active");
}

if(jQuery.inArray("add-coupon", url_in_array) != -1)
{
	$("#Add_Coupon").addClass("active_dsp");
	$("#Coupons").addClass("active");
}





if(jQuery.inArray("country", url_in_array) != -1 && jQuery.inArray("add-country", url_in_array) == -1)
{
	$("#Manage_Countries").addClass("active_dsp");
	$("#Countries").addClass("active");
}

if(jQuery.inArray("add-country", url_in_array) != -1)
{
	$("#Add_Countries").addClass("active_dsp");
	$("#Countries").addClass("active");
}





if(jQuery.inArray("grape", url_in_array) != -1 && jQuery.inArray("add-grape", url_in_array) == -1)
{
	$("#Manage_Grape").addClass("active_dsp");
	$("#Grape").addClass("active");
}

if(jQuery.inArray("add-grape", url_in_array) != -1)
{
	$("#Add_Grape").addClass("active_dsp");
	$("#Grape").addClass("active");
}


if(jQuery.inArray("manage-custom-page", url_in_array) != -1 && jQuery.inArray("add-page", url_in_array) == -1)
{
	$("#Mange_Pages").addClass("active_dsp");
	$("#Manage_Content").addClass("active");
}

if(jQuery.inArray("add-page", url_in_array) != -1)
{
	$("#Add_Page").addClass("active_dsp");
	$("#Manage_Content").addClass("active");
}




if(jQuery.inArray("producer", url_in_array) != -1 || jQuery.inArray("add-producer", url_in_array) != -1)
{
	$("#Producer_Winery").addClass("active_dsp");
	$("#Manage_Filtters").addClass("active");
}





if(jQuery.inArray("appellation", url_in_array) != -1)
{
	$("#Manage_Appellation").addClass("active_dsp");
	$("#Manage_Filtters").addClass("active");
}



if(jQuery.inArray("color", url_in_array) != -1)
{
	$("#Color").addClass("active_dsp");
	$("#Manage_Filtters").addClass("active");
}

if(jQuery.inArray("customer", url_in_array) != -1)
{
	$("#Customer").addClass("active_dsp");
	$("#Manage_Customer").addClass("active");
}


if(jQuery.inArray("size", url_in_array) != -1)
{
	$("#Bottle_Size").addClass("active_dsp");
	$("#Manage_Filtters").addClass("active");
}


if(jQuery.inArray("classification", url_in_array) != -1)
{
	$("#Classification").addClass("active_dsp");
	$("#Manage_Filtters").addClass("active");
}


if(jQuery.inArray("varietals", url_in_array) != -1)
{
	$("#Varietals").addClass("active_dsp");
	$("#Manage_Filtters").addClass("active");
}

if(jQuery.inArray("vintages", url_in_array) != -1)
{
	$("#Vintages").addClass("active_dsp");
	$("#Manage_Filtters").addClass("active");
}

});
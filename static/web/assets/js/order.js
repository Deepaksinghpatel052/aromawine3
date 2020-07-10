
$(document).on('click',".add_to_card",function(){

var product_id = $(this).data("product_id");
var cost_type = $(this).data("cost_type");
var case_formate = $("#case_formate_"+cost_type).val();
var quentity = $("#quentyti_"+cost_type).val();
var product_year = $("#product_year").val();
var add_to_card_url = $("#add_to_card_url").val();

$.ajax({
   method:"POST",
   url:add_to_card_url,
   data:{'product_id':product_id,'Year':product_year,'Type':cost_type,'Case_Formate_id':case_formate,'Quentity_set':quentity},
   dataType:"json",
   success:function(data){
    get_card_product();
      if(data.status == "0")
      {
      	swal({
            title: data.message,
            icon: "error",
            buttons: true,
            dangerMode: true,
          });
      }
      else
      {
        swal({
            title: data.message,
            icon: "success",
            buttons: true,
            dangerMode: true,
          });
      	
      }
   }
   });


});



$(document).on('change','.select_case_formate',function(){
var product_id = $("#product_id").val();
var product_year = $("#product_year").val();
var get_product_price_page = $("#get_product_price_page").val();
var type = $(this).data('type');
var format_id = $(this).val();

$.ajax({
   method:"POST",
   url:get_product_price_page,
   data:{'format_id':format_id},
   dataType:"json",
   success:function(data){
     var price_for_retail = data.data.Retail_Cost;
     var quentity_for_retail = data.data.Retail_Stock;
     var price_for_bond = data.data.Bond_Cost;
     var quentity_for_bond = data.data.Bond_Stock;
     
     if(type=="Bond")
     {
       var set_quntity = '';
       for(var i=1; i<=quentity_for_bond; i++)
       {
       	 set_quntity +='<option>'+i+'</option>';
       }
     	$("#quentyti_Bond").html(set_quntity);
     	$("#set_price_for_bond").text("$"+price_for_bond);
     	if(quentity_for_bond == 0 || price_for_bond == 0 )
     	{
     		$("#Bond_buy").prop( "disabled", true );
     	}
     	else
     	{
     		$("#Bond_buy").prop( "disabled", false );
     	}
     }
     if(type=="Retail")
     {
     	var set_quntity = '';
       for(var i=1; i<=quentity_for_retail; i++)
       {
       	 set_quntity +='<option>'+i+'</option>';
       }
     	$("#quentyti_Retail").html(set_quntity);
     	$("#set_price_for_retail").text("$"+price_for_retail);
     	if(quentity_for_retail == 0 || price_for_retail == 0)
     	{
     		$("#Retail_buy").prop( "disabled", true );
     	}
     	else
     	{
     		$("#Retail_buy").prop( "disabled", false );
     	}
     }
     
     
   }
});

});



$(document).ready(function(){
  get_card_product();
})



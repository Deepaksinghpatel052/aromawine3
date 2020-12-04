

var API_BASE_URL = 'https://sandbox-api.liv-ex.com/';
var CLIENT_KEY_set = '52fbdab1-9145-4fe9-8a93-27c70bd7577a';
var CLIENT_SECRET_set = '5YcyXPEj';
var base_url = "http://3.133.12.113/";

$(document).on('click','#run_lwine_code',function(){


			  	$("#show_error_message_Category_not_avelabel").text('');
			  	$("#show_error_message_Appellation_not_avelabel").text('');
			  	$("#show_error_message_Bottel_Size_Not_avelabel").text('');
			  	$("#show_error_message_Varietals_not_Avelabel").text('');
			  	$("#show_error_message_Grape_not_avelabel").text('');


 $(".se-pre-con").css("display","block");
var lwine_code  = $("#id_LWineCode").val();

if(lwine_code)
{
	if(lwine_code.length == 7)
    {
    	

    	var settings = {
			  "url": API_BASE_URL+"lwin/view/v1/lwinView",
			  "method": "POST",
			  "timeout": 0,
			  "headers": {
			    "CLIENT_KEY": CLIENT_KEY_set,
			    "CLIENT_SECRET": CLIENT_SECRET_set,
			    "ACCEPT": "application/json",
			    "CONTENT-TYPE": "application/json"
			  },
			  "data": JSON.stringify({"lwin":lwine_code,"includeVintageListing":false}),
			};

			$.ajax(settings).done(function (response) {
			  console.log("=================");
			  console.log(response);
			  console.log(response.lwinView);
			  
			  if(response.lwinView.errors)
			  {
				  	swal({
	            		title: 'Error: '+response.lwinView.errors.error[0].code+"! "+response.lwinView.errors.error[0].message,
	            		icon: "warning",
	            		buttons: true,
	            		dangerMode: true,
	          		});
			 
			  }
			  else
			  {

			  	$("#show_error_message_Category_not_avelabel").text('Category is not provided by Lwine API.');
			  	$("#show_error_message_Appellation_not_avelabel").text('Appellation is not provided by Lwine API.');
			  	$("#show_error_message_Bottel_Size_Not_avelabel").text('Bottel Size is not provided by Lwine API.');
			  	$("#show_error_message_Varietals_not_Avelabel").text('Varietals is not provided by Lwine API.');
			  	$("#show_error_message_Grape_not_avelabel").text('Grape is not provided by Lwine API.');
			  	$("#id_Product_name").val(response.lwinView[0].wine);
			  	// .attr("selected","selected")
			  	$('select[name="Select_Type"] option').each(function(){
			  		if($(this).text()==response.lwinView[0].type)
			  		{
			  			$(this).attr("selected","selected");
			  		}
			  	});
// ==========================================================================

			  	var producte_status = false;
			  	$("#show_error_message_Producer_not_avelabel").text('');
			  	$('select[name="Producer"] option').each(function(){
			  		if($(this).text()==response.lwinView[0].producerName)
			  		{
			  			producte_status = true;
			  			$(this).attr("selected","selected");
			  		}
			  	});

			  	if(!producte_status)
			  	{
			  		$("#show_error_message_Producer_not_avelabel").text("Producer '"+response.lwinView[0].producerName+"' is not in dropdown.");
			  	
			  	}
			  	
// =========================================================================================
				var color_status = false;
				$("#show_error_message_Color_not_avelabel").text('');
			  	$('select[name="Color"] option').each(function(){
			  		if($(this).text()==response.lwinView[0].colour)
			  		{
			  			color_status = true;
			  			$(this).attr("selected","selected");
			  		}
			  	});
			  	if(!color_status)
			  	{
			  		$("#show_error_message_Color_not_avelabel").text("Color '"+response.lwinView[0].colour+"' is not in dropdown.");
			  	
			  	}
// ===================================================================
			  	// $('select[name="Classification"] option').each(function(){
			  	// 	if(response.lwinView[0].classification.indexOf($(this).text()) != 1)
			  	// 	{
			  	// 		$(this).attr("selected","selected");
			  	// 	}
			  	// });
             
            var selected_year = response.lwinView[0].vintageValues;
               $.ajax({
		             method:"POST",
		             url:base_url+"admin/products/get-product-vintage",
		             data:{"selected_year":selected_year},
		             dataType:'html',
		             success:function(data)
		             {
		             	$(".vintage_year_ajax").html(data);
		             }
		         });
// =============================================================================
           var country_status = false;
           $("#show_error_message_Country_not_avelabel").text('');
			  	$('select[name="Country"] option').each(function(){
			  		if($(this).text()==response.lwinView[0].country)
			  		{
			  			country_status = true;
			  			$(this).attr("selected","selected");
			  		}
			  	});
				if(!color_status)
			  	{
			  		$("#show_error_message_Country_not_avelabel").text("Country '"+response.lwinView[0].country+"' is not in dropdown.");
			  	
			  	}
// =========================================================
			  	var regions_status = false;
           		$("#show_error_message_Regions_not_avelabel").text('');

			  	$('select[name="Regions"] option').each(function(){
			  		if($(this).text()==response.lwinView[0].region)
			  		{
			  			regions_status = true;
			  			$(this).attr("selected","selected");
			  			// $('select[name="Regions"] option').select2('val', '3');
			  		}
			  	});

			  	if(!regions_status)
			  	{

			  		$("#show_error_message_Regions_not_avelabel").text("Regions '"+response.lwinView[0].region+"' is not in dropdown.");
			  	
			  	}
// =========================================================================
			  	console.log(response.lwinView[0].classification);

var classifications = response.lwinView[0].classification;
               $.ajax({
		             method:"POST",
		             url:base_url+"admin/products/get-product-classifications",
		             data:{"classifications":classifications},
		             dataType:'html',
		             success:function(data)
		             {
		             	$(".classifications_ajax").html(data);
		             }
		         });
			  	

			   	// console.log(response.lwinView[0].lwin);
			   	// console.log(response.lwinView[0].producerTitle);
			   	// console.log(response.lwinView[0].producerName);
			   	// console.log(response.lwinView[0].country);
			   	// console.log(response.lwinView[0].region);
			   	// console.log(response.lwinView[0].subRegion);
			   	// console.log(response.lwinView[0].site);
			   	// console.log(response.lwinView[0].parcel);
			   	// console.log(response.lwinView[0].colour);
			   	// console.log(response.lwinView[0].type);
			   	// console.log(response.lwinView[0].subType);
			   	// console.log(response.lwinView[0].designation);
			   	// console.log(response.lwinView[0].classification);
			   	// console.log(response.lwinView[0].vintageValues);
			   	// console.log(response.lwinView[0].vintageValues);
			   	// var vintageValues = response.lwinView[0].vintageValues
			   	// for(var i=0; i<vintageValues.length; i++)
			   	// {
			   	// 	get_data_with_year_lwine_code(lwine_code, vintageValues[i]);
			   	// }
               
			  }
			  

			   $(".se-pre-con").css("display","none");
			});
    }
    else
    {
    	 $(".se-pre-con").css("display","none");
    	swal({
            title: "Please insert 7 digit Lwine Code",
            icon: "warning",
            buttons: true,
            dangerMode: true,
          });
    }
}
else{
	 $(".se-pre-con").css("display","none");
	swal({
            title: "Please insert 7 digit Lwine Code",
            icon: "warning",
            buttons: true,
            dangerMode: true,
          });
}


});



function get_data_with_year_lwine_code(lwine_code, year)
{
	var settings = {
  "url": API_BASE_URL+"data/v2/priceData",
  "method": "POST",
  "timeout": 0,
  "headers": {
    "CLIENT_KEY": CLIENT_KEY_set,
	"CLIENT_SECRET": CLIENT_SECRET_set,
	"ACCEPT": "application/json",
	"CONTENT-TYPE": "application/json"
  },
  "data": JSON.stringify({"lwin":[lwine_code+year],"priceType":["A"],"priceDate":"","currency":"USD"}),
};

$.ajax(settings).done(function (response) {
  console.log(lwine_code+year);
  
var set_GST = "0";
   if($("#gst_set").val())
  {
    set_GST = $("#gst_set").val();
  } 

var _duty_set = "0";
  if($("#duti_set").val())
  {
    _duty_set = $("#duti_set").val();
  }   

  var lwinDetail = response.lwinDetail;
   for(var i=0; i<lwinDetail.length; i++)
   {
   	var dataDetail = lwinDetail[i].dataDetail;
   	
   	 for(var j=0; j<dataDetail.length; j++)
   	 {
   	 	// console.log(dataDetail[i].vintage);
   	 	// console.log(dataDetail[i].priceData);
   	 	// console.log(dataDetail[i].packSize);
   	 	$(".add_row_"+dataDetail[i].vintage).append('<tr style="cursor: pointer;"><td data-field="name" style="width: 75px;"><input type="text" name="'+dataDetail[i].vintage+'_bottle[]" value="'+dataDetail[i].packSize+'" class="'+dataDetail[i].vintage+'_bottle"></td><td data-field="name" style="width: 116px;"><input type="text" style="width: 100px;" class="'+dataDetail[i].vintage+'_retail_cose" value="'+dataDetail[i].priceData+'" name="'+dataDetail[i].vintage+'_retail_cose[]"></td><td data-field="name" style="width: 126px;">\<input type="text" name="'+dataDetail[i].vintage+'_retail_stock[]" value="0" class="'+dataDetail[i].vintage+'_retail_stock" style="width: 100px;"></td><td data-field="name" style="width: 147px;"><input type="text" name="'+dataDetail[i].vintage+'_descount_cose[]" class="'+dataDetail[i].vintage+'_descount_cose" value="0" style="width: 100px;"></td><td data-field="name" style="width: 63px;"><input type="text" name="'+dataDetail[i].vintage+'_duty[]" class="'+dataDetail[i].vintage+'_duty" value="'+_duty_set+'" style="width: 65px;"></td><td data-field="name" style="width: 70px;"><input type="text" name="'+dataDetail[i].vintage+'_GST[]" value="'+set_GST+'" class="'+dataDetail[i].vintage+'_GST" style="width: 65px;"></td><td data-field="name" style="width: 115px;"><input type="text" name="'+dataDetail[i].vintage+'_bond_cose[]" value="0" class="'+dataDetail[i].vintage+'_bond_cose" style="width: 100px;"></td><td data-field="name" style="width: 125px;"><input type="text" name="'+dataDetail[i].vintage+'_bond_stock[]" class="'+dataDetail[i].vintage+'_bond_stock" value="0" style="width: 100px;"></td><td data-field="name" style="width: 125px;"><input type="text" name="'+dataDetail[i].vintage+'_bond_descount_cost[]" class="'+dataDetail[i].vintage+'_bond_descount_cost" value="0" style="width: 100px;"></td><td><a class="delect_ed" data-vintage_id="{{cost_items.id}}" title="Delete"><i class="fa fa-trash"></i></a></td></tr>');
   	 }

   }
});
}
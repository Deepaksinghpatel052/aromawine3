(function($, window, document, undefined) {
  var pluginName = "editable",
    defaults = {
      keyboard: true,
      dblclick: true,
      button: true,
      buttonSelector: ".edit",
      maintainWidth: true,
      dropdowns: {},
      edit: function() {},
      save: function() {},
      cancel: function() {}
    };

  function editable(element, options) {
    this.element = element;
    this.options = $.extend({}, defaults, options);

    this._defaults = defaults;
    this._name = pluginName;

    this.init();
  }

  editable.prototype = {
    init: function() {
      this.editing = false;

      // if (this.options.dblclick) {
      //   $(this.element)
      //     .css('cursor', 'pointer')
      //     .bind('dblclick', this.toggle.bind(this));
      // }

      if (this.options.button) {
        $(this.options.buttonSelector, this.element)
          .bind('click', this.toggle.bind(this));
      }
    },

    toggle: function(e) {
      e.preventDefault();

      this.editing = !this.editing;

      if (this.editing) {
        this.edit();
      } else {
        this.save();
      }
    },

    edit: function() {
      var instance = this,
        values = {};

      $('td[data-field]', this.element).each(function() {
        var input,
          field = $(this).data('field'),
          value = $(this).text(),
          width = $(this).width();

        values[field] = value;

        // $(this).empty();

        if (instance.options.maintainWidth) {
          $(this).width(width);
        }

        if (field in instance.options.dropdowns) {
          input = $('<select></select>');

          for (var i = 0; i < instance.options.dropdowns[field].length; i++) {
            $('<option></option>')
              .text(instance.options.dropdowns[field][i])
              .appendTo(input);
          };

          input.val(value)
            .data('old-value', value)
            .dblclick(instance._captureEvent);
        } else {
          input = $('<input type="text" />')
            .val(value)
            .data('old-value', value)
            .dblclick(instance._captureEvent);
        }

        input.appendTo(this);

        if (instance.options.keyboard) {
          input.keydown(instance._captureKey.bind(instance));
        }
      });

      this.options.edit.bind(this.element)(values);
    },

    save: function() {
      var instance = this,
        values = {};

      $('td[data-field]', this.element).each(function() {
        var value = $(':input', this).val();

        values[$(this).data('field')] = value;

        // $(this).empty()
        //   .text(value);
      });

      this.options.save.bind(this.element)(values);
    },

    cancel: function() {
      var instance = this,
        values = {};

      $('td[data-field]', this.element).each(function() {
        var value = $(':input', this).data('old-value');

        values[$(this).data('field')] = value;

        // $(this).empty()
        //   .text(value);
      });

      this.options.cancel.bind(this.element)(values);
    },

    _captureEvent: function(e) {
      e.stopPropagation();
    },

    _captureKey: function(e) {
      if (e.which === 13) {
        this.editing = false;
        this.save();
      } else if (e.which === 27) {
        this.editing = false;
        this.cancel();
      }
    }
  };

  $.fn[pluginName] = function(options) {
    return this.each(function() {
      if (!$.data(this, "plugin_" + pluginName)) {
        $.data(this, "plugin_" + pluginName,
          new editable(this, options));
      }
    });
  };

})(jQuery, window, document);

editTable();

//custome editable starts
function editTable(){
  
  $(function() {
  var pickers = {};

  $('table tr').editable({
    dropdowns: {
      sex: ['Male', 'Female']
    },
    edit: function(values) {
      $(".edit i", this)
        .removeClass('fa-pencil')
        .addClass('fa-save')
        .attr('title', 'Save');

      pickers[this] = new Pikaday({
        field: $("td[data-field=birthday] input", this)[0],
        format: 'MMM D, YYYY'
      });
    },
    save: function(values) {
      $(".edit i", this)
        .removeClass('fa-save')
        .addClass('fa-pencil')
        .attr('title', 'Edit');

      if (this in pickers) {
        pickers[this].destroy();
        delete pickers[this];
      }
    },
    cancel: function(values) {
      $(".edit i", this)
        .removeClass('fa-save')
        .addClass('fa-pencil')
        .attr('title', 'Edit');

      if (this in pickers) {
        pickers[this].destroy();
        delete pickers[this];
      }
    }
  });
});
  
}

$(document).on("click",".add_rows",function(){
var vintage_year = $(this).data("vintage_year");
// alert($(this).data("vintage_year"));
var bottle_value = "";
console.log(($("."+vintage_year+"_bottle").last().val() == undefined));
if($("."+vintage_year+"_bottle").last().val() == undefined)
{
   bottle_value  = "0";
}
else{
  bottle_value  = $("."+vintage_year+"_bottle").last().val();
}

var _retail_cose_set = "0";
var _retail_stock_set = "0";

if($("."+vintage_year+"_retail_cose").last().val() == undefined)
{
  _retail_cose_set = "0";
}
else
{
  _retail_cose_set =$("."+vintage_year+"_retail_cose").last().val();
}

if($("."+vintage_year+"_retail_stock").last().val() == undefined)
{
  _retail_stock_set = "0";
}
else
{
  _retail_stock_set =$("."+vintage_year+"_retail_stock").last().val();
}


var _descount_cose_set = "0";
if($("."+vintage_year+"_descount_cose").last().val() == undefined)
{
  _descount_cose_set = "0";
}
else
{
  _descount_cose_set =$("."+vintage_year+"_descount_cose").last().val();
}


var _duty_set = "0";
if($("."+vintage_year+"_duty").last().val() == undefined)
{
  _duty_set = "0";
  if($("#duti_set").val())
  {
    _duty_set = $("#duti_set").val();
  } 
}
else
{
  _duty_set =$("."+vintage_year+"_duty").last().val();
}

var set_GST = "0";
if($("."+vintage_year+"_GST").last().val() == undefined)
{
  set_GST = "0";
   if($("#gst_set").val())
  {
    set_GST = $("#gst_set").val();
  } 
}
else
{
  set_GST =$("."+vintage_year+"_GST").last().val();
}

var set_bond_cose = "0";
if($("."+vintage_year+"_bond_cose").last().val() == undefined)
{
  set_bond_cose = "0";
}
else
{
  set_bond_cose=$("."+vintage_year+"_bond_cose").last().val();
}

var set_bond_stock = "0";
if($("."+vintage_year+"_bond_stock").last().val() == undefined)
{
  set_bond_stock = "0";
}
else
{
  set_bond_stock=$("."+vintage_year+"_bond_stock").last().val();
}


var set_bond_stock = "0";
if($("."+vintage_year+"_bond_stock").last().val() == undefined)
{
  set_bond_stock = "0";
}
else
{
  set_bond_stock=$("."+vintage_year+"_bond_stock").last().val();
}


var set_bond_descount_cost = "0";
if($("."+vintage_year+"_bond_descount_cost").last().val() == undefined)
{
  set_bond_descount_cost = "0";
}
else
{
  set_bond_descount_cost=$("."+vintage_year+"_bond_descount_cost").last().val();
}


var set_aroma_of_wine_cost = "0";
if($("."+vintage_year+"_set_aroma_of_wine_cost").last().val() == undefined)
{
  set_aroma_of_wine_cost = "0";
}
else
{
  set_aroma_of_wine_cost=$("."+vintage_year+"_set_aroma_of_wine_cost").last().val();
}




  $(".add_row_"+vintage_year).append('<tr style="cursor: pointer;"><td data-field="name" style="width: 75px;"><input type="hidden" name="'+vintage_year+'_id[]" value=""><input type="text" name="'+vintage_year+'_bottle[]" value="'+bottle_value+'" class="'+vintage_year+'_bottle"></td><td data-field="name" style="width: 116px;"><input type="text" style="width: 100px;" class="'+vintage_year+'_retail_cose" value="'+_retail_cose_set+'" name="'+vintage_year+'_retail_cose[]"></td><td data-field="name" style="width: 126px;"><input type="text" name="'+vintage_year+'_retail_stock[]" value="'+_retail_stock_set+'" class="'+vintage_year+'_retail_stock" style="width: 100px;"></td><td data-field="name" style="width: 147px;"><input type="text" name="'+vintage_year+'_descount_cose[]" class="'+vintage_year+'_descount_cose" value="'+_descount_cose_set+'" style="width: 100px;"> </td><td data-field="name" style="width: 63px;"><input type="text" name="'+vintage_year+'_duty[]"  class="'+vintage_year+'_duty" value="'+_duty_set+'" style="width: 65px;"></td><td data-field="name" style="width: 54px;"><input type="text" name="'+vintage_year+'_GST[]" value="'+set_GST+'" class="'+vintage_year+'_GST" style="width: 65px;"></td><td data-field="name" style="width: 115px;"><input type="text" name="'+vintage_year+'_bond_cose[]" value="'+set_bond_cose+'" class="'+vintage_year+'_bond_cose" style="width: 100px;"></td><td data-field="name" style="width: 125px;"><input type="text" name="'+vintage_year+'_bond_stock[]" class="'+vintage_year+'_bond_stock" value="'+set_bond_stock+'" style="width: 100px;"></td><td><input type="text" name="'+vintage_year+'_bond_descount_cost[]" class="'+vintage_year+'_bond_descount_cost" value="'+set_bond_descount_cost+'" style="width: 100px;"></td><td><input type="text" name="'+vintage_year+'_set_aroma_of_wine_cost[]" class="'+vintage_year+'_set_aroma_of_wine_cost" value="'+set_aroma_of_wine_cost+'" style="width: 100px;"></td><td><a class="delect_ed" title="Delete"><i class="fa fa-trash"></i></a></td></tr>');  
  
  // editTable();  
  // setTimeout(function(){   
  //   $(".editableTable").find("tbody tr:first td:last a[title='Edit']").click(); 
  // }, 200); 
  
  // setTimeout(function(){ 
  //   $(".editableTable").find("tbody tr:first td:first input[type='text']").focus();
  //     }, 300); 
  
  //  $(".editableTable").find("a[title='Delete']").unbind('click').click(function(e){
  //       $(this).closest("tr").remove();
  //   });

});




$(document).on("click",".delect_ed",function(){

var id = $(this).data("vintage_id");
var get_all_remove_ids = $("#all_remove_vintage_ids").val();

if(id)
{
  if(get_all_remove_ids=="")
{
  get_all_remove_ids = id;
}
else
{
  get_all_remove_ids = get_all_remove_ids+","+id;
}  
}


$("#all_remove_vintage_ids").val(get_all_remove_ids);
$(this).closest("tr").remove();
});

function myFunction() {
    
}

$(".editableTable").find("a[title='Delete']").click(function(e){  
  var x;
    if (confirm("Are you sure you want to delete entire row?") == true) {
        $(this).closest("tr").remove();
    } else {
        
    }     
});
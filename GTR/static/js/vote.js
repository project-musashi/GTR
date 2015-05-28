jQuery(document).ready(function($) 
    {
	$(".vote_form").submit(function(e) 
		{
		    e.preventDefault(); 
		    var btn = $("button", this);
		    var l_id = $(".hidden_id", this).val();
		    btn.attr('disabled', true);
		    $.post("/vote/", $(this).serializeArray(),
			  function(data) {
			      if(data["voteobj"]) {
				  btn.text("-");
			      }
			      else {
				  btn.text("+");
			      }
			  });
		    btn.attr('disabled', false);
		});

	$('.agree').click(function(){
    	var objid;
    	objid = $(this).attr("data-catid");
    	var old_this = $(this);
    	$.get('/agree/', {obj_id: objid}, function(data){
    	           $("#agree_count_"+objid).html(data);
        	       $("#agree_button_"+objid).attr('disabled', true);
        	       $("#disagree_button_"+objid).attr('disabled', true);
    	});
	});
	$('.disagree').click(function(){
    	var objid;
    	objid = $(this).attr("data-catid");
    	var old_this = $(this);
    	$.get('/disagree/', {obj_id: objid}, function(data){
    	           $("#disagree_count_"+objid).html(data);
                   $("#agree_button_"+objid).attr('disabled', true);
                   $("#disagree_button_"+objid).attr('disabled', true);
    	});
	});
    });
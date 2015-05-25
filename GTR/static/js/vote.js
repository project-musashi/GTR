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

	$('#agree').click(function(){
    	var objid;
    	objid = $(this).attr("data-catid");
    	$.get('/agree/', {obj_id: objid}, function(data){
            	   $('#agree_count').html(data);
        	       $('#agree').attr('disabled', true);
        	       $('#disagree').attr('disabled', true);
    	});
	});
	$('#disagree').click(function(){
    	var objid;
    	objid = $(this).attr("data-catid");
    	$.get('/disagree/', {obj_id: objid}, function(data){
            	   $('#disagree_count').html(data);
            	   $('#agree').attr('disabled', true);
        	       $('#disagree').attr('disabled', true);
    	});
	});
    });
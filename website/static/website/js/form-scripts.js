jQuery(document).ready(function() {

    /*
        Fullscreen background
    */
    /*$.backstretch("assets/img/backgrounds/1.jpg");

    $('#top-navbar-1').on('shown.bs.collapse', function(){
    	$.backstretch("resize");
    });
    $('#top-navbar-1').on('hidden.bs.collapse', function(){
    	$.backstretch("resize");
    });*/

    /*
        Form
    */
    $('.current-acad-form , .prev-acad-form ,.addtional-form , .basic-profile-form fieldset:first-child').fadeIn('slow');

    $('.current-acad-form , .prev-acad-form ,.addtional-form , .basic-profile-form input[type="text"], .current-acad-form ,.prev-acad-form ,.addtional-form ,.basic-profile-form input[type="password"], .current-acad-form  .prev-acad-form .addtional-form .basic-profile-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });


    // submit
    $('.current-acad-form ,.prev-acad-form ,.addtional-form ,.basic-profile-form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], input[type="password"], textarea').each(function() {
    		if( $(this).val() == "" ) {
    			e.preventDefault();
    			$(this).addClass('input-error');
    		}
    		else {
    			$(this).removeClass('input-error');
    		}
    	});
    	
    });


	


});


jQuery(document).ready(function() {
    
    $('.event-form fieldset:first-child').fadeIn('slow');
    
    $('.event-form input[type="text"], .event-form input[type="date"], .event-form textarea').on('focus', function() {
    	$(this).removeClass('input-error');
    });
    
    // submit
    $('.event-form').on('submit', function(e) {
    	
    	$(this).find('input[type="text"], input[type="date"], textarea').each(function() {
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

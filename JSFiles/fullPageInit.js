$(document).ready(function() {
	$('#fullpage').fullpage({
	    anchors:['page_1, page_2, page_3, page_4, page_5'],
	    navigation: true,
		navigationPosition: 'right',
		showActiveTooltip: false,
	    navigationTooltips: ['fullPage', 'Open', 'Easy', 'Touch', 'Bleh'],
	});
});
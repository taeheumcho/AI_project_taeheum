var a=document.getElementById('execute');
var b=document.getElementById('reset');
$('execute').on('click',function(){
    document.getElementById('execute_form').style.display="";
});
a.on('click',function(){
    document.getElementById('execute_form').style.display="";
});
b.on('click',function(){
	document.getElementById('execute_form').style.display="none";
//    document.getElementById('b_form').style.display="";
});

//function visiblity_showAndHid(showid) {
//	var e = document.getElementById(showid);
//	if(showid = 'execute')
////		if(document.getElementById('execute_form').style.display = '')
////			
////		else
//			document.getElementById('execute_form').style.display = '';
//	else
////		if(document.getElementById('execute_form').style.display = 'none')
////		
////		else
//			document.getElementById('execute_form').style.display = 'none';
//	
//}
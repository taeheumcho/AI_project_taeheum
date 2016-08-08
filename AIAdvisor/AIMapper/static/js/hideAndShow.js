function visiblity_showAndHid(showid) {
	var e = document.getElementById(showid);
	if(showid == 'execute')
			document.getElementById('execute_form').style.display = "";
	else
			document.getElementById('execute_form').style.display = "none";
	
}

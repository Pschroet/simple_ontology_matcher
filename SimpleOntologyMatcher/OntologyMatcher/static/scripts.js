function addItem(item){
	toggleHide("add-" + item);
	toggleHide("remove-" + item);
	if (typeof(Storage) !== "undefined") {
		if(localStorage.getItem("matchers") == null){
			localStorage.setItem("matchers", item);
		}else{
			localStorage.setItem("matchers", localStorage.getItem("matchers") + ";" + item);
		}
	} else {
	    // Sorry! No Web Storage support..
	}
}

function removeItem(item){
	toggleHide("remove-" + item);
	toggleHide("add-" + item);
}

function toggleHide(id){
	elem = document.getElementById(id);
	if(elem.hasAttribute("hidden")){
		elem.removeAttribute("hidden");
	}else{
		elem.setAttribute("hidden", "hidden");
	}
}
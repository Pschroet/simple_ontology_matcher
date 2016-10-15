//adds an ontology, terminology or matcher to the used items of it's category
function addItem(type, item, name){
	//hide the button
	toggleHide("add-" + type + "-" + name);
	//create the element for the item
	matcherList = document.getElementById("used" + type + "s");
	tmp = document.createElement("button");
	tmp.setAttribute("id", "remove-" + type + "-" + name);
	tmp.setAttribute("onClick", "removeItem('" + type + "', '" + name + "')");
	tmp.innerHTML = item;
	matcherList.appendChild(tmp);
	document.getElementById("availableOntologies").action = document.getElementById("availableOntologies").action + type + "=" + name + "&";
}

//removes a used item
function removeItem(type, name){
	toggleHide("add-" + type + "-" + name);
	parent = document.getElementById("used" + type + "s");
	child = document.getElementById("remove-" + type + "-" + name);
	parent.removeChild(child);
	document.getElementById("availableOntologies").action = document.getElementById("availableOntologies").action.replace(type + "=" + name + "&", "");
}

//toggles whether the element, whose id attribute is given, is hidden or not
function toggleHide(id){
	elem = document.getElementById(id);
	if(elem.hasAttribute("hidden")){
		elem.removeAttribute("hidden");
	}else{
		elem.setAttribute("hidden", "hidden");
	}
}
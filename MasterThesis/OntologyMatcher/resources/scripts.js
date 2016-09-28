function addItem(type, item, name){
	//hide the button
	toggleHide("add-" + name);
	//<button id="remove-{{ item }}" onClick="removeItem('{{ item }}')" hidden="hidden">Remove {{ item }}</button><br>
	//<button id="remove-{{ item }}" onClick="removeItem('{{ item }}')" hidden="hidden">Remove {{ item }}</button><br>
	//create the element for the item
	matcherList = document.getElementById("used" + type + "s");
	tmp = document.createElement("button");
	tmp.setAttribute("id", "remove-" + name);
	tmp.setAttribute("onClick", "removeItem('" + type + "', '" + name + "')");
	tmp.innerHTML = item;
	matcherList.appendChild(tmp);
	//matcherList.appendChild(document.createElement("br"));
	document.getElementById("availableOntologies").action = document.getElementById("availableOntologies").action + type + "=" + name + "&";
}

function removeItem(type, name){
	toggleHide("add-" + name);
	parent = document.getElementById("used" + type + "s");
	child = document.getElementById("remove-" + name);
	parent.removeChild(child);
	document.getElementById("availableOntologies").action = document.getElementById("availableOntologies").action.replace(type + "=" + name + "&", "");
}

function setAction(){
	alert(document.getElementById("availableOntologies").action);
}

function toggleHide(id){
	elem = document.getElementById(id);
	if(elem.hasAttribute("hidden")){
		elem.removeAttribute("hidden");
	}else{
		elem.setAttribute("hidden", "hidden");
	}
}
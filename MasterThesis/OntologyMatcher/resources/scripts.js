function addItem(type, item){
	//hide the button
	toggleHide("add-" + item);
	//<button id="remove-{{ item }}" onClick="removeItem('{{ item }}')" hidden="hidden">Remove {{ item }}</button><br>
	//<button id="remove-{{ item }}" onClick="removeItem('{{ item }}')" hidden="hidden">Remove {{ item }}</button><br>
	//create the element for the item
	matcherList = document.getElementById("used" + type + "s");
	tmp = document.createElement("button");
	tmp.setAttribute("id", "remove-" + item);
	tmp.setAttribute("onClick", "removeItem('" + type + "', '" + item + "')");
	tmp.innerHTML = item;
	matcherList.appendChild(tmp);
	//matcherList.appendChild(document.createElement("br"));
	document.getElementById("availableOntologies").action = document.getElementById("availableOntologies").action + type + "=" + item + "&";
}

function removeItem(type, item){
	toggleHide("add-" + item);
	parent = document.getElementById("used" + type + "s");
	child = document.getElementById("remove-" + item);
	parent.removeChild(child);
	document.getElementById("availableOntologies").action = document.getElementById("availableOntologies").action.replace(type + "=" + item + "&", "");
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
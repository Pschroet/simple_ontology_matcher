function addItem(type, item){
	//hide the button
	toggleHide("add-" + item);
	//<button id="remove-{{ item }}" onClick="removeItem('{{ item }}')" hidden="hidden">Remove {{ item }}</button><br>
	//<button id="remove-{{ item }}" onClick="removeItem('{{ item }}')" hidden="hidden">Remove {{ item }}</button><br>
	//create the element for the item
	matcherList = document.getElementById("used" + type);
	tmp = document.createElement("button");
	tmp.setAttribute("id", "remove-" + item);
	tmp.setAttribute("onClick", "remove('" + type + "', 'remove-" + item + "')");
	tmp.innerHTML = item;
	matcherList.appendChild(tmp);
	matcherList.appendChild(document.createElement("br"));
	//add the item to the corresponding list
	if (typeof(Storage) !== "undefined") {
		if(localStorage.getItem(type) == null){
			localStorage.setItem(type, item);
		}else{
			localStorage.setItem(type, localStorage.getItem(type) + ";" + item);
		}
	} else {
	    // Sorry! No Web Storage support..
	}
}

function removeItem(type, item){
	toggleHide("add-" + item);
	//add the item to the corresponding list
	if (typeof(Storage) !== "undefined") {
		if(localStorage.getItem(type) != null){
			localStorage.setItem(type, localStorage.getItem(type).replace(item + ";", ""));
		}
	} else {
	    // Sorry! No Web Storage support..
	}
}

function toggleHide(id){
	console.log(id);
	elem = document.getElementById(id);
	if(elem.hasAttribute("hidden")){
		elem.removeAttribute("hidden");
	}else{
		elem.setAttribute("hidden", "hidden");
	}
}
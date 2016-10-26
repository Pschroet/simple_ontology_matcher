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

function saveResult(){
	//get all matches...
	matchingResults = document.getElementById("matchingResults").getElementsByTagName("li");
	//... go through them
	result = "<?xml version='1.0' encoding='utf-8'?>\n<rdf:RDF  xmlns='http://knowledgeweb.semanticweb.org/heterogeneity/alignment'\n xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'\n xmlns:xsd='http://www.w3.org/2001/XMLSchema#'>\n<Alignment>\n";
	ontologies = document.getElementById("ontologies").getElementsByTagName("div");
	for(var i = 0; i < ontologies.length; i++){
		result = result + "\t<onto" + i + ">" + ontologies[i].innerHTML + "</onto" + i + ">\n";
	}
	for(var i = 0; i < ontologies.length; i++){
		result = result + "\t<uri" + i + ">" + ontologies[i].innerHTML + "</uri" + i + ">\n";
	}
	for(var i = 0; i < matchingResults.length; i++){
		//connectionOptions = matchingResults[i].getElementsByTagName("select")[0];
		//chosenOption = connectionOptions.options[connectionOptions.selectedIndex].value;
		//if(chosenOption != "None"){
			//console.log(matchingResults[i].getElementsByTagName("a")[0].getAttribute("href"));
			//console.log(matchingResults[i].getElementsByTagName("a")[1].getAttribute("href"));
			//console.log(chosenOption);
		//}
		result = result + "\t<map>\n\t\t<Cell>\n\t\t\t<entity1 rdf:resource='" + matchingResults[i].getElementsByTagName("a")[0].getAttribute("href") + "'/>\n";
		result = result + "\t\t\t<entity2 rdf:resource='" + matchingResults[i].getElementsByTagName("a")[1].getAttribute("href") + "'/>\t\n";
		result = result + "\t\t</Cell>\n\t</map>\n";
	}
	result = result + "</Alignment>\n</rdf:RDF>";
	var b = new Blob([result],{type:"text/plain;charset=utf-8"});
	saveAs(b, "matches.rdf");
}
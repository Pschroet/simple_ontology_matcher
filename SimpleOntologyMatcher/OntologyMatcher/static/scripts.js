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
	result = "<?xml version='1.0' encoding='utf-8'?>\n<rdf:RDF  xmlns='http://knowledgeweb.semanticweb.org/heterogeneity/alignment'\n xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'\n xmlns:rdfs='http://www.w3.org/2000/01/rdf-schema#'\n xmlns:xsd='http://www.w3.org/2001/XMLSchema#'>\n<Alignment>\n";
	ontologies = document.getElementById("ontologies").getElementsByTagName("div");
	for(var i = 0; i < ontologies.length; i++){
		result = result + "\t<onto" + i + ">" + ontologies[i].innerHTML + "</onto" + i + ">\n";
	}
	for(var i = 0; i < ontologies.length; i++){
		result = result + "\t<uri" + i + ">" + ontologies[i].innerHTML + "</uri" + i + ">\n";
	}
	for(var i = 0; i < matchingResults.length; i++){
		result = result + "\t<map>\n\t\t<Cell>\n\t\t\t<entity1 rdf:resource='" + matchingResults[i].getElementsByTagName("a")[0].getAttribute("href") + "'";
		//if there is a label, add it to the result
		if(matchingResults[i].getElementsByTagName("i")[0].innerHTML != ""){
			result = result + ">\n\t\t\t\t<rdfs:label>" + matchingResults[i].getElementsByTagName("i")[0].innerHTML + "</rdfs:label>\n\t\t\t</entity1>\n"
		}else{
			result = result + "/>\n";
		}
		result = result + "\t\t\t<entity2 rdf:resource='" + matchingResults[i].getElementsByTagName("a")[1].getAttribute("href") + "'";
		//if there is a label, add it to the result
		if(matchingResults[i].getElementsByTagName("i")[1].innerHTML != ""){
			result = result + ">\n\t\t\t\t<rdfs:label>" + matchingResults[i].getElementsByTagName("i")[1].innerHTML + "</rdfs:label>\n\t\t\t</entity2>\n";
		}else{
			result = result + "/>\n";
		}
		//if there is a connection, save it, too
		connectionOptions = matchingResults[i].getElementsByTagName("select")[0];
		chosenOption = connectionOptions.options[connectionOptions.selectedIndex].value;
		if(chosenOption != "None"){
			result = result + "\t\t\t<connectionType>" + chosenOption + "</connectionType>\n";
		}
		result = result + "\t\t</Cell>\n\t</map>\n";
	}
	result = result + "</Alignment>\n</rdf:RDF>";
	var b = new Blob([result],{type:"text/plain;charset=utf-8"});
	saveAs(b, "matches.rdf");
}
'''
Created on 15.09.2016

@author: Philipp Schroeter
'''

#tries to match two ontologies just by counting the matches of each item in the results
#returns a list, which holds information about nodes that are assumed to be linked on some way
# each item in the list has the following elements (in this order): IRI of the first element, it's label, the IRI of the second element, it's label, a string that states, why those elements have been chosen
def match_two_ontologies(results, onto, onto1):
    #ensure that there are actually ontologies to compare
    if onto is not None and onto1 is not None:
        connections = {"matches":[], "text":"Counted Matches (counting_matcher)"}
        counter = {}
        for item in results:
            for match in item["matches"]:
                if counter.has_key(match[0] + "$" + match[2]):
                    counter[match[0] + "$" + match[2]] += 1
                else:
                    counter[match[0] + "$" + match[2]] = 1
        for item in counter:
            match = item.split("$")
            connections["matches"].append([match[0], "", match[1], "", " have been found " + str(counter[item]) + " times"])
        return results.append(connections)
# simple_ontology_matcher
This projects is the source code produced during my master thesis at Freie Universität Berlin (which can be found [here](https://github.com/Pschroet/master-thesis-ps-ontology-matching)). It's an ontology matching tool, consisting of a backend, frontend and additional tools.

To run it, just use the settings.py as a Django application.

The software is released under the GNU General Public License 3

https://www.gnu.org/licenses/gpl-3.0.html

Part of the repository are the following zip archives:
- [defusedxml-0.4.1.tar.gz](https://pypi.python.org/pypi/defusedxml/)
- [FileSaver.js-1.3.3.zip](https://github.com/eligrey/FileSaver.js)
- [PyDictionary-1.5.2.zip](https://pypi.python.org/pypi/PyDictionary)
- [python-Levenshtein-0.12.0.tar.gz](https://github.com/dimlev/pylevenshtein)

as well as the file [FileSaver.js](https://github.com/eligrey/FileSaver.js)

They all retain their original license (included in the zip files or found on the website) and are not released as part of this software. They are just shipped for convenience.

==================================================================

__Running as a standalone software__

'python SimpleOntologyMatcher/manage.py runserver'

This starts the Django server. When no port is given after *runserver* the app can be accessed at

> http://127.0.0.1:8000/matcher

Another possibility is to use *main.py* to run matching algorithms. This file can be found in

> SimpleOntologyMatcher/OntologyMatcher/

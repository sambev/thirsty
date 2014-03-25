=======
thirsty
=======
Flask project creation and helper.  Currently it just creates a bootstrapped
application with Flask, Grunt, and Foundation that has the following::
    sass compilation and linting with grunt
    pep8 linting
    foundation grid
    angularjs

Details about the application can be found here::
https://github.com/sambev/basicflask

Supported commands
==================
`thirsty new project <name>` - creates an entirely new bootstrapped project
`thirsty new view <name>` - creates a method view with empty CRUD methods

What it does
=============
Downloads the master branch of https://github.com/sambev/basicflask.git as zip
Unzips it
Renames it to whatever you supplied as name
Deletes zip
Installs python dependencies with pip
Installs bower dependencies with bower
Installs npm dependencies with npm
The end.


Dependencies
============
Python 2.7.5
Virtualenv 1.10.1
Ruby 2.0.0p247 - for sass, hopefully replacing with python soon
Bower 1.2.8
NPM 1.3.14

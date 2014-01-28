thirsty
=======

Base project creation script.  Sets up a project with Flask, Foundation, and Grunt.

Run it
------
`bash thirsty.sh <name>`

Add it to your path and call it anywhere.

What it does (You can just read it.  It is short.)
------------
Downloads the master branch of https://github.com/sambev/basicflask.git as zip
unzips it
renames it to whatever you supplied as name
deletes zip
installs python dependencies with pip
installs bower dependencies with bower
installs npm dependencies with npm

The end.

You should use virutualenv with this.

Dependencies
------------
Python 2.7.5
Ruby 2.0.0p247
Bower 1.2.8
NPM 1.3.14

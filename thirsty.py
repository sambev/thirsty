#!/usr/bin/python
"""
Thirsty project creator/helper
    use it like:
    `thirsty new project myFirstProject`
    `thirsty new view myView`

    essentially:
    `thirsty <action> <object> <name>`

    where action can be 'new'
    object can be 'project' or 'view'
    name is the name you want it to be called
"""
import argparse
import zipfile
import StringIO
import os
import urllib2
import subprocess
from bin.new_actions import newView


parser = argparse.ArgumentParser()
parser.add_argument(
    'action',
    help='Action to be applied. `new` is the only supported action right now',
    type=str
)
parser.add_argument(
    'object',
    help='Object to apply action to. `project` or `view`',
    type=str
)
parser.add_argument(
    'name',
    help='Name of the object',
    type=str
)
args = parser.parse_args()

if args.action == 'new':
    if args.object == 'project':
        """Create a new project by downloading the basicflask zip from github
        and try to install the dependencies
        """
        try:
            print 'Fetching app code from github...'
            req = urllib2.urlopen('https://github.com/sambev/basicflask/archive/master.zip')
            z = zipfile.ZipFile(StringIO.StringIO(req.read()))
            print 'Extracting files...'
            z.extractall()
            os.rename('basicflask-master', args.name)
            os.chdir(args.name)
            try:
                print 'Installing python dependencies'
                subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
            except OSError as e:
                print 'Failure %s' % e
                print 'You need to have pip to install the dependencies'

            try:
                print 'Installing bower packages'
                subprocess.call(['bower', 'install'])
            except OSError as e:
                print 'Failure %s' % e
                print 'You need to have bower installed for front end libraries'

            try:
                print 'Installing npm packages'
                subprocess.call(['npm', 'install'])
            except OSError as e:
                print 'Failure %s' %e
                print 'You need to have npm installed to use grunt'

        except Exception as e:
            print 'Failure: %s' % e

    elif args.object == 'view':
        """Create a new method view with the given name"""
        try:
            print 'Creating new view...'
            newView(args.name)
            print 'SUCCESS!'
        except Exception as e:
            print 'Failure: %s' % e

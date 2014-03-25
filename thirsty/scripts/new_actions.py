import urllib2
import subprocess
import zipfile
import StringIO
import os

def newView(name):
    """Create a new basic new view with the given name
    :param name - name of the view
    """
    py_path = os.environ['VIRTUAL_ENV']
    with open(py_path + '/lib/python2.7/site-packages/thirsty/templates/base_view.py') as f:
        try:
            file = f.read()
            new_file = file.replace('Name', name.title())
            new_file = new_file.replace('name', name.lower())
            with open('%s.py' % name, 'w') as nf:
                try:
                    nf.write(new_file)
                except:
                    nf.close()
        except:
            f.close()


def newProject(name):
    """Create a new project with the given name
    :param name - name of the project

    This downloads the basic-flask master from github and runs all of the
    dependency installs
    """
    print 'Fetching app code from github...'
    req = urllib2.urlopen('https://github.com/sambev/basicflask/archive/master.zip')
    z = zipfile.ZipFile(StringIO.StringIO(req.read()))
    print 'Extracting files...'
    z.extractall()
    os.rename('basicflask-master', name)
    os.chdir(name)
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

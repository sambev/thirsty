def newView(name):
    """Create a new basic new view with the given name
    :param name - name of the view
    """
    with open('bin/base_view.py') as f:
        try:
            file = f.read()
            new_file = file.replace('Name', name.title())
            new_file = new_file.replace('name', name.lower())
            with open('mynewview.py', 'w') as nf:
                try:
                    nf.write(new_file)
                except:
                    nf.close()
        except:
            f.close()

if __name__ == '__main__':
    newView('person')
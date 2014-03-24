from distutils.core import setup
from pip.req import parse_requirements

setup(
    name='thirsty',
    version='0.0.1',
    author='Sam Beveridge',
    author_email='sam.bev87@gmail.com',
    url='http://github.com/sambev/thirsty',
    packages=[
        'thirsty',
        'thirsty/scripts',
        'thirsty/templates'
    ],
    scripts=['bin/thirsty'],
    license='LISCENSE.txt',
    description='flask project creation and helper',
    long_description=open('README.txt').read(),
)

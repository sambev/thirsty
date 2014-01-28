#!/bin/bash
# Download the zip file from github:
#  https://github.com/sambev/basicflask/archive/master.zip
# unzip, rename the folder, and delete it.

if [[ -z $1 ]]; then
    echo "ERROR: Please enter in a project name"
    echo "usage: 'thirsty <name>'"
    exit 1
fi

echo "===================="
echo "DOWNLOADING FILES..."
echo "===================="
curl -LOk https://github.com/sambev/basicflask/archive/master.zip

echo "===================="
echo "UNZIPPING PROJECT..."
echo "===================="
unzip master.zip

echo "===================="
echo "RENAMING PROJECT...."
echo "===================="
mv basicflask-master $1

echo "===================="
echo "CLEANING UP........."
echo "===================="
rm master.zip

echo "================================="
echo "INSTALLING PYTHON DEPENDENCIES..."
echo "================================="
cd $1 && pip install -r requirements.txt


echo "================================="
echo "INSTALLING BOWER COMPONENTS......"
echo "================================="
bower install

echo "================================="
echo "INSTALLING NPM COMPONENTS........"
echo "================================="
npm install

exit 0
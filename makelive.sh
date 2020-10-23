#!/bin/sh
pipenv run sphinx-build -a -b html source build
pipenv run sphinx-autobuild -b html --delay 1 source build

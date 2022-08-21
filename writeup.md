## Goal
To create a frontend for [pytube](https://github.com/pytube/pytube) using [pyside6](https://pypi.org/project/PySide6/).

[pytube](https://github.com/pytube/pytube) is a library in python used to download videos from YouTube. I will be creating a front-end for the command line app using [pyside6](https://pypi.org/project/PySide6/).

---

## Overview
This is the first project i've done on my own in python. In doing so i've learned a lot about how python projects are set up and managed. The most prominent tool i've learned about is pipenv from [this great article at Real Python](https://realpython.com/pipenv-guide/). I have known about virtual environments in python but have never really used them, so this was a great way to get familiar with it. 

---

## Set Up

The first thing I did was set up pipenv by running the following commands in my shell
* pipenv shell --three
  * Sets up a python3 virtual environment in the given directory
* pipenv install -e git+https://github.com/pytube/pytube.git#egg=pytube
  * Installs the pytube package
* pipenv install pytest --dev
  * Installs pytest but only for development purposes. If we were to deployt to prouduction with pipenv, this would be emitted
* pipenv install pyside6   
  * Qt for frontend
* pipenv --venv
  * This was run to see where the virutal enviorment python interpreter is installed so I could point VS Code to it.  

---

## Learning

Learning resouces for Qt for Python can be found [here](https://doc.qt.io/qtforpython/tutorials/index.html).

#### Qt

The basic flow of a Qt app seems to be
1. create a QApplication object.
2. create/instantiate your widgets, labels, etc.
3. call .show on your top level views
4. call app.exec on your QApllication object 
   * this call start running the code by entering Qt's main loop


---

## Design
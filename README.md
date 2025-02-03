<h1 align="center">ProgrammingDirectories</h1>

<p align="center">
  <img src="https://raw.githubusercontent.com/fersilentt/ProgrammingDirectories/refs/heads/master/resources/img/ProgrammingDirectories.png" width="8%" />
</p>


<br/>
    <i>This project is created to manage projects and programming tutorials that we have stored in different repositories such as GitHub, GitLab, BitBucket, etc.</i>
<br/>
<br/>





- [Important](#Important)
- [Build application](#Build-application)
  - [Commands to create icon in MacOS](#Commands-to-create-icon-in-MacOS)
- [Bug fixes](#Bug-fixes)

---

#### Important

1. To build this project we must have Python 3.8 installed.

2. The python version and venv are created with pyenv

3. To build the project, we execute the commands in section **[Build application](#Build-application)**

---

#### Build application

- To install all the modules run
```
pyenv shell 3.8.10
python -V
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python src/app.py
```
- To install module by module

```
pip install sqlalchemy
pip install pyqt5==5.15.2
pip install validators
pip install requests
pip install PyInstaller==4.8
python src/app.py
```

* *If a fork of the project is to be created, we execute the following commands to avoid tracing the project configuration files while testing*

```
git update-index --assume-unchanged src/static/json/data.json
git update-index --assume-unchanged src/static/json/list_databases.json
```

* *In case you need to convert .ui files from qt to .py, run the following*

```
pyuic5 file_name_ui.ui -o file_name_py.py
```

#### Commands to create icon in MacOS

1. We create the application with the configuration set up

```
pyinstaller Programming\ Directories.spec
```

* *When executing this command you may get an error message when building, simply run the command again*

* *If you are going to modify the .spec file, adding more configuration parameters we execute the following*

```
pyinstaller --name "Programming Directories" --icon="resources/img/main_icon.icns" --windowed src/app.py
```


2. Copy the following files and folders to /Contents/MacOS once the application has been created

```
config.py
controller
model
static
view
```

#### Bug fixes

- If MacOS displays the following error when running the application, **"Programming Directories" is damaged and cannot be opened. You should take it to the dump.** , run the following command to fix this

```
xattr -cr /Applications/Programming\ Directories.app/
```

* *When the executable is created with PyInstaller, it works without problems locally, but when it is uploaded to GiHub, it has this problem*

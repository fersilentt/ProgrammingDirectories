<h1 align="center">Programming Directories</h1>

<p align="center">
  <img src="https://github.com/fersilentt/ProgrammingDirectories/blob/master/resources/img/main_icon.png" width="8%" />
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

1. To install all the modules run
```
pyenv shell 3.8.10
python -V
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt 
```
2. To install module by module

```
pip install sqlalchemy
pip install pyqt5==5.15.2
pip install validators
pip install requests
pip install PyInstaller==4.8
```

3. We start the application

```
python src/app.py
```
* *If a fork of the project is to be created, we execute the following commands to avoid tracing the project configuration files while testing*

```
git update-index --assume-unchanged src/static/json/data.json
git update-index --assume-unchanged src/static/json/list_databases.json
```

#### Commands to create icon in MacOS

1. We create the executable to build our application with **py2applet**.

```
pyinstaller -n "Programming Directories" --windowed app.py
```

2. We build the application, so that it creates the .app file

```
pyinstaller Programming\ Directories.spec
```

3. Copy the contents of the missing code by following these steps

```
a. Enter the "dist" folder
b. In the created application we click on "Show package contents"
c. Copy the "src" folder, inside "/Contents/Resources"
```

```
pyuic5 src/view/ui/main/main.ui -o main_form.py
```

#### Bug fixes

# Mount virtual environment and install packages
pyenv shell 3.8.10
python -V
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Application Packaging
pyinstaller "ProgrammingDirectories.spec"

# Copy application directories and files
cp -r src/controller/ dist/ProgrammingDirectories/
cp -r src/model/ dist/ProgrammingDirectories/
cp -r src/view/ dist/ProgrammingDirectories/
cp -r src/static/ dist/ProgrammingDirectories/
cp src/config.py dist/ProgrammingDirectories/
cp resources/img/ProgrammingDirectories.png dist/ProgrammingDirectories
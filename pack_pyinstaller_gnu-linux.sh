# Mount virtual environment and install packages
pyenv shell 3.8.10
python -V
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Application Packaging
cp spec_versions/ProgrammingDirectories_gnu-linux.spec ProgrammingDirectories.spec
pyinstaller "ProgrammingDirectories.spec"

# Copy application directories and files
cp resources/img/ProgrammingDirectories.png dist/ProgrammingDirectories

path=dist/ProgrammingDirectories/ProgrammingDirectories.desktop

echo "[Desktop Entry]" >> $path
echo "Type=Application" >> $path
echo "Name=ProgrammingDirectories" >> $path
echo "Comment=Manage projects and programming tutorials" >> $path
echo "Exec=ProgrammingDirectories" >> $path
echo "Icon=ProgrammingDirectories.png" >> $path
echo "Categories=Network;" >> $path

chmod +x $path
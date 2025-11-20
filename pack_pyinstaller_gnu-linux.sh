# Mount virtual environment and install packages
pyenv shell 3.8.10
python -V
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# We delete the Pyinstaller files
rm -r build/
rm -r dist/
rm ProgrammingDirectories.spec 

# Application Packaging
cp spec_versions/ProgrammingDirectories_gnu-linux.spec ProgrammingDirectories.spec
pyinstaller "ProgrammingDirectories.spec"

# Copy application directories and files
cp resources/img/ProgrammingDirectories.png dist/ProgrammingDirectories

# Create the shortcut
path=dist/ProgrammingDirectories/ProgrammingDirectories.desktop

echo "[Desktop Entry]" >> $path
echo "Type=Application" >> $path
echo "Name=ProgrammingDirectories" >> $path
echo "Comment=Manage projects and programming tutorials" >> $path
echo "Exec=ProgrammingDirectories" >> $path
echo "Icon=ProgrammingDirectories" >> $path
echo "Categories=Network;" >> $path

chmod +x $path

# Compressed the folder in tar.gz format
tar -czvf dist/ProgrammingDirectories-GNU-Linux.tar.gz dist/ProgrammingDirectories/

# Copy the installation.sh file for GNU-Linux to the dist folder
cp install_gnu-linux.sh dist/

# Mount virtual environment and install packages
pyenv shell 3.8.10
python -V
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Application Packaging
cp spec_versions/ProgrammingDirectories_mac.spec ProgrammingDirectories.spec
pyinstaller "ProgrammingDirectories.spec" -y


if [ -d dist/ProgrammingDirectories.app ]
    then 
        state="yes"
    else 
        state="no"
fi


while [[ "$state"=="no" ]]
do
  pyinstaller "ProgrammingDirectories.spec" -y
  
  if [ -d dist/ProgrammingDirectories.app ]
    then
        state="yes"
        break
    else 
        state="no"
  fi
done

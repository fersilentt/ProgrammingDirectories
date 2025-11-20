#!/bin/bash

wget https://github.com/fersilentt/ProgrammingDirectories/releases/download/v1.0.5/ProgrammingDirectories-GNU-Linux.tar.gz

tar -xf ProgrammingDirectories-GNU-Linux.tar.gz


# We check if the directory exists
DIRECTORIO=$(eval echo ~/.local/share/ProgrammingDirectories/)

if [ -d "$DIRECTORIO" ]; then
    echo "The directory exists."
    rm -r ~/.local/share/ProgrammingDirectories/
    mv ProgrammingDirectories ~/.local/share
else
    echo "The directory does not exist."
    mv ProgrammingDirectories ~/.local/share
fi


echo "[Desktop Entry]" >> ProgrammingDirectories.desktop
echo "Type=Application" >> ProgrammingDirectories.desktop
echo "Name=ProgrammingDirectories" >> ProgrammingDirectories.desktop
echo "Comment=Manage projects and programming tutorials" >> ProgrammingDirectories.desktop
echo "Exec=/home/$USER/.local/share/ProgrammingDirectories/ProgrammingDirectories" >> ProgrammingDirectories.desktop
echo "Icon=/home/$USER/.local/share/ProgrammingDirectories/ProgrammingDirectories.png" >> ProgrammingDirectories.desktop
echo "Categories=Network;" >> ProgrammingDirectories.desktop


if test -d ~/.local/share/applications/; then x="yes"; else x="no"; fi


if [ "$x" = "yes" ]
	then 
		mv ProgrammingDirectories.desktop ~/.local/share/applications/
		
    else
        mkdir -p ~/.local/share/applications/
        mv ProgrammingDirectories.desktop ~/.local/share/applications/
		
fi 

rm ProgrammingDirectories-GNU-Linux.tar.gz
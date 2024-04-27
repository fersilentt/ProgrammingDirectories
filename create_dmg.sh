mkdir -p dist/dmg

rm -r dist/dmg/*

cp -r "dist/Programming Directories.app" dist/dmg

test -f "dist/Programming Directories.dmg" && rm "dist/Programming Directories.dmg"

create-dmg \
    --volname "Programming Directories" \
    --volicon "resources/img/main_icon.icns" \
    --window-pos 200 120 \
    --window-size 600 300 \
    --icon-size 100 \
    --icon "Programming Directories.app" 175 120 \
    --hide-extension "Programming Directories.app" \
    --app-drop-link 425 120 \
    "dist/Programming Directories.dmg" \
    "dist/dmg/"
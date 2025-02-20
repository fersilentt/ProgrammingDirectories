# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src/app.py'],
             pathex=[],
             binaries=[],
             datas=[('src/controller/', 'controller'), ('src/model/', 'model'), ('src/view/', 'view'), ('src/static/', 'static'), ('src/config.py', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='Programming Directories',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='resources/img/ProgrammingDirectories.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='ProgrammingDirectories')
app = BUNDLE(coll,
             name='ProgrammingDirectories.app',
             icon='resources/img/ProgrammingDirectories.icns',
             bundle_identifier=None)

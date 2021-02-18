# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/arbaaz/Work/Git/Hermes/Release/Hermes'],
             binaries=[],
             datas=[( '/home/arbaaz/Work/Git/Hermes/Release/Hermes/data/Harry Potter and the Prince of Slytherin_md.txt','data' ),
                ( '/home/arbaaz/Work/Git/Hermes/Release/Hermes/data/Harry Potter and the Prince of Slytherin_pt.txt','data' ),
                ( '/home/arbaaz/Work/Git/Hermes/Release/Hermes/data/POS Dictionary.json','data' ),
                ( '/home/arbaaz/Work/Git/Hermes/Release/Hermes/data/POS Dictionary.xlsx','data' ),
                ( '/home/arbaaz/Work/Git/Hermes/Release/Hermes/images/icon.ico','.' )
                ],
             hiddenimports=['cmath'],
             hookspath=[],
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
          name='Hermes',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon='/home/arbaaz/Work/Git/Hermes/Release/Hermes/images/icon.ico',
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Hermes')

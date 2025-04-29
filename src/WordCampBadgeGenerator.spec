# -*- mode: python ; coding: utf-8 -*-

import os
import platform

block_cipher = None

# Determinar el icono según el sistema operativo
icon_path = 'assets/icon.icns' if platform.system() == 'Darwin' else 'assets/icon.ico'

a = Analysis(
    ['WordCampBadgeGenerator.py'],  # Ruta al archivo principal de Python relativa al .spec
    pathex=['.'],  # El directorio raíz donde PyInstaller buscará los archivos
    binaries=[],
    datas=[('assets/*', 'assets')],  # Ruta a los assets relativa al .spec
    hiddenimports=['tkinter'],
    hookspath=[],
    runtime_hooks=[],
    excludes=['pkg_resources._vendor.packaging.utils', 'pkg_resources._vendor.packaging.version', 'pkg_resources._vendor.packaging.specifiers', 'pkg_resources._vendor.packaging.requirements', 'pkg_resources._vendor.packaging.markers'],  # Excluir módulos innecesarios
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

# Creamos el archivo PYZ con los datos del script
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

if platform.system() == 'Darwin':
    # Configuración específica para macOS
    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='WordCampBadgeGenerator',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=False,
        console=False,
        icon=icon_path,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
    )

    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=False,
        upx_exclude=[],
        name='WordCampBadgeGenerator',
    )

    app = BUNDLE(
        coll,
        name='WordCampBadgeGenerator.app',
        icon=icon_path,
        bundle_identifier='com.wordcamp.badgegenerator',
        info_plist={
            'NSHighResolutionCapable': 'True',
            'LSBackgroundOnly': 'False',
            'CFBundleDisplayName': 'WordCamp Badge Generator',
            'CFBundleName': 'WordCamp Badge Generator',
            'CFBundleExecutable': 'WordCampBadgeGenerator',
            'CFBundleIdentifier': 'com.wordcamp.badgegenerator',
            'CFBundleInfoDictionaryVersion': '6.0',
            'CFBundlePackageType': 'APPL',
            'CFBundleShortVersionString': '1.0.0',
            'LSMinimumSystemVersion': '10.13.0',
            'NSAppleScriptEnabled': 'False',
            'NSPrincipalClass': 'NSApplication',
            'NSRequiresAquaSystemAppearance': 'False',
            'LSApplicationCategoryType': 'public.app-category.utilities',
        },
    )
else:
    # Configuración para Windows
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        [],
        name='WordCampBadgeGenerator',  # Nombre del archivo ejecutable
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=False,  # Deshabilitar UPX para evitar errores
        console=False,  # Cambiado a False para evitar la ventana de consola
        icon=icon_path,  # Ruta al icono relativa al .spec
    )


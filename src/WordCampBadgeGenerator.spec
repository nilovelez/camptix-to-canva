# -*- mode: python ; coding: utf-8 -*-

import os

block_cipher = None

a = Analysis(
    ['WordCampBadgeGenerator.py'],  # Ruta al archivo principal de Python relativa al .spec
    pathex=['.'],  # El directorio raíz donde PyInstaller buscará los archivos
    binaries=[],
    datas=[('assets/*', 'assets')],  # Ruta a los assets relativa al .spec
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=['pkg_resources._vendor.packaging.utils', 'pkg_resources._vendor.packaging.version', 'pkg_resources._vendor.packaging.specifiers', 'pkg_resources._vendor.packaging.requirements', 'pkg_resources._vendor.packaging.markers', 'pkg_resources._vendor.packaging.utils', 'pkg_resources._vendor.packaging.version', 'pkg_resources._vendor.packaging.specifiers', 'pkg_resources._vendor.packaging.requirements', 'pkg_resources._vendor.packaging.markers'],  # Excluir módulos innecesarios
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

# Creamos el archivo PYZ con los datos del script
pyz = PYZ(a.pure, a.zipped_data,
          cipher=block_cipher)

# Configuración del ejecutable para Windows
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
    icon='assets/icon.ico',  # Ruta al icono relativa al .spec
)


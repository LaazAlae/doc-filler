# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['document_filler.py'],
    pathex=[],
    binaries=[],
    datas=[('cons_ids.txt', '.'), ('descriptions.txt', '.'), ('dropdown_options.json', '.'), ('filldoc.docm', '.'), ('filldoc.docx', '.'), ('flights.txt', '.'), ('names.txt', '.'), ('tags.txt', '.'), ('user_selections.txt', '.'), ('app.log', '.')],
    hiddenimports=['kivy', 'kivy.deps.sdl2', 'kivy.deps.glew'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['gstreamer'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='document_filler',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['logo.icns'],
)
app = BUNDLE(
    exe,
    name='document_filler.app',
    icon='logo.icns',
    bundle_identifier=None,
)

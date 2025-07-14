[app]
title = Visita Técnica
package.name = VisitaTecnica
package.domain = org.vini.visita
version = 0.1

# Código-fonte principal
source.dir = .
source.main = visita_tecnica_app/main.py
source.include_patterns = visita_tecnica_app/*.kv, visita_tecnica_app/**/*.db, visita_tecnica_app/**/*.png, visita_tecnica_app/**/*.jpeg

# Bibliotecas necessárias
requirements = python3,kivy,sqlite3,Pillow,cython,pyjnius

# Permissões Android
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA

# Tela cheia e orientação
fullscreen = 1
orientation = portrait

# Configurações do Android
android.api = 31
android.minapi = 21
android.target = 31
android.build_tools_version = 33.0.2
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a

# Forçar branch estável do python-for-android
p4a.branch = master

# Ícones e splash
presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png

# Habilita o modo debug (APK não assinado)
android.debug = 1

# Exibe logs detalhados e impede builds como root
[buildozer]
log_level = 2
warn_on_root = 1

# Se quiser usar uma versão específica do SDK localmente:
# android.sdk_path = /caminho/para/seu/sdk
# android.ndk_path = /caminho/para/seu/ndk

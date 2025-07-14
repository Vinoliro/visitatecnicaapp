[app]
# Nome exibido no dispositivo
title = Visita Técnica
version = 0.1

# Nome interno do pacote
package.name = VisitaTecnica

# Domínio reverso (pode personalizar)
package.domain = org.vini.visita

# Diretório onde está seu código-fonte
source.dir = .

# Caminho para o arquivo principal do app
source.main = visita_tecnica_app/main.py

# Quais arquivos incluir no APK
source.include_patterns = visita_tecnica_app/*.kv, visita_tecnica_app/**/*.db, visita_tecnica_app/**/*.png, visita_tecnica_app/**/*.jpeg

# Bibliotecas Python necessárias
requirements = python3,kivy,sqlite3,Pillow,cython,pyjnius

# Permissões Android
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA

# Tela cheia e orientação
fullscreen = 1
orientation = portrait

# Versões da API Android
android.minapi = 21
android.target = 31

# ✅ Corrigir erro do GitHub Actions aceitando build tools compatíveis
android.build_tools_version = 33.0.2

# Arquiteturas suportadas
android.archs = arm64-v8a, armeabi-v7a

# Splash e ícone (opcional)
presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png

# Tipo de build
android.debug = 1

# Logging
[buildozer]
log_level = 2
warn_on_root = 1

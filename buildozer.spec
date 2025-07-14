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

# Permissões Android (adicione mais se necessário)
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, CAMERA

# Defina se o app é em tela cheia
fullscreen = 1

# Força a orientação retrato
orientation = portrait

# Versões da API Android
android.minapi = 21
android.target = 31

# Arquiteturas de CPU suportadas
android.archs = arm64-v8a, armeabi-v7a

# Caminho dos ícones e splash (opcional, se existirem)
presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png

# Tipo de build (debug = testes; release = publicação final)
android.debug = 1

# Logging
[buildozer]
log_level = 2
warn_on_root = 1

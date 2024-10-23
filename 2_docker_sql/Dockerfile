# Utilisation de l'image Python 3.12 (dernière version stable)
FROM python:3.12

# Installer pandas via pip
RUN pip install pandas

# Définir le répertoire de travail
WORKDIR /app

# Copier le script pipeline.py dans le répertoire de travail
COPY pipeline.py pipeline.py

# Définir l'entrypoint sur pour interagir avec le conteneur et fixe le comportement par défaut
ENTRYPOINT [ "python", "pipeline.py" ]
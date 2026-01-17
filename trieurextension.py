import os
import shutil

# Récupération du contenu du dossier Téléchargements
contenu_dossier_non_trie: list[str] = os.listdir("./Downloads")

# Préparation du tri
contenu_dossier: list[str] = []

# On ignore les fichiers cachés et les dossiers
for s in contenu_dossier_non_trie:
    if s[0]!='.' and '.' in s:
        contenu_dossier.append(s)

# Fonction pour récupérer l'extention d'un fichier
def get_extension(fichier: str) -> str:
    pointPasse: bool = False
    extension: str = ""

    for c in fichier:
        if c=='.':
            pointPasse = True
        if pointPasse:
            extension += c

    extension = extension[1:].upper()
    return extension

# Récupération de toutes les extentions
extensions: list[str] = []

for s in contenu_dossier:
    extension: str = get_extension(s)
    if extension not in extensions:
        extensions.append(extension)

# Création d'un dossier pour chaque extension
for s in extensions:
    if not os.path.exists("./Downloads/" + s):
        os.makedirs("./Downloads/" + s)

# Délacement des fichiers dans le bon repertoire
for fichier in contenu_dossier:
    shutil.move("./Downloads/" + fichier, "./Downloads/" + get_extension(fichier) + "/")

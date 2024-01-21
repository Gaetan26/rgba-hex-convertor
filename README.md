# rgba-hex-convertor
Convert RGBA color codes to HEXADECIMAL color codes 100% in python
Utilisez notre interface graphique intuitive pour convertir rapidement vos codes couleurs rgba vers hexadecimal ou haxadecimal vers rgba

## Comment utiliser?
1. Installez les dépendances
   > Pour donner un aspect appreciable, nous avons utiliser la bibliothèque `customtkinter` qui est une amélioration au niveau de la qualité de widgets de la bibiothèque classique `tkinter`. Ainsi vous aurez donc besoin d'installer `customtkinter` afin de pouvoir utiliser correctement le programme.
  Installer customtkinter depuis `pip` ou si vous préférez, [cloner le réferentiel github de customtkinter](https://github.com/Gaetan26)
   ```
    pip install customtkinter
    ```
2. Experimentez
   Une fois la bibliothèque `customtkinter` installée, vous pouvez lancer le programme grâce au fichier `main.py` avec une instruction ressemblant à `python main.py` selon les sytèmes _(Windows, Linux, MacOS)_ avec lequel vous travaillez.
   Une fois le programme lancé vous verrez appairaitre une interface graphique composé de :
   * Un texte d'appel à contribution au projet
   * Une ligne de trois champ de texte pour saisir le code couleur RGBA
     * R: pour la valeur du _R:red_
     * G: pour la valeur du _G:green_
     * B: pour la valeur du _B:blue_
     * A: pour la valeur du _A:alpha_
   * Un champ de texte pour saisir la valeur du code couleur HEXADECIMAL
     > _vous pouvez saisir le code couleur HEXADECIMAl avec ou sans le `#` du début_
     > _donc `#000fffff` donnera le même résultat que `000fffff`_
     > _aussi, vous pouvez saisir le code couleur RGBA et le code couleur HEXADECIMAL avec ou sans une valeur pour l'`alpha`, par défaut il sera remplacé par le maximum_
     > _donc `(0,130,230)` donnera le même résultat que `(0,130,203,255)` et `#b00020` donnera le même résultat que `#b00020ff`
   * Une instruction qui indique qu'il vous suffit de presser le button `return ~ enter` pour lancer la conversion
     > _si vous souhaitez effacez les contenus de tous les champs de textes, il vous suffit de presser le bouton `delete`_

### vous êtes prêt à utiliser le programme !

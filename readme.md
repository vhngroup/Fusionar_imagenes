# Fusionador de imagenes - Image Blending
| Imagen original 1         | Imangen Original 2       |
| :------------------------:|:------------------------:|
| ![Antes](https://github.com/vhngroup/Fusionar_imagenes/static/Original1.jpg) | ![Despues](https://github.com/vhngroup/Fusionar_imagenes/static/Original2.jpg) |
| :------------------------:|:------------------------:|
| ![Antes](https://github.com/vhngroup/Fusionar_imagenes/static/Demo1.jpg) | ![Despues](https://github.com/vhngroup/Fusionar_imagenes/static/imagen_fusionada.jpg) |
* Script creado en python para remover el fondo de las imagenes.
* Se ha utilizado la libreria *rembg* con la cual se retira el fondo de la images de formato jpg, png y jpeg.
* Las imagenes originales se deben ubicar en la carpeta input
* El script las procesara y genera la salida en la carpeta ouput, creando una nueva carpeta con la fecha y hora.

## Instrucciones:
* Se recomienda el uso de virtualenv
* Ejecutar el comando: pip install -r requirements.txt para instal las dependencias.
* Ubicar la imagenes a usar en la carpeta input.
* Ejecutar el script remove_background_image.py y ver el resultado.

## Creditos
Este Ejercicio fue realizado en base al canal: https://www.youtube.com/@pildorasdeprogramacion
# Fusionador de imagenes - Image Blending
| Imagen original 1         | Imangen Original 2       |
| :------------------------:|:------------------------:|
| ![Antes](https://github.com/vhngroup/Fusionar_imagenes/blob/main/static/Original1.jpg)|![Despues](https://github.com/vhngroup/Fusionar_imagenes/blob/main/static/Original2.jpg)|
| Imagen procesada 1          | Imagen procesada 2         |
| ![Antes](https://github.com/vhngroup/Fusionar_imagenes/blob/main/static/Demo1.jpg)|![Despues](https://github.com/vhngroup/Fusionar_imagenes/blob/main/static/imagen_fusionada.jpg)|
* Script creado en python para fusionar dos imagenes.
* Se ha utilizado la libreria *opencv* cv2 con la cual se ajusta el grado alpha y combina las dos imagenes.
* El script procesa las imagenes genera la imagen combinada y da la opccion de guardarla en la carpeta raiz.

## Instrucciones:
* Se recomienda el uso de virtualenv
* Ejecutar el comando: pip install -r requirements.txt para instalar las dependencias.
* Ejecutar el script streamlit run main.py
* Ingresar a la url indicada en la consola, seleccionar y cargar las imagenes
* Seleccionamos el nivel de gradiente Alpha desplazando la barra de selección.
* Realizamos click en generar
* Si no nos gusta el resultado, ajustamos la gradiente hasta quedar satisfechos.
* Finalmente guardamos el resultado y podremos usar la imagen.

## Creditos
Este Ejercicio fue realizado en base al canal: https://www.youtube.com/@CodigoEspinoza
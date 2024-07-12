import streamlit as st
import cv2
from PIL import Image
import numpy as np
import time

st.title("Fusionador de imagen")
gamma = 0.0
#imagen load and resize
st.session_state.disabled = True

#Funcion que redimenciona la imagen
def load_and_resize_image(uploaded_file, size=(500,500)):
    image = Image.open(uploaded_file)
    image = image.resize(size)
    return np.array(image) #retornamos un arreglo

#funcion que hace el degradada
def degradado(alpha):
    image_demo = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    return(image_demo)

#Cargamos la primera Imagen
uploaded_file1 = st.file_uploader("Selecciona la primera imagen", type=['jpg', 'jpeg', 'png'])
if uploaded_file1 is not None:
    img1 = load_and_resize_image(uploaded_file1)
    st.image(img1, caption='Primera Imagen', use_column_width=True)

#Cargamos la segunda imagen
uploaded_file2 = st.file_uploader("Selecciona la segunda imagen", type=['jpg', 'jpeg', 'png'])
if uploaded_file2 is not None:
    img2 = load_and_resize_image(uploaded_file2)
    st.image(img2, caption='Segunda Imagen', use_column_width=True)

#Damos el gradiente o alpha
alpha = st.slider ("Ingrese Alpha o transparencia(0 a 1)", 0.0, 1.0, 0.5)

#creamos el boton proceder y confirmamos si lo oprimen.
if st.button("Proceder"):
    if uploaded_file1 is not None and uploaded_file2 is not None: #Confrimamos que esten cargadas
        if img1.shape == img2.shape: #Confirmamos dimenciones iguales
            beta = 1 - alpha # Peso o porcentaje con el que difuminaremos la img2 vs la img1
            res = degradado(alpha)
            st.image(res, caption="Imagen Mezclada", use_column_width=True)
        else:
            print("Las imagenes deben tener el mismo tamaño.")
    else:
        print("Por favor verifique la carga de las 2 imagenes")

#Damos la opccion de guardar la imagen
filename = st.text_input("Nombre de la imagen")
if st.button("guardar"):
    if filename =="":
        filename = "imagen_fusionada"
    beta = 1 - alpha # Peso o porcentaje con el que difuminaremos la img2 vs la img1
    res = degradado(alpha)
    image_saved = filename + ".jpg"
    cv2.imwrite(image_saved, res)
    st.success("La imagen combinada ha sido guardada como " + image_saved)
    

if st.button("Mostrar Imagen Guardada"):
    try:
        saved_image = Image.open(image_saved)
        st.success(saved_image)
        st.image(saved_image, caption = 'Imagen Guardada', use_column_width=True)
    except:
        st.error("No hay Imagen")
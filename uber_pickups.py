import streamlit as st
import pandas as pd
import numpy as np

st.title('Proyecto multigrado')

st.subheader("Bienvenido a nuestro proyecto, te recordamos que :blue[no somos profesionales], porfavor consulta un medico especializado.")

dangert=0

dangerc=0
dangerb=0
dangera=0
contadorb=0
danger=0
contador=0
edad = st.slider('Introduce tu edad:', 0, 100, 0)
st.write("Tu edad es de: ", edad, 'años.')
edad=int(edad)
if edad<=25:
    dangerc=1
    st.subheader("Aun eres muy joven, cuidate.")
else :
    st.subheader("Cuidado, aun tiene una vida por delante.")


st.subheader("Alcohol")
with st.expander("-----"):
    f=st.caption("¿Consumes alcohol o otras drogas de efecto retardante?")
    if st.button('  Si '):
        f=1
        contadorb=contadorb + f
    g=st.caption("¿Consumes frecuentemente? ")
    if st.button('  Si  '):
        g=2
        contadorb=contadorb + g
    h=st.caption("¿Consumes más de una vez al mes? ")
    if st.button(' Si '):
        h=3
        contadorb=contadorb + h
    if contadorb==3:
        st.subheader("El alcohol es una droga de efecto retardante(que tiene el proposito de aletargarte o relajarte), que puede causar problemas en las partes del cerebro que controlan el equilibrio, la memoria, el habla y el juicio, porfavor recibe ayuda.")
    else:
        st.subheader("El alcohol puede parecer una buena idea ya que tiene efectos de relajacion, pero puede causar una adiccion muy facilmente.")


st.subheader("Alucinógenos")
with st.expander("------"):
    a=st.caption("¿Consumes alucinógenos? : ")
    if st.button('Si'):
        b=1
        contador=contador + b
    c=st.caption("¿Has consumido más de una vez? ")
    if st.button(' Si'):
        d=2
        contador = contador + d
    e=st.caption("¿Consumes más de una vez al mes? ")
    if st.button('Si '):
        e=3
        contador = contador + e
    if contador==3:
        st.subheader("Tambien conocidas como drogas psicodélicas y disociativas, pueden afectar a la forma en que el cerebro procesa la sustancia química llamada serotonina. Pueden provocar visiones vívidas y afectar el sentido de sí mismo de una persona, parece que necesita ayuda de un profecional.")
    else:
        st.subheader("Tambien conocidas como drogas psicodélicas y disociativas, pueden afectar a la forma en que el cerebro procesa la sustancia química llamada serotonina. Pueden provocar visiones vívidas y afectar el sentido de sí mismo de una persona")


st.subheader("Enfermedades")
with st.expander("-----"):
    options = st.multiselect(
    'Selecciones si alguien en su familia presenta alguna de estas enfermedades',
    ['Alucinaciones', 'Locura', 'Alzheimer', 'Esquizofrenia'])



if st.button(' Fin '):
    st.caption("----------")
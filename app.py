
import streamlit as st

st.title("¿Qué moto puedes comprar?")
st.write("Descubre qué motocicletas se ajustan a tu presupuesto.")

budget = st.number_input(
    "Introduce tu presupuesto:",
    min_value=0,
    step=50000
)

if st.button("Buscar motocicletas"):

    if budget >= 600000:
        st.success("Puedes comprar una Hypermotard 698, XADV 750 o Tiger 660.")

    elif budget >= 400000:
        st.success("Puedes comprar una Sahara 300 o CFMOTO 450.")

    elif budget >= 200000:
        st.success("Puedes comprar una V-Strom 250, Duke 200 o NS 400Z.")

    elif budget >= 100000:
        st.success("probablemente seas Kevin y puedes comprar una Boxer CT100.")

    else:
        st.warning("bro...")

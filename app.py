import json
from datetime import date
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Precio de propiedades", page_icon="🏠")

CARPETA = Path(__file__).parent
if not (CARPETA / "modelo.joblib").exists() or not (CARPETA / "info.json").exists():
    st.error("Faltan modelo.joblib o info.json. Súbanlos al repositorio, en la misma carpeta que app.py.")
    st.stop()

modelo = joblib.load(CARPETA / "modelo.joblib")
info = json.load(open(CARPETA / "info.json", encoding="utf-8"))
op = info["opciones"]

st.title(" Predicción del precio de una propiedad")
st.caption(f"Modelo: {info['modelo']} · R² {info['r2']:.2f} · error promedio ${info['mae']:,.0f}")

# 1. Entrada de datos del usuario
c1, c2 = st.columns(2)
localidad = c1.selectbox("Localidad", op["locality"])
tipo = c1.selectbox("Tipo de propiedad", op["property"])
residencial = c1.selectbox("Tipo residencial", op["residential"])
orientacion = c1.selectbox("Orientación", op["face"])
area = c2.number_input("Área habitable", min_value=50.0, value=1000.0, step=50.0)
habitaciones = c2.number_input("Habitaciones", min_value=1, value=3)
banos = c2.number_input("Baños", min_value=0, value=2)
impuesto = c2.number_input("Tasa de impuesto", min_value=0.0, value=1.3, step=0.01)
fecha = st.date_input("Fecha de venta", value=date.fromisoformat(info["ultima_fecha"]))

# 2. Ejecución del modelo en vivo (mismas variables que en el notebook)
if st.button("Estimar precio", type="primary"):
    datos = pd.DataFrame([{
        "carpet_area": area, "num_rooms": habitaciones, "num_bathrooms": banos,
        "property_tax_rate": impuesto, "sale_year": fecha.year, "sale_month": fecha.month,
        "area_per_room": area / habitaciones, "locality": localidad, "property": tipo,
        "residential": residencial, "face": orientacion,
    }])
    precio = modelo.predict(datos)[0]

    # 3. Visualización del resultado
    st.metric("Precio estimado", f"${precio:,.0f}")
    st.write(f"Margen de error típico del modelo (MAE): ± ${info['mae']:,.0f}")

    comparacion = pd.DataFrame({
        "Precio": [precio, info["mediana_localidad"][localidad]],
    }, index=["Esta propiedad", f"Mediana en {localidad}"])
    st.bar_chart(comparacion)

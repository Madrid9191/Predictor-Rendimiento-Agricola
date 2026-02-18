# ---------- FUNCIONES ----------
def predecir(modelo, columnas, pais, cultivo, año, lluvia, pesticida, temp):
    import pandas as pd

    entrada = pd.DataFrame(0, index=[0], columns=columnas)

    # Variables numéricas
    entrada['Year'] = año
    entrada['average_rain_fall_mm_per_year'] = lluvia
    entrada['Pesticidas_ton'] = pesticida
    entrada['avg_temp'] = temp

    # Variables categóricas (One-Hot)
    entrada[f'Pais_{pais}'] = 1
    entrada[f'Cultivo_{cultivo}'] = 1

    return modelo.predict(entrada)[0]


# ---------- IMPORTS ----------
import streamlit as st
import pandas as pd
import joblib


# ---------- CARGAR MODELO ----------
modelo = joblib.load('model/modelo_rf.pkl')
columnas = joblib.load('model/columnas_modelo.pkl')


# ---------- EXTRAER OPCIONES DESDE EL MODELO ----------
paises = sorted(
    col.replace('Pais_', '')
    for col in columnas
    if col.startswith('Pais_')
)

cultivos = sorted(
    col.replace('Cultivo_', '')
    for col in columnas
    if col.startswith('Cultivo_')
)


# ---------- CONFIGURACIÓN DE LA APP ----------
st.set_page_config(
    page_title="Predictor de Rendimiento Agrícola",
    layout="centered"
)

st.title("🌾 Predictor de Rendimiento de Cosecha")
st.write(
    "Modelo de Machine Learning para estimar el rendimiento agrícola "
    "en función del clima y el uso de pesticidas."
)


# ---------- INPUTS PRINCIPALES ----------
pais = st.selectbox("🌍 País", paises, index=paises.index("Mexico"))
cultivo = st.selectbox("🌱 Cultivo", cultivos, index=cultivos.index("Maize"))

año = st.number_input("📅 Año", min_value=1960, max_value=2030, value=2025)
lluvia = st.number_input("💧 Lluvia anual (mm)", min_value=0.0, value=1000.0)
pesticida = st.number_input("🧪 Pesticidas (ton)", min_value=0.0, value=5000.0)
temp = st.number_input("🌡️ Temperatura promedio (°C)", value=24.0)


# ---------- PREDICCIÓN BASE ----------
st.markdown("### 🔮 Predicción base")

if st.button("Predecir rendimiento"):
    rendimiento_base = predecir(
        modelo, columnas,
        pais, cultivo, año,
        lluvia, pesticida, temp
    )

    st.success(
        f"🌱 Rendimiento estimado: **{rendimiento_base:.2f} ton/ha**"
    )


# ---------- COMPARACIÓN DE ESCENARIOS ----------
st.markdown("---")
st.subheader("🔍 Comparación de escenarios")
st.write(
    "Simula cambios en las condiciones para analizar su impacto "
    "en el rendimiento."
)

# Sliders de cambio
delta_lluvia = st.slider(
    "Cambio en lluvia (mm)",
    min_value=-500,
    max_value=500,
    value=0,
    step=50
)

delta_temp = st.slider(
    "Cambio en temperatura (°C)",
    min_value=-3.0,
    max_value=3.0,
    value=0.0,
    step=0.5
)

delta_pesticida = st.slider(
    "Cambio en pesticidas (ton)",
    min_value=-3000,
    max_value=3000,
    value=0,
    step=500
)

# Botón de comparación
if st.button("📊 Comparar escenarios"):
    rendimiento_base = predecir(
        modelo, columnas,
        pais, cultivo, año,
        lluvia, pesticida, temp
    )

    rendimiento_alternativo = predecir(
        modelo, columnas,
        pais, cultivo, año,
        lluvia + delta_lluvia,
        pesticida + delta_pesticida,
        temp + delta_temp
    )

    diferencia = rendimiento_alternativo - rendimiento_base

    # Resultados
    st.markdown("### 📋 Resultados")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🌱 Escenario base (ton/ha)",
            f"{rendimiento_base:.2f}"
        )

    with col2:
        st.metric(
            "🔄 Escenario alternativo (ton/ha)",
            f"{rendimiento_alternativo:.2f}",
            delta=f"{diferencia:+.2f}"
        )

    # Interpretación automática
    if diferencia > 0:
        st.success(
            f"📈 El escenario alternativo **mejora** el rendimiento "
            f"en {diferencia:.2f} ton/ha."
        )
    elif diferencia < 0:
        st.warning(
            f"📉 El escenario alternativo **reduce** el rendimiento "
            f"en {abs(diferencia):.2f} ton/ha."
        )
    else:
        st.info("➖ No se observa cambio en el rendimiento.")

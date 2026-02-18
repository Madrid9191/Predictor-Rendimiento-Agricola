# 🌾 Predictor de Rendimiento Agrícola

Aplicación de **Machine Learning** desarrollada con **Python y Streamlit** que predice el **rendimiento de cultivos (toneladas por hectárea)** a partir de variables climáticas, uso de pesticidas, país y tipo de cultivo.

El modelo está entrenado con datos históricos reales y utiliza **Random Forest Regressor** para capturar relaciones no lineales entre clima y producción agrícola.

---

## 🚀 Demo en línea

👉 **App desplegada en Streamlit Cloud**  
(agrega aquí la URL cuando termine el deploy)

---

## 📊 Variables utilizadas

La predicción se basa en las siguientes variables:

- 🌍 **País**
- 🌱 **Cultivo**
- 📅 **Año**
- 🌧️ **Precipitación anual promedio (mm)**
- 🧪 **Uso de pesticidas (toneladas)**
- 🌡️ **Temperatura promedio (°C)**

---

## 🧠 Modelo de Machine Learning

- Algoritmo: **Random Forest Regressor**
- Librería: `scikit-learn`
- Tipo de problema: **Regresión**
- Salida: **Rendimiento agrícola (ton/ha)**

El modelo entrenado se guarda usando **Joblib** y se versiona con **Git LFS** debido a su tamaño.

---

## Instalación local
**Clonar el repositorio**

git clone https://github.com/Madrid9191/Predictor-Rendimiento-Agricola.git
cd Predictor-Rendimiento-Agricola/CYP

**Crear entorno virtual**

python -m venv venv


Activar en Windows:

venv\Scripts\activate

**Instalar dependencias**

pip install -r requirements.txt

**Ejecutar la app**

streamlit run app.py

---

## 🗂️ Estructura del proyecto

```text
Predictor-Rendimiento-Agricola/
│
├── CYP/
│   ├── app.py                  # Aplicación Streamlit
│   ├── train_model.py          # Entrenamiento del modelo
│   ├── requirements.txt        # Dependencias
│   └── model/
│       ├── modelo_rf.pkl        # Modelo entrenado (Git LFS)
│       └── columnas_modelo.pkl  # Columnas del modelo
│
├── .gitignore
├── .gitattributes
└── README.md

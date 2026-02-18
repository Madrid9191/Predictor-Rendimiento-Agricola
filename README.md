# 🌾 Predictor de Rendimiento Agrícola

Aplicación interactiva desarrollada en **Python** y **Streamlit** que utiliza **Machine Learning** para predecir el rendimiento de cultivos agrícolas en función de variables climáticas y de manejo, como la lluvia, la temperatura y el uso de pesticidas.

El proyecto permite además **comparar escenarios**, respondiendo preguntas del tipo:
> *¿Qué pasaría con el rendimiento si aumenta la lluvia o cambia la temperatura?*

---

## 🚀 Características principales

- 📊 Predicción de rendimiento (ton/ha)
- 🌍 Selección de país y cultivo mediante menús desplegables
- 🔍 Comparación de escenarios climáticos y de manejo
- 📈 Interpretación automática de resultados
- 🧠 Modelo basado en **Random Forest Regressor**
- 🖥️ Interfaz interactiva con **Streamlit**

---

## 🧠 Modelo de Machine Learning

- **Algoritmo:** Random Forest Regressor  
- **Variables de entrada:**
  - País
  - Cultivo
  - Año
  - Lluvia anual (mm)
  - Temperatura promedio (°C)
  - Uso de pesticidas (ton)
- **Variable objetivo:**
  - Rendimiento agrícola (ton/ha)

Las variables categóricas (país y cultivo) se transforman mediante **One-Hot Encoding**.

---

## 🔍 Comparación de escenarios

La aplicación permite simular cambios en:
- 🌧️ Lluvia
- 🌡️ Temperatura
- 🧪 Uso de pesticidas

y comparar:
- Rendimiento base
- Rendimiento alternativo
- Diferencia entre escenarios

Esto convierte la app en una **herramienta de apoyo a la toma de decisiones**.

---

## Cómo ejecutar el proyecto localmente

**Clonar el repositorio**

git clone https://github.com/Madrid9191/crop-yield-app.git

cd crop-yield-app

**Instalar dependencias**

pip install -r requirements.txt

**Entrenar el modelo (una sola vez)**

python train_model.py

**Ejecutar la aplicación**

streamlit run app.py

---

## 📁 Estructura del proyecto

```text
crop_yield_app/
│
├── app.py                  # Aplicación Streamlit
├── train_model.py          # Entrenamiento del modelo
├── requirements.txt        # Dependencias
│
├── data/
│   ├── pesticides.csv
│   ├── rainfall.csv
│   ├── temp.csv
│   └── yield.csv
│
└── model/
    ├── modelo_rf.pkl
    └── columnas_modelo.pkl





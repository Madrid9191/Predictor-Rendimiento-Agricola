# 🌾 Predictor de Rendimiento Agrícola

Aplicación de **Machine Learning** desarrollada con **Python y Streamlit** que predice el **rendimiento de cultivos (toneladas por hectárea)** a partir de variables climáticas, uso de pesticidas, país y tipo de cultivo.

El modelo está entrenado con datos históricos reales y utiliza **Random Forest Regressor** para capturar relaciones no lineales entre clima y producción agrícola.


---
### Quick links:

Data source: [Crop Yield Prediction Dataset](https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset)

[Data exploration](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/exploracion.PNG)

[Data cleaning-PreMerge](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/limpieza.PNG)

[Data cleaning-Merge](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/merge.PNG)

[Data cleaning-PostMerge](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/postmerge.PNG)

[One-Hot](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/onehot.PNG)

[Modelo](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/modelo.PNG)


## 🚀 Demo en línea

👉 **App desplegada en Streamlit Cloud**  
([Enlace a la aplicacion](https://crop-yield-ml.streamlit.app/))

---
## Data source

El data set usado fue "Crop Yield Prediction Dataset" obtenido en [Kaggle](https://www.kaggle.com/datasets/patelris/crop-yield-prediction-dataset) cuya informacion se obtuvo de FAO (Food and Agriculture Organization) y World Data Bank. Se descargaron cuatro csv´s de este data set ["pesticides.csv"](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/pesticides.csv), ["yield.csv"](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/yield.csv), ["temp.cvs"](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/temp.csv) y ["rainfall.csv"](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/rainfall.csv) 

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
## Data exploration

[Data exploration](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/train_model.py)

Los cuatro archivos csv fueron cargados y convertidos a data frame para trabajar con ellos. La exploración de los datos permitió encontrar inconsistencias en los nombres de las columnas. Pesticidas (p), Lluvia (r) y Rendimiento (y) usan "Area" y "Year" y Temperatura (t) usa "country" y "year" (en minúsculas), mientras que las tablas Rendimiento (y) y Pesticidas (p) tienen una columna con el mismo nombre Valor. También  la columna average_rain_fall_mm_per_year en el data frame de Lluvia es de tipo object (texto), no número. Por otra parte la columna Área de la tabla Lluvia tiene espacios extras, es ¨ Area¨ no ¨Area¨. Asimismo se encontró que la tabla Lluvia tiene casi 800 valores faltantes y la tabla Temperatura tiene unos 2,500 valores faltantes. Mientras que en la tabla de Rendimiento la columna Valor tiene los valores en hectogramos (hg/ha) por lo que deben ser cambiados a toneladas (ton/ha) para que los resultados sean fáciles de interpretar. Por último, como en la tabla de Temperatura (t), hay muchos registros para el mismo país y el mismo año.

![](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/temperatura.PNG)

![](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/rendimiento.PNG)

![](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/pesticidas.PNG)

![](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/lluvia.PNG)


---
## Data cleaning

[Data cleaning](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/train_model.py)

- Todas las filas con valores nulos fueron borrados
- En total se borraron 3300 filas
- Se eliminaron los espacios extra
- Se estandarizaron los nombres de las columnas "country" y "year" para coincidir con los nombres usados en las demás
- Se reemplazó la temperatura por la temperatura promedio por país y año
- En la tabla Rendimiento (y) se cambió el nombre de la columna Valor por Rendimiento_hg_ha
- En la tabla Pesticidas (p) se cambió el nombre de la columna Valor por Pesticidas_ton
- Las columnas Área y Year se usaron para hacer merge (unir las tablas) 
- La columna Valor de la tabla Rendimiento (y) se transformado de hg/ha a  ton/ha
- Se usó el método One Hot para convertir las columnas Pais y Cultivo de variables categóricas a variables continuas  
- Se borraron todas las columnas innecesarias y se dejaron solo 'Area', 'Item', 'Year', 'Rendimiento_ton_ha', 'Pesticidas_ton', 'average_rain_fall_mm_per_year', y 'avg_temp'

---
## 🧠 Modelo de Machine Learning

- Algoritmo: **Random Forest Regressor**
- Librería: `scikit-learn`
- Tipo de problema: **Regresión**
- Salida: **Rendimiento agrícola (ton/ha)**

El modelo entrenado se guarda usando **Joblib** y se versiona con **Git LFS** debido a su tamaño.

## ¿Por qué Random Forest?

El algoritmo elegido para el modelo fue Random Fores, el cual es uno de los algoritmos más potentes y populares en Machine Learning. Para entenderlo, primero debemos entender qué es un Árbol de Decisión.

Un árbol de decisión es como un diagrama de flujo que toma decisiones basadas en preguntas simples (ej. "¿La temperatura es mayor a 25°C?" → Sí/No). Aunque son fáciles de entender, tienen un problema: suelen ser muy inestables y se "memorizan" los datos de entrenamiento demasiado rápido (sobreajuste).

Como su nombre lo indica, es una colección de muchos árboles de decisión trabajando juntos. En lugar de confiar en lo que dice un solo árbol, el algoritmo crea un "bosque" y hace que todos voten para llegar a un resultado final.

Se eligió el Random Forest porque en la agricultura, las variables no siempre tienen una relación de "a más, mejor". Por ejemplo, un poco más de lluvia ayuda al cultivo, pero demasiada lluvia lo ahoga. Random Forest es excelente detectando estos patrones complejos y curvas que una regresión lineal simple no podría ver. También porque reduce del Overfitting (Sobreajuste).

## Entrenar el Modelo
[Entrenar el Modelo](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/train_model.py)
Antes de usar el algoritmo se estableció la variable a predecir que serían las toneladas del cultivo y las variables que servirán para predecir. Una vez establecidas se usó ¨RandomForestRegressor¨. Se usa la versión "Regressor" porque el objetivo es predecir un número continuo (toneladas de cultivo) y no una categoría (como "maíz" o "frijol"). 

Al finalizar el entrenamiento se guardó el modelo y también los nombres de las columnas.

![](https://github.com/Madrid9191/Predictor-Rendimiento-Agricola/blob/main/CYP/modelo.PNG)

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

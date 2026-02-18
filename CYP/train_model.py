import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

# ---------- CARGA ----------
p = pd.read_csv('pesticides.csv')
r = pd.read_csv('rainfall.csv')
t = pd.read_csv('temp.csv')
y = pd.read_csv('yield.csv')

# ---------- LIMPIEZA ----------
for df in [p, r, t, y]:
    df.columns = df.columns.str.strip()

r['average_rain_fall_mm_per_year'] = pd.to_numeric(
    r['average_rain_fall_mm_per_year'], errors='coerce'
)

r = r.dropna(subset=['average_rain_fall_mm_per_year'])
t = t.dropna(subset=['avg_temp'])

t = t.rename(columns={'year': 'Year', 'country': 'Area'})

# ---------- MERGE ----------
t_avg = t.groupby(['Year', 'Area'])['avg_temp'].mean().reset_index()

y = y[['Area', 'Item', 'Year', 'Value']].rename(
    columns={'Value': 'Rendimiento_hg_ha'}
)
p = p[['Area', 'Year', 'Value']].rename(
    columns={'Value': 'Pesticidas_ton'}
)

df = pd.merge(y, r, on=['Area', 'Year'])
df = pd.merge(df, p, on=['Area', 'Year'])
df = pd.merge(df, t_avg, on=['Area', 'Year'])

df['Rendimiento_ton_ha'] = df['Rendimiento_hg_ha'] / 10000

df = df[['Area', 'Item', 'Year', 'Rendimiento_ton_ha',
         'Pesticidas_ton', 'average_rain_fall_mm_per_year', 'avg_temp']]

# ---------- ONE HOT ----------
df_ml = pd.get_dummies(df, columns=['Area', 'Item'],
                       prefix=['Pais', 'Cultivo'])

y_target = df_ml['Rendimiento_ton_ha']
X = df_ml.drop('Rendimiento_ton_ha', axis=1)

# ---------- ENTRENAR ----------
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X, y_target)

# ---------- GUARDAR ----------
joblib.dump(modelo, 'model/modelo_rf.pkl')
joblib.dump(list(X.columns), 'model/columnas_modelo.pkl')

print("✅ Modelo entrenado y guardado")

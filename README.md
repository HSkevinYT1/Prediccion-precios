# Predicción de Precios Inmobiliarios

Proyecto de Inteligencia Artificial — UNAB. Predice el precio de venta de una propiedad con regresión supervisada y lo muestra en una app de Streamlit.

**App:** (https://prediccion-precios-bfkcqwy2k5hjtmbehrrvno.streamlit.app/) · **Dataset:** [Kaggle — Real Estate Property Transactions](https://www.kaggle.com/datasets/subhiarjaria09/real-estate-property-transactions-dataset)

## Archivos
| Archivo | Qué es |
|---|---|
| `Proyecto_Precios.ipynb` | Notebook: limpieza, EDA, PCA, modelos y resultados |
| `app.py` | App de Streamlit |
| `modelo.joblib` | Modelo entrenado (Random Forest + preprocesamiento) |
| `info.json` | Opciones de la app y métricas del modelo |
| `requirements.txt` | Librerías que necesita la app |

## Resultados (test con el 20% de ventas más recientes)
| Modelo | RMSE | MAE | R² |
|---|---|---|---|
| **Random Forest** | **668,181** | **289,131** | **0.383** |
| Regresión Lineal | 668,233 | 289,345 | 0.383 |
| Random Forest + PCA | 756,203 | 316,269 | 0.209 |
| Regresión Lineal + PCA | 852,466 | 385,623 | -0.005 |

La variable que más influye en el precio es la localidad.

## Ejecutar la app localmente
```
pip install -r requirements.txt
streamlit run app.py
```

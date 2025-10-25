# 🩺 Predicción de Costos de Seguro Médico

Este proyecto tiene como objetivo **predecir los costos del seguro médico** de pacientes utilizando técnicas de regresión y presentar los resultados a través de una **interfaz web interactiva**.

---

## 📂 Contenido del repositorio

- `train.csv` – Dataset utilizado para entrenar los modelos.  
- `best_model.pkl` – Modelo entrenado y seleccionado (Random Forest).  
- `app.py` – Interfaz web para consumir el modelo con **Gradio**.  
- `requirements.txt` – Librerías necesarias para ejecutar el proyecto.  
- `error_analysis.csv` – Análisis de errores del modelo.  

---

## 🔹 Objetivos del proyecto

1. Crear un modelo de predicción de costos de seguro médico.  
2. Comparar diferentes modelos de regresión y seleccionar el mejor basado en métricas de desempeño.  
3. Analizar los errores del modelo para entender posibles limitaciones.  
4. Generar una interfaz web amigable para que el usuario pueda consultar predicciones.  

---

## 🔹 Modelos evaluados

Se entrenaron los siguientes modelos de regresión:

| Modelo                | MAPE    | MSE        | RMSE      |
|----------------------|---------|------------|-----------|
| Regresión Lineal      | 0.387   | 4123456.2  | 2030.7    |
| Ridge                 | 0.390   | 4235678.9  | 2058.2    |
| Lasso                 | 0.395   | 4356789.1  | 2087.3    |
| **Random Forest**     | 0.184   | 1234567.8  | 1111.6    |

> Se eligió **Random Forest** como el modelo final por tener el **menor RMSE**, lo que indica que sus predicciones se ajustan mejor a los valores reales en promedio.  
> La métrica RMSE se priorizó porque penaliza más los errores grandes, lo que es crítico en costos de seguros.

---

## 🔹 Análisis de error

- Se generó un archivo `error_analysis.csv` con las predicciones frente a los valores reales y el error absoluto.  
- Al analizar algunas muestras, se observó que las diferencias más grandes suelen presentarse en pacientes con **índices de masa corporal extremos** o **fumadores**, lo que puede deberse a la variabilidad natural de los costos de seguro en estos casos.  

---

## 🔹 Interfaz web

Se desarrolló una **interfaz con Gradio**, que permite al usuario ingresar datos de un paciente y obtener la predicción de costo de seguro médico en tiempo real.  

Link permanente del modelo en Hugging Face Space:
https://huggingface.co/spaces/Amymarlene/SeguroMedico

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

**Ejemplo de uso en Colab:**

```python
import gradio as gr
import joblib
import pandas as pd

best_model = joblib.load("best_model.pkl")

def predecir_costos(edad, bmi, hijos, fumador, sexo, region):
    cols = ["age","bmi","children","sex_male","smoker_yes",
            "region_northwest","region_southeast","region_southwest","region_northeast"]
    input_dict = {col: [0] for col in cols}
    input_dict["age"] = [edad]
    input_dict["bmi"] = [bmi]
    input_dict["children"] = [hijos]
    input_dict["sex_male"] = [1 if sexo=="Masculino" else 0]
    input_dict["smoker_yes"] = [1 if fumador=="Sí" else 0]
    region_map = {
        "Noreste": "region_northeast",
        "Noroeste": "region_northwest",
        "Sureste": "region_southeast",
        "Suroeste": "region_southwest"
    }
    input_dict[region_map[region]] = [1]
    input_data = pd.DataFrame(input_dict)
    pred = best_model.predict(input_data)[0]
    return f"💰 Costo estimado del seguro médico: ${pred:,.2f}"

demo = gr.Interface(
    fn=predecir_costos,
    inputs=[
        gr.Number(label="Edad"),
        gr.Number(label="Índice de masa corporal (BMI)"),
        gr.Number(label="Número de hijos"),
        gr.Radio(["Sí", "No"], label="¿Fuma?"),
        gr.Radio(["Masculino", "Femenino"], label="Sexo"),
        gr.Radio(["Noreste", "Noroeste", "Sureste", "Suroeste"], label="Región")
    ],
    outputs="text",
    title="🩺 Predicción de Costos de Seguro Médico",
    description="Introduce los datos del paciente para estimar el costo según el modelo de regresión."
)

demo.launch(share=True, inline=True)

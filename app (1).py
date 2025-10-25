import pandas as pd
import joblib
import gradio as gr
from sklearn.linear_model import LinearRegression

# -------------------------------
# Cargar o entrenar modelo
# -------------------------------
try:
    model = joblib.load("best_model.pkl")
except:
    # Dataset de ejemplo para entrenar LinearRegression rápido
    url = "https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv"
    data = pd.read_csv(url)
    data_encoded = pd.get_dummies(data, drop_first=True)

    X = data_encoded.drop("charges", axis=1)
    y = data_encoded["charges"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "best_model.pkl")

# -------------------------------
# Función de predicción
# -------------------------------
def predecir_costos(edad, bmi, hijos, fumador, sexo, region):
    # Columnas que espera el modelo
    cols = ["age","bmi","children","sex_male","smoker_yes",
            "region_northwest","region_southeast","region_southwest","region_northeast"]

    input_dict = {col: [0] for col in cols}

    input_dict["age"] = [edad]
    input_dict["bmi"] = [bmi]
    input_dict["children"] = [hijos]
    input_dict["sex_male"] = [1 if sexo=="Masculino" else 0]
    input_dict["smoker_yes"] = [1 if fumador=="Sí" else 0]

    # Asignar correctamente la columna de región
    region_map = {
        "Noreste": "region_northeast",
        "Noroeste": "region_northwest",
        "Sureste": "region_southeast",
        "Suroeste": "region_southwest"
    }
    input_dict[region_map[region]] = [1]

    input_data = pd.DataFrame(input_dict)

    # Predicción
    try:
        pred = model.predict(input_data)[0]
        return f"💰 Costo estimado del seguro médico: ${pred:,.2f}"
    except Exception as e:
        return f"Error al predecir: {e}"

# -------------------------------
# Interfaz Gradio
# -------------------------------
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
    description="Introduce los datos del paciente para estimar el costo según un modelo LinearRegression."
)

demo.launch()

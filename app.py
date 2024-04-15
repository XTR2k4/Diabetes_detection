import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model using pickle
with open("diabetes-prediction-model.pkl", "rb") as pickle_in:  # Replace with your model filename
  model = pickle.load(pickle_in)

def predict_diabetes(data):
  """
  Makes a prediction using the loaded diabetes model.

  Args:
      data: A Pandas DataFrame containing the user input features.

  Returns:
      A string indicating the predicted outcome (diabetic or non-diabetic).
  """
  prediction = model.predict(data)[0]
  if prediction == 1:
    return "Diabetic"
  else:
    return "Non-diabetic"

st.title("Diabetes Prediction App")

# User input fields
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level (mg/dL)", min_value=0)
blood_pressure = st.number_input("Blood Pressure (mmHg)", min_value=0)
skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0)
insulin = st.number_input("Insulin Level (mu U/mL)", min_value=0)
bmi = st.number_input("Body Mass Index (BMI)")
diabetes_pedigree = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age (years)", min_value=0)

# Create a DataFrame from user inputs
data = pd.DataFrame({
  "Pregnancies": [pregnancies],
  "Glucose": [glucose],
  "BloodPressure": [blood_pressure],
  "SkinThickness": [skin_thickness],
  "Insulin": [insulin],
  "BMI": [bmi],
  "DiabetesPedigreeFunction": [diabetes_pedigree],
  "Age": [age]
})

# Prediction button
if st.button("Predict"):
  prediction = predict_diabetes(data)
  st.success(f"Prediction: {prediction}")

# Display additional information (optional)
st.write("Note:")
st.write("This is a simple app for demonstration purposes only. It should not be used for medical diagnosis. Please consult a healthcare professional for any concerns about diabetes.")

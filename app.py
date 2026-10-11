import random
import joblib
import pandas as pd
import streamlit as st

# Chargement du modèle
model = joblib.load("best_random_forest.joblib")

st.title("🍷 Prédiction de la Qualité du Vin")

# 1. Initialisation des valeurs par défaut dans le session_state
if "wine_data" not in st.session_state:
  st.session_state.wine_data = {
      "fixed_acidity": 7.4,
      "volatile_acidity": 0.7,
      "citric_acid": 0.0,
      "residual_sugar": 1.9,
      "chlorides": 0.076,
      "free_sulfur_dioxide": 11.0,
      "total_sulfur_dioxide": 34.0,
      "density": 0.9978,
      "pH": 3.51,
      "sulphates": 0.56,
      "alcohol": 9.4,
      "color": "Rouge",
  }


# 2. Fonction pour générer des caractéristiques aléatoires
def randomize_features():
  st.session_state.wine_data = {
      "fixed_acidity": round(random.uniform(4.0, 15.0), 2),
      "volatile_acidity": round(random.uniform(0.1, 1.2), 2),
      "citric_acid": round(random.uniform(0.0, 0.8), 2),
      "residual_sugar": round(random.uniform(0.6, 15.0), 2),
      "chlorides": round(random.uniform(0.01, 0.2), 3),
      "free_sulfur_dioxide": round(random.uniform(1.0, 70.0), 1),
      "total_sulfur_dioxide": round(random.uniform(6.0, 250.0), 1),
      "density": round(random.uniform(0.989, 1.003), 4),
      "pH": round(random.uniform(2.8, 4.0), 2),
      "sulphates": round(random.uniform(0.3, 1.2), 2),
      "alcohol": round(random.uniform(8.5, 14.5), 1),
      "color": random.choice(["Rouge", "Blanc"]),
  }


# Bouton de tirage aléatoire (en dehors du formulaire)
st.button("🎲 Générer un vin aléatoire", on_click=randomize_features)

# 3. Formulaire avec les valeurs liées au session_state
with st.form("Entrez les informations de votre vin"):
  fixed_acidity = st.number_input(
      "Acidité fixe",
      min_value=3.0,
      max_value=16.0,
      value=st.session_state.wine_data["fixed_acidity"],
  )
  volatile_acidity = st.number_input(
      "Acidité volatile",
      min_value=0.1,
      max_value=2.0,
      value=st.session_state.wine_data["volatile_acidity"],
  )
  citric_acid = st.number_input(
      "Acide citrique",
      min_value=0.0,
      max_value=1.0,
      value=st.session_state.wine_data["citric_acid"],
  )
  residual_sugar = st.number_input(
      "Sucre résiduel",
      min_value=0.5,
      max_value=20.0,
      value=st.session_state.wine_data["residual_sugar"],
  )
  chlorides = st.number_input(
      "Chlorures",
      min_value=0.01,
      max_value=0.6,
      value=st.session_state.wine_data["chlorides"],
  )
  free_sulfur_dioxide = st.number_input(
      "Dioxyde de soufre libre",
      min_value=1.0,
      max_value=72.0,
      value=st.session_state.wine_data["free_sulfur_dioxide"],
  )
  total_sulfur_dioxide = st.number_input(
      "Dioxyde de soufre total",
      min_value=6.0,
      max_value=300.0,
      value=st.session_state.wine_data["total_sulfur_dioxide"],
  )
  density = st.number_input(
      "Densité",
      min_value=0.98,
      max_value=1.05,
      value=st.session_state.wine_data["density"],
  )
  pH = st.number_input(
      "pH",
      min_value=2.5,
      max_value=4.5,
      value=st.session_state.wine_data["pH"],
  )
  sulphates = st.number_input(
      "Sulfates",
      min_value=0.2,
      max_value=2.0,
      value=st.session_state.wine_data["sulphates"],
  )
  alcohol = st.number_input(
      "Alcool (% vol)",
      min_value=8.0,
      max_value=15.0,
      value=st.session_state.wine_data["alcohol"],
  )

  # Choix de la couleur
  color_index = 1 if st.session_state.wine_data["color"] == "Blanc" else 0
  color_str = st.selectbox(
      "Couleur du vin", options=["Rouge", "Blanc"], index=color_index
  )

  soumis = st.form_submit_button("Évaluer la qualité")

# 4. Inférence au clic
if soumis:
  color_encoded = 1 if color_str == "Blanc" else 0

  df_input = pd.DataFrame([{
      "fixed acidity": fixed_acidity,
      "volatile acidity": volatile_acidity,
      "citric acid": citric_acid,
      "residual sugar": residual_sugar,
      "chlorides": chlorides,
      "free sulfur dioxide": free_sulfur_dioxide,
      "total sulfur dioxide": total_sulfur_dioxide,
      "density": density,
      "pH": pH,
      "sulphates": sulphates,
      "alcohol": alcohol,
      "color": color_encoded,
  }])

  prediction = model.predict(df_input)[0]
  proba = model.predict_proba(df_input)[0][1]

  if prediction == 1:
    st.success(f"🎉 **Vin de Haute Qualité !** (Probabilité : {proba:.1%})")
  else:
    st.info(f"🍷 **Vin Ordinaire.** (Probabilité d'être bon : {proba:.1%})")
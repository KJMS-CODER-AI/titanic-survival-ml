import joblib
import numpy as np

# Charger le modèle et le scaler
model = joblib.load("model_titanic.pkl")
scaler = joblib.load("scaler_titanic.pkl")

print("=== Prédicteur de survie Titanic ===\n")

# Poser les questions à l'utilisateur
pclass   = int(input("Classe du billet (1, 2 ou 3) : "))
sex      = input("Sexe (male/female) : ").strip().lower()
age      = float(input("Age : "))
sibsp    = int(input("Nb frères/soeurs/conjoint à bord : "))
parch    = int(input("Nb parents/enfants à bord : "))
fare     = float(input("Prix du billet : "))
embarked = input("Port embarquement (S/C/Q) : ").strip().upper()

# Encoder comme on a fait dans le notebook
sex_enc      = 0 if sex == "male" else 1
embarked_enc = {"S": 0, "C": 1, "Q": 2}.get(embarked, 0)
family_size  = sibsp + parch + 1
is_alone     = 1 if family_size == 1 else 0

# Créer le tableau de features
X = np.array([[pclass, sex_enc, age, sibsp, parch,
               fare, embarked_enc, family_size, is_alone]])

# Normaliser
X = scaler.transform(X)

# Prédire
prediction   = model.predict(X)[0]
probabilite  = model.predict_proba(X)[0][1]

print("\n--- Résultat ---")
if prediction == 1:
    print(f"Survécu ! (probabilité : {probabilite:.1%})")
else:
    print(f"N'a pas survécu (probabilité de survie : {probabilite:.1%})")
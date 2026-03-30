# 🚢 Titanic Survival Prediction - Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)
![ML](https://img.shields.io/badge/Machine%20Learning-Classification-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

---

## 📖 Description

Ce projet de Machine Learning prédit si un passager du Titanic a **survécu ou non** à la tragédie du 15 avril 1912.  
En utilisant des algorithmes de classification, le modèle analyse les caractéristiques des passagers (âge, sexe, classe, etc.) pour estimer leur probabilité de survie.

> *"Women and children first"* — Ce projet explore les données réelles pour valider ou infirmer ce genre de patterns.

---

## 🎯 Objectif

| Objectif | Détail |
|---|---|
| 🔍 Problème | Classification binaire (Survécu / Non survécu) |
| 📊 Dataset | Titanic - Machine Learning from Disaster |
| 🤖 Type de ML | Supervised Learning |
| 📈 Métrique | Accuracy, Precision, Recall, F1-Score |

---

## 📁 Structure du Projet

```
titanic_ml/
│
├── 📓 titanic.ipynb         # Notebook principal (EDA + Modèle)
├── 📄 titanic.csv           # Dataset des passagers
├── 🐍 predict.py            # Script de prédiction
├── 📦 model_titanic.pkl     # Modèle ML entraîné (sauvegardé)
└── 📦 scaler_titanic.pkl    # Scaler pour la normalisation
```

---

## 📊 Variables du Dataset

| Variable | Description | Type |
|---|---|---|
| `PassengerId` | Identifiant unique du passager | Numérique |
| `Survived` | Survie (0 = Non, 1 = Oui) | Cible 🎯 |
| `Pclass` | Classe du billet (1, 2, 3) | Catégorielle |
| `Name` | Nom du passager | Texte |
| `Sex` | Sexe du passager | Catégorielle |
| `Age` | Âge en années | Numérique |
| `SibSp` | Nb de frères/sœurs/conjoints à bord | Numérique |
| `Parch` | Nb de parents/enfants à bord | Numérique |
| `Ticket` | Numéro de ticket | Texte |
| `Fare` | Prix du billet | Numérique |
| `Cabin` | Numéro de cabine | Texte |
| `Embarked` | Port d'embarquement (C, Q, S) | Catégorielle |

---

## ⚙️ Étapes du Projet

| Étape | Description | Statut |
|---|---|---|
| 1️⃣ | Chargement et exploration des données (EDA) | ✅ Fait |
| 2️⃣ | Nettoyage des données (valeurs manquantes) | ✅ Fait |
| 3️⃣ | Feature Engineering | ✅ Fait |
| 4️⃣ | Entraînement du modèle | ✅ Fait |
| 5️⃣ | Évaluation des performances | ✅ Fait |
| 6️⃣ | Sauvegarde du modèle (.pkl) | ✅ Fait |

---

## 🤖 Modèle Utilisé

| Paramètre | Valeur |
|---|---|
| Algorithme | Classification (Random Forest / Logistic Regression) |
| Librairie | Scikit-learn |
| Normalisation | StandardScaler |
| Sauvegarde | Pickle (.pkl) |

---

## 🚀 Comment utiliser ce projet ?

### 1. Clone le dépôt
```bash
git clone https://github.com/KJMS-CODER-AI/titanic-survival-ml.git
cd titanic-survival-ml
```

### 2. Installe les dépendances
```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

### 3. Lance le Notebook
```bash
jupyter notebook titanic.ipynb
```

### 4. Faire une prédiction
```bash
python predict.py
```

---

## 📈 Résultats

| Métrique | Score |
|---|---|
| ✅ Accuracy | À compléter |
| 🎯 Precision | À compléter |
| 🔁 Recall | À compléter |
| 📊 F1-Score | À compléter |

---

## 🛠️ Technologies utilisées

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=for-the-badge&logo=Jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)

---

## 👤 Auteur

**KJMS-CODER-AI**  
🔗 [GitHub Profile](https://github.com/KJMS-CODER-AI)

---

## 📜 Licence

Ce projet est open source et disponible sous licence [MIT](LICENSE).

---

⭐ **N'oublie pas de mettre une étoile si ce projet t'a aidé !** ⭐

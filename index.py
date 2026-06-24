import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, RandomizedSearchCV

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

from imblearn.over_sampling import SMOTE


# ==========================================
# 1. LOAD DATA
# ==========================================

df = pd.read_csv("creditcard.csv")

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("Dataset Shape:", df.shape)

print("\nClass Distribution:")
print(df["Class"].value_counts())

print("\nClass Percentage:")
print(df["Class"].value_counts(normalize=True) * 100)


# ==========================================
# 2. FEATURES & TARGET
# ==========================================

X = df.drop("Class", axis=1)
y = df["Class"]


# ==========================================
# 3. TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTrain Shape:", X_train.shape)
print("Test Shape:", X_test.shape)


# ==========================================
# 4. FEATURE SCALING
# ==========================================

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# ==========================================
# 5. SMOTE
# ==========================================

print("\nBefore SMOTE:")
print(y_train.value_counts())

smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train_scaled,
    y_train
)

print("\nAfter SMOTE:")
print(y_train_smote.value_counts())


# ==========================================
# 6. LOGISTIC REGRESSION
# ==========================================

print("\n" + "=" * 50)
print("LOGISTIC REGRESSION")
print("=" * 50)

lr_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

lr_model.fit(
    X_train_smote,
    y_train_smote
)

lr_pred = lr_model.predict(X_test_scaled)

print("\nAccuracy:")
print(accuracy_score(y_test, lr_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, lr_pred))

print("\nClassification Report:")
print(classification_report(y_test, lr_pred))


# ==========================================
# 7. RANDOM FOREST BASELINE
# ==========================================

print("\n" + "=" * 50)
print("RANDOM FOREST")
print("=" * 50)

rf_model = RandomForestClassifier(
  class_weight="balanced",
    random_state=42
)

rf_model.fit(
    X_train_smote,
    y_train_smote
)

rf_pred = rf_model.predict(X_test_scaled)

print("\nAccuracy:")
print(accuracy_score(y_test, rf_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, rf_pred))

print("\nClassification Report:")
print(classification_report(y_test, rf_pred))


# ==========================================
# 8. HYPERPARAMETER TUNING
# ==========================================

print("\n" + "=" * 50)
print("GRID SEARCH")
print("=" * 50)

param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [10, 20],
    "min_samples_split": [2, 5]
}

grid = RandomizedSearchCV(
    estimator=RandomForestClassifier(class_weight='balanced', random_state=42),
    param_distributions=param_grid,
    n_iter=6,
    cv=3,
    scoring="average_precision",
    n_jobs=-1,
    verbose=1,
    random_state=42
)
grid.fit(X_train_scaled, y_train)  #

print("\nBest Parameters:")
print(grid.best_params_)

best_rf = grid.best_estimator_


# ==========================================
# 9. EVALUATE BEST MODEL
# ==========================================

print("\n" + "=" * 50)
print("BEST RANDOM FOREST")
print("=" * 50)

best_pred = best_rf.predict(X_test_scaled)

print("\nAccuracy:")
print(accuracy_score(y_test, best_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, best_pred))

print("\nClassification Report:")
print(classification_report(y_test, best_pred))


# ==========================================
# 10. SAVE MODEL
# ==========================================

joblib.dump(
    best_rf,
    "fraud_model.pkl"
)

joblib.dump(
    scaler,
    "scaler.pkl"
)

print("\nModel Saved Successfully!")
print("fraud_model.pkl")
print("scaler.pkl")
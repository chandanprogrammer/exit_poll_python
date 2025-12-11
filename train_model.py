import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Load dataset
df = pd.read_csv("exit_poll.csv")

# Encode categorical columns with SEPARATE encoders
categorical_cols = ['gender','education','region','income','best_issue','party']
encoders = {}

df_clean = df.copy()

for col in categorical_cols:
    le = LabelEncoder()
    df_clean[col] = le.fit_transform(df_clean[col])
    encoders[col] = le   # store each encoder separately

# Split data
X = df_clean.drop('party', axis=1)
y = df_clean['party']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Train model
model = RandomForestClassifier(n_estimators=300, max_depth=12, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Save model
pickle.dump(model, open("exit_poll_model.pkl", "wb"))

# Save encoders
pickle.dump(encoders, open("encoders.pkl", "wb"))

print("Model + Encoders Saved Successfully!")

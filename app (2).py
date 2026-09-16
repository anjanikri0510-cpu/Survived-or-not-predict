import streamlit as st
import pandas as pd
import joblib

# ---------- Page setup ----------
st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢", layout="centered")

st.title("🚢 Titanic Survival Predictor")
st.write(
    "Enter passenger details below to predict whether they would have "
    "survived the Titanic disaster, using a trained Logistic Regression model."
)

# ---------- Load model ----------
@st.cache_resource
def load_model():
    return joblib.load("survived_pipeline.pkl")

model = load_model()

# ---------- Sidebar inputs ----------
st.sidebar.header("Passenger Details")

pclass = st.sidebar.selectbox(
    "Passenger Class (Pclass)",
    options=[1, 2, 3],
    index=2,
    help="1 = 1st class, 2 = 2nd class, 3 = 3rd class",
)

sex = st.sidebar.radio("Sex", options=["male", "female"], index=0)

age = st.sidebar.slider("Age", min_value=0, max_value=100, value=30)

sibsp = st.sidebar.number_input(
    "Siblings / Spouses aboard (SibSp)", min_value=0, max_value=10, value=0, step=1
)

parch = st.sidebar.number_input(
    "Parents / Children aboard (Parch)", min_value=0, max_value=10, value=0, step=1
)

fare = st.sidebar.number_input(
    "Fare paid", min_value=0.0, max_value=600.0, value=32.0, step=1.0, format="%.2f"
)

embarked = st.sidebar.selectbox(
    "Port of Embarkation",
    options=["S - Southampton", "C - Cherbourg", "Q - Queenstown"],
    index=0,
)
embarked_code = embarked[0]  # "S", "C", or "Q"

# ---------- Build feature row matching training columns ----------
# Model expects: ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'Sex_encoded', 'S', 'C', 'Q']
sex_encoded = 0 if sex == "male" else 1

input_df = pd.DataFrame(
    [{
        "Pclass": pclass,
        "Age": age,
        "SibSp": sibsp,
        "Parch": parch,
        "Fare": fare,
        "Sex_encoded": sex_encoded,
        "S": 1 if embarked_code == "S" else 0,
        "C": 1 if embarked_code == "C" else 0,
        "Q": 1 if embarked_code == "Q" else 0,
    }]
)

st.subheader("Passenger Summary")
st.dataframe(input_df, use_container_width=True, hide_index=True)

# ---------- Predict ----------
if st.button("Predict Survival", type="primary"):
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df)[0]
    survival_prob = proba[1]

    st.divider()
    if prediction == 1:
        st.success(f"✅ Likely to **SURVIVE** — probability: {survival_prob:.1%}")
    else:
        st.error(f"❌ Likely **NOT to survive** — probability of survival: {survival_prob:.1%}")

    st.progress(float(survival_prob))
    st.caption(
        f"Model confidence — Did not survive: {proba[0]:.1%} | Survived: {proba[1]:.1%}"
    )

st.divider()
st.caption(
    "Model: Logistic Regression trained on the classic Titanic dataset. "
    "For educational/demo purposes only."
)

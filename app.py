# =========================
# 📦 Import Libraries
# =========================
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import warnings

warnings.filterwarnings("ignore")

# =========================
# 🎯 Load Model
# =========================
model = pickle.load(open('bigmart_best_model.pkl', 'rb'))

# =========================
# 🖥️ App Title
# =========================
st.set_page_config(page_title="BigMart Sales Prediction", layout="centered")

st.title("🛒 BigMart Sales Prediction App")
st.write("Predict Item Outlet Sales using Machine Learning (Gradient Boosting)")

# =========================
# 📥 User Inputs
# =========================
st.header("Enter Product Details")

# Numeric Inputs
item_weight = st.number_input("Item Weight", min_value=0.0)
item_visibility = st.number_input("Item Visibility", min_value=0.0)
item_mrp = st.number_input("Item MRP", min_value=0.0)

# Categorical Inputs (adjust based on dataset)
item_fat_content = st.selectbox("Item Fat Content", ["Low Fat", "Regular"])
item_type = st.selectbox("Item Type", [
    "Dairy", "Soft Drinks", "Meat", "Fruits and Vegetables",
    "Household", "Baking Goods", "Snack Foods"
])
outlet_size = st.selectbox("Outlet Size", ["Small", "Medium", "High"])
outlet_location = st.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"])
outlet_type = st.selectbox("Outlet Type", [
    "Supermarket Type1", "Supermarket Type2", "Grocery Store"
])

# =========================
# 🔮 Prediction Button
# =========================
if st.button("Predict Sales"):
    try:
        # Create DataFrame (IMPORTANT for pipeline models)
        input_data = pd.DataFrame({
            'Item_Weight': [item_weight],
            'Item_Visibility': [item_visibility],
            'Item_MRP': [item_mrp],
            'Item_Fat_Content': [item_fat_content],
            'Item_Type': [item_type],
            'Outlet_Size': [outlet_size],
            'Outlet_Location_Type': [outlet_location],
            'Outlet_Type': [outlet_type]
        })

        # Prediction
        prediction = model.predict(input_data)[0]
        output = round(prediction, 2)

        # Display Result
        st.success(f"💰 Predicted Sales: {output}")

    except Exception as e:
        st.error(f"Error: {str(e)}")

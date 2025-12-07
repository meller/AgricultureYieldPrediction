"""
Agriculture Yield Prediction Demo
A Vibe Coding Project for Jerusalem University Agriculture Department

This demo showcases:
1. Data Loading & Exploration
2. AI/ML Model Training (Linear Regression)
3. Interactive Visualization with Plotly & Streamlit
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# PAGE CONFIG
# ============================================================================
st.set_page_config(
    page_title="Agriculture Yield Prediction",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# TITLE & INTRO
# ============================================================================
st.markdown("# 🌾 Precision Agriculture Yield Prediction")
st.markdown("### Interactive AI-Powered Analysis for Optimal Crop Yields")
st.markdown("---")

# ============================================================================
# VIBE PROMPT 1: DATA LOADING & EXPLORATION
# ============================================================================
st.subheader("📊 Step 1: Load & Explore Agricultural Data")

try:
    # Load the CSV file
    df = pd.read_csv('yield_data.csv')
    st.success("✅ Data loaded successfully!")

    # Display the DataFrame
    st.write(f"**Dataset Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
    st.dataframe(df, use_container_width=True)

    # Display basic statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", df.shape[0])
    with col2:
        st.metric("Average Yield (Tons/Ha)", f"{df['Yield'].mean():.2f}")
    with col3:
        st.metric("Max Yield (Tons/Ha)", f"{df['Yield'].max():.2f}")

except FileNotFoundError:
    st.error("❌ Error: yield_data.csv not found in the project directory.")
    st.stop()

st.markdown("---")

# ============================================================================
# VIBE PROMPT 2: AI/ML MODEL TRAINING
# ============================================================================
st.subheader("🤖 Step 2: Train AI Model (Linear Regression)")

st.markdown("""
**What's happening here:**
- We're using **Scikit-Learn** to train a Linear Regression model
- Features used: Nitrogen Level, Rainfall, Average Temperature
- Target: Crop Yield (Tons/Ha)
- This model learns the relationship between inputs and yield
""")

# Prepare features and target
X = df[['Nitrogen_Level', 'Rainfall', 'Avg_Temp']]
y = df['Yield']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Calculate metrics
r2_train = r2_score(y_train, y_pred_train)
r2_test = r2_score(y_test, y_pred_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_pred_test))

# Display model metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("R² Score (Test)", f"{r2_test:.3f}", delta="Model Quality")
with col2:
    st.metric("RMSE (Test)", f"{rmse_test:.3f}", delta="Error Rate")
with col3:
    st.metric("Training Samples", len(X_train))

# Display feature coefficients
st.markdown("**Model Coefficients (Feature Importance):**")
coef_df = pd.DataFrame({
    'Feature': ['Nitrogen Level', 'Rainfall', 'Avg Temperature'],
    'Coefficient': model.coef_,
    'Interpretation': [
        'Impact per kg/ha Nitrogen',
        'Impact per mm Rainfall',
        'Impact per °C Temperature'
    ]
})
st.dataframe(coef_df, use_container_width=True)

st.markdown("---")

# ============================================================================
# VIBE PROMPT 3: THE WOW MOMENT - INTERACTIVE VISUALIZATION
# ============================================================================
st.subheader("✨ Step 3: Interactive Visualization (The 'Wow' Moment)")

st.markdown("""
**Why Interactive Charts Matter:**
- Users can **hover** to see exact values
- **Pan and zoom** to explore specific regions
- Much more engaging than static plots
- Perfect for presentations and research
""")

# Add predictions to the original dataframe
df['Predicted_Yield'] = model.predict(X)

# Create tabs for different visualizations
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Scatter: Nitrogen vs Yield",
    "💧 Scatter: Rainfall vs Yield",
    "📈 Actual vs Predicted",
    "🔬 Advanced: 3D Explorer"
])

# ============================================================================
# TAB 1: Nitrogen Level vs Yield (Color-coded by Predicted Yield)
# ============================================================================
with tab1:
    st.markdown("**Relationship: Nitrogen Application & Crop Yield**")

    fig1 = px.scatter(
        df,
        x='Nitrogen_Level',
        y='Yield',
        color='Predicted_Yield',
        size='Rainfall',
        hover_data=['Region', 'Crop_Type', 'Avg_Temp'],
        title='Nitrogen Level vs Actual Yield (colored by AI Prediction)',
        labels={
            'Nitrogen_Level': 'Nitrogen Level (kg/ha)',
            'Yield': 'Actual Yield (Tons/Ha)',
            'Predicted_Yield': 'Predicted Yield'
        },
        color_continuous_scale='Viridis'
    )
    fig1.update_layout(height=500, hovermode='closest')
    st.plotly_chart(fig1, use_container_width=True)

    st.info("💡 **Insight:** Higher nitrogen levels generally correlate with higher yields, but there are diminishing returns and optimal ranges.")

# ============================================================================
# TAB 2: Rainfall vs Yield
# ============================================================================
with tab2:
    st.markdown("**Relationship: Rainfall & Crop Yield**")

    fig2 = px.scatter(
        df,
        x='Rainfall',
        y='Yield',
        color='Nitrogen_Level',
        size='Avg_Temp',
        hover_data=['Region', 'Crop_Type', 'Phosphorus'],
        title='Rainfall vs Actual Yield (colored by Nitrogen Level)',
        labels={
            'Rainfall': 'Rainfall (mm)',
            'Yield': 'Actual Yield (Tons/Ha)',
            'Nitrogen_Level': 'Nitrogen Level'
        },
        color_continuous_scale='Blues'
    )
    fig2.update_layout(height=500, hovermode='closest')
    st.plotly_chart(fig2, use_container_width=True)

    st.info("💡 **Insight:** Water availability is critical—moderate rainfall shows optimal yields, with both drought and excess water reducing performance.")

# ============================================================================
# TAB 3: Model Performance - Actual vs Predicted
# ============================================================================
with tab3:
    st.markdown("**Model Performance: How Well Does AI Predict?**")

    # Create prediction comparison dataframe
    pred_comparison = pd.DataFrame({
        'Actual_Yield': y_test,
        'Predicted_Yield': y_pred_test,
        'Error': y_test - y_pred_test,
        'Error_Percent': ((y_test - y_pred_test) / y_test * 100).abs()
    }).reset_index(drop=True)

    fig3 = px.scatter(
        pred_comparison,
        x='Actual_Yield',
        y='Predicted_Yield',
        color='Error_Percent',
        hover_data=['Error'],
        title='Model Accuracy: Actual vs Predicted Yields',
        labels={
            'Actual_Yield': 'Actual Yield (Tons/Ha)',
            'Predicted_Yield': 'AI Predicted Yield (Tons/Ha)',
            'Error_Percent': 'Error %'
        },
        color_continuous_scale='RdYlGn_r'
    )

    # Add perfect prediction line
    fig3.add_shape(
        type='line',
        x0=df['Yield'].min(),
        y0=df['Yield'].min(),
        x1=df['Yield'].max(),
        y1=df['Yield'].max(),
        line=dict(dash='dash', color='red', width=2),
        name='Perfect Prediction'
    )

    fig3.update_layout(height=500, hovermode='closest')
    st.plotly_chart(fig3, use_container_width=True)

    st.write(f"**Model R² Score: {r2_test:.3f}** (Higher is better, max = 1.0)")
    st.write(f"**Root Mean Square Error: {rmse_test:.3f}** (Lower is better)")

# ============================================================================
# TAB 4: Advanced 3D Explorer
# ============================================================================
with tab4:
    st.markdown("**3D Interactive Explorer: All Variables Together**")

    fig4 = px.scatter_3d(
        df,
        x='Nitrogen_Level',
        y='Rainfall',
        z='Yield',
        color='Avg_Temp',
        size='Phosphorus',
        hover_data=['Region', 'Crop_Type'],
        title='3D: Nitrogen × Rainfall × Yield (colored by Temperature)',
        labels={
            'Nitrogen_Level': 'Nitrogen (kg/ha)',
            'Rainfall': 'Rainfall (mm)',
            'Yield': 'Yield (Tons/Ha)',
            'Avg_Temp': 'Temperature (°C)'
        },
        color_continuous_scale='Plasma'
    )

    fig4.update_layout(height=600, scene=dict(
        xaxis_title='Nitrogen Level (kg/ha)',
        yaxis_title='Rainfall (mm)',
        zaxis_title='Yield (Tons/Ha)'
    ))
    st.plotly_chart(fig4, use_container_width=True)

    st.info("💡 **Interaction:** Rotate the 3D plot with your mouse to explore all relationships simultaneously. This reveals complex multi-variable patterns!")

st.markdown("---")

# ============================================================================
# INTERACTIVE PREDICTION TOOL
# ============================================================================
st.subheader("🎮 Try the Model Yourself!")
st.markdown("**Enter values to predict crop yield for your specific conditions:**")

col1, col2, col3 = st.columns(3)

with col1:
    nitrogen = st.slider(
        "Nitrogen Level (kg/ha)",
        min_value=int(df['Nitrogen_Level'].min()),
        max_value=int(df['Nitrogen_Level'].max()),
        value=150
    )

with col2:
    rainfall = st.slider(
        "Rainfall (mm)",
        min_value=int(df['Rainfall'].min()),
        max_value=int(df['Rainfall'].max()),
        value=750
    )

with col3:
    temperature = st.slider(
        "Average Temperature (°C)",
        min_value=float(df['Avg_Temp'].min()),
        max_value=float(df['Avg_Temp'].max()),
        value=26.0,
        step=0.1
    )

# Make prediction
predicted_yield = model.predict([[nitrogen, rainfall, temperature]])[0]

# Display prediction with visual feedback
st.markdown("---")
col_pred1, col_pred2, col_pred3 = st.columns([1, 2, 1])

with col_pred2:
    st.markdown(f"""
    <div style='text-align: center; padding: 20px; background-color: #f0f8ff; border-radius: 10px; border: 2px solid #4CAF50;'>
        <h3>🎯 Predicted Yield</h3>
        <h1 style='color: #4CAF50;'>{predicted_yield:.2f}</h1>
        <p>Tons per Hectare</p>
    </div>
    """, unsafe_allow_html=True)

# Show comparison with dataset average
avg_yield = df['Yield'].mean()
comparison = "above" if predicted_yield > avg_yield else "below"
diff = abs(predicted_yield - avg_yield)

st.info(f"📊 This prediction is **{comparison}** the dataset average ({avg_yield:.2f} Tons/Ha) by {diff:.2f} Tons/Ha")

st.markdown("---")

# ============================================================================
# FOOTER
# ============================================================================
st.markdown("""
---
### 🎓 About This Project

**Developed for:** Jerusalem University Agriculture Department
**Purpose:** Demonstrate AI/ML application in precision agriculture
**Technologies:** Python, Streamlit, Scikit-Learn, Plotly, Pandas

**Key Concepts Demonstrated:**
- ✅ Data Loading & Exploration (Pandas)
- ✅ Machine Learning Model Training (Scikit-Learn)
- ✅ Interactive Visualization (Plotly)
- ✅ Model Evaluation & Metrics
- ✅ Real-time Predictions

**Future Enhancements:**
- Multiple crop type models
- Historical yield trends
- Weather forecasting integration
- Recommendation engine for optimal fertilizer dosage

---
*Created with Vibe Coding & AI-assisted development* 🚀
""")

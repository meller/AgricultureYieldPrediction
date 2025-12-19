# Quick Setup Guide

## 🚀 Get Started in 2 Minutes

### Step 1: Activate Virtual Environment
```bash
source venv/bin/activate
```

```powershell
# On Windows (creates a Windows-specific env and installs deps)
.\scripts\windows\setup.ps1
.\.venv-windows\Scripts\Activate.ps1
```

### Step 2: Run the App
```bash
streamlit run app.py
```

### Step 3: Open in Browser
The app will automatically open at `http://localhost:8501`

---

## ✅ What You Get

- **Step 1:** Load and explore agricultural data (45 records)
- **Step 2:** AI model training with R² metrics
- **Step 3:** 4 interactive visualization tabs
- **Bonus:** Real-time prediction tool with sliders

---

## 🎬 Demo Flow (15-20 minutes)

1. **Data Overview** - Show the CSV table
2. **Model Metrics** - Point out R² score (0.95+)
3. **Interactive Charts** - This is the "wow moment"!
   - Nitrogen vs Yield (Tab 1)
   - Rainfall vs Yield (Tab 2)
   - Model Performance (Tab 3)
   - 3D Explorer (Tab 4) ← audience loves this
4. **Live Prediction** - Use sliders, change values in real-time
5. **Wrap up** - Discuss real-world applications

---

## 💾 Files in This Project

- `app.py` - Main Streamlit application (700+ lines)
- `yield_data.csv` - Realistic agricultural dataset (45 rows)
- `requirements.txt` - Python dependencies
- `README.md` - Comprehensive documentation
- `SETUP_GUIDE.md` - This file

---

## 📊 Expected Output

When you run the app, you should see:

1. 🌾 Precision Agriculture Yield Prediction (title)
2. 📊 Data exploration section with metrics
3. 🤖 Model training results with R² score
4. 4 tabs with interactive charts
5. 🎮 Prediction tool at the bottom

---

## 🎨 Interactive Features

### Hover Over Charts
- See exact values
- Identify specific data points
- View hidden information

### Pan & Zoom
- Click and drag to move around
- Scroll wheel to zoom
- Double-click to reset

### 3D Plot (Tab 4)
- Click and drag to rotate
- Scroll to zoom in/out
- Shows 5 variables simultaneously!

---

## ⚡ Performance Tips

- First load might take 5 seconds (model training)
- Subsequent interactions are instant
- Sliders respond immediately
- Charts are fully interactive

---

## 🆘 Troubleshooting

### Port 8501 already in use?
```bash
streamlit run app.py --server.port 8502
```

### Charts not showing?
- Make sure JavaScript is enabled in browser
- Try a different browser (Chrome/Firefox recommended)
- Disable browser extensions

### Data file not found?
- Make sure `yield_data.csv` is in same folder as `app.py`
- Run from project root: `/home/mellera/VsCode/AgricultureYieldPrediction/`

---

## 📝 What to Mention During Demo

**"This is a realistic agriculture dataset with:**
- Multiple regions (North, South, Center)
- Two crop types (Wheat, Corn)
- Real environmental factors (nitrogen, rainfall, temp)"

**"The AI model learned to predict yield based on:**
- Nitrogen application levels
- Rainfall amounts
- Average temperatures"

**"Notice the interactive charts:**
- Hover to see exact values
- Pan and zoom to explore
- 3D view shows all relationships at once"

**"Real applications:**
- Farmers optimize fertilizer use
- Research guides policy decisions
- Saves money and protects environment"

---

## 🎓 For Students/Learners

**Key Concepts Demonstrated:**
1. Data Science Pipeline (Load → Process → Model → Visualize)
2. Linear Regression (simple but powerful ML)
3. Model Evaluation (R², RMSE metrics)
4. Interactive Data Visualization
5. End-to-End ML Application

---

**Ready? Run `streamlit run app.py` and wow your audience! 🚀**

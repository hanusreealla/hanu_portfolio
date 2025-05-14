
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Alla Hanu Sree Portfolio", layout="wide")

# --- HOME ---
st.title("Welcome to Alla Hanu Sree's Portfolio")
st.markdown("""
Hi, I’m Alla Hanu Sree, a Mechanical Engineer from IIT Hyderabad, with strong expertise in Python and Machine Learning.

I specialize in applying machine learning, computer vision, and sensor integration to solve real-world problems in robotics, simulation, and embedded systems.

Currently, I’m working on developing solutions for autonomous systems, simulation environments, and marine sensor modules.

---

**Key Focus Areas:**
- Robotics & Simulation
- Machine Learning & Computer Vision
- Sensor Integration & IoT
""")

# --- PROJECTS ---
st.header("Projects")

# Project 1
st.subheader("Credit Card Fraud Detection")
st.write("""
Built fraud detection models using Logistic Regression and SMOTE to handle imbalanced data. 
Evaluated performance using ROC-AUC, precision, and recall.
""")
st.markdown("**Skills & Tools:** Python, Pandas, Scikit-learn, SMOTE, ROC-AUC")
st.markdown("[GitHub Repo](https://github.com/hanusreealla/credit_card_fraud_detection_project/blob/main/CREDITCARDFRAUDDETECTION.ipynb)")

# Project 2
st.subheader("3D Object Reconstruction (Ongoing)")
st.write("""
Reconstructing 3D shapes from 2D views using OpenCV.
Involves edge detection, Hough transform, and coordinate mapping.
""")
st.markdown("**Skills & Tools:** Python, OpenCV, Hough Transform")
st.markdown("*GitHub Repo coming soon*")

# Project 3
st.subheader("Marine Water Quality Sensor Module")
st.write("""
Designed a sensor-integrated water quality module to measure pH, ORP, EC, and DO.
Integrated GPS-based logging and processed data in QGIS.
""")
st.markdown("**Skills & Tools:** Arduino, Embedded Systems, Sensor Integration, QGIS")
st.markdown("[Documentation PDF](https://chat.openai.com/mnt/data/DIY%20Water%20Quality%20Sensor%20Module%20Development%20for%20Marine%20Applications%20(1).pdf)")

# Project 4
st.subheader("6-Bar Walking Mechanism")
st.write("""
Designed a 6-bar linkage walking mechanism with object pickup functionality.
Involved kinematic synthesis and gear-driven slider-crank input.
""")
st.markdown("**Skills & Tools:** Mechanism Design, MATLAB, Gears, Slider-Crank")
st.markdown("[Kinematics Report](https://chat.openai.com/mnt/data/Kinematics%20Profile.pdf)")

# --- SKILLS ---
st.header("Skills")
st.markdown("""
**Languages:** Python, C++, Arduino  
**ML Frameworks:** Scikit-learn, XGBoost  
**Robotics & Simulation Tools:** ROS2 (learning), Isaac Sim (learning), Gazebo, MATLAB, Solid Edge, OpenCV  
**Embedded Systems:** Arduino, Sensor Integration, IoT  
**Data Analytics:** Pandas, NumPy, Data Visualization
""")

# --- RESUME & CONTACT ---
st.header("Contact")
st.markdown("""
**Email:** hanusreealla@gmail.com  
**GitHub:** [hanusreealla](https://github.com/hanusreealla)
""")

st.markdown("---")
st.caption("Built with Streamlit | © 2025 Alla Hanu Sree")

import gradio as gr
from agents.classifier import SkinClassifier
from agents.recommender import RecommendationAgent
from utils.helpers import evaluate_prediction

# Initialize Agents
classifier = SkinClassifier()
recommender = RecommendationAgent()

def analyze(image):
    condition, confidence = classifier.predict(image)
    advice = recommender.get_advice(condition, confidence)
    quality = evaluate_prediction(confidence)

    report = f"""
🏥 **DIGITAL HEALTH DIAGNOSTIC REPORT**

----------------------------------------
🧑‍⚕️ Patient Skin Analysis Summary
----------------------------------------

🔍 **Detected Condition**
➡ {condition}

📊 **Confidence Score**
➡ {confidence}

📈 **Prediction Reliability**
➡ {quality}

----------------------------------------
💊 **Medical Recommendation**
----------------------------------------
{advice}

----------------------------------------
⚠️ **Disclaimer**
----------------------------------------
This system is an AI-assisted decision support tool.
Please consult a certified dermatologist for medical treatment.

💙 *Your skin health matters. Early diagnosis saves lives.*
"""

    return report

with gr.Blocks(theme=gr.themes.Soft()) as demo:

    # ===== HEADER =====
    gr.HTML("""
    <div style="background:linear-gradient(90deg,#1f8ef1,#2ecc71);
                padding:25px;
                border-radius:15px;
                text-align:center;">
        <h1 style="color:white;">🩺 Smart Skin Healthcare System</h1>
        <h3 style="color:white;">
        AI-Powered • Multi-Agent • CNN Transfer Learning
        </h3>
        <p style="color:white;font-size:16px;">
        Empowering early detection for healthier lives 💙
        </p>
    </div>
    """)

    gr.Markdown("## 🧠 How This Healthcare AI Works")
    gr.Markdown("""
    - **Agent 1 – Image Analysis Agent**: Uses CNN with Transfer Learning  
    - **Agent 2 – Medical Decision Agent**: Interprets diagnosis  
    - **Agent 3 – Evaluation Agent**: Measures confidence & reliability  
    - **Agent 4 – UI Agent**: Generates hospital-style reports  
    """)

    gr.Markdown("---")

    # ===== INPUT SECTION =====
    gr.Markdown("## 📷 Upload Skin Image")
    gr.Markdown("Please upload a **clear image** of the affected skin area for analysis.")

    with gr.Row():
        image_input = gr.Image(type="pil", label="Skin Image")

    # ===== ACTION =====
    with gr.Row():
        submit_btn = gr.Button("🧪 Analyze Skin Health", variant="primary")
        clear_btn = gr.Button("🔄 Clear")

    # ===== OUTPUT =====
    gr.Markdown("## 📄 Diagnostic Report")
    output_text = gr.Markdown()

    submit_btn.click(fn=analyze, inputs=image_input, outputs=output_text)
    clear_btn.click(lambda: (None, ""), outputs=[image_input, output_text])

    # ===== FOOTER =====
    gr.HTML("""
    <div style="background-color:#f9f9f9;
                padding:15px;
                border-radius:10px;
                margin-top:20px;
                text-align:center;">
        <p style="font-size:16px;">
        💙 <b>Health is Wealth.</b>  
        This AI system supports preventive healthcare and early detection.
        </p>
        <p style="font-size:14px;color:gray;">
        Developed as an Advanced Multi-Agent AI Healthcare Project
        </p>
    </div>
    """)

demo.launch()




import gradio as gr
import os, time

from agents.classifier import SkinClassifier
from utils.helpers import evaluate_prediction
from utils.db import init_db, save_patient, fetch_all_patients

# ======================
# INIT
# ======================
classifier = SkinClassifier()
init_db()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ======================
# LOGIC
# ======================
def login(user, pwd):
    if user == "admin" and pwd == "admin123":
        return gr.update(visible=False), gr.update(visible=True), ""
    return gr.update(visible=True), gr.update(visible=False), "❌ Invalid login"

def analyze(name, image):
    image_path = os.path.join(UPLOAD_DIR, f"{name}_{int(time.time())}.png")
    image.save(image_path)

    condition, confidence = classifier.predict(image)
    quality = evaluate_prediction(confidence)

    summary = f"""
    <div class="card">
        <h3>🧑‍⚕️ Diagnosis Summary</h3>
        <p><b>Patient:</b> {name}</p>
        <p><b>Condition:</b> {condition}</p>
        <p><b>Confidence:</b> {confidence*100:.1f}%</p>
        <div class="bar">
            <div class="fill" style="width:{confidence*100}%"></div>
        </div>
        <p class="quality">{quality}</p>
    </div>
    """
    return condition, confidence, summary, image_path

def treatment(name, condition, confidence, image_path):
    advice = [
        "Keep affected area clean",
        "Avoid scratching",
        "Use mild soap",
        "Apply sunscreen daily",
        "Moisturize regularly",
        "Avoid harsh cosmetics",
        "Drink enough water",
        "Consult dermatologist if severe"
    ]

    save_patient(name, image_path, condition, confidence, "\n".join(advice))

    html = "<div class='grid'>"
    for a in advice:
        html += f"<div class='tip'>💡 {a}</div>"
    html += "</div><p class='warn'>⚠️ AI-assisted only</p>"
    return html

def records():
    rows = fetch_all_patients()
    html = """
    <table class="table">
    <tr><th>Patient</th><th>Condition</th><th>Confidence</th><th>Date</th></tr>
    """
    for r in rows:
        html += f"<tr><td>{r[1]}</td><td>{r[3]}</td><td>{r[4]*100:.1f}%</td><td>{r[6]}</td></tr>"
    html += "</table>"
    return html

# ======================
# UI
# ======================
with gr.Blocks(css="""
body {
    background:#f8fafc;
    font-family: Arial, sans-serif;
}
.card {
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0 4px 12px rgba(0,0,0,.08);
}
.bar {
    background:#e5e7eb;
    height:12px;
    border-radius:8px;
}
.fill {
    background:#22c55e;
    height:12px;
    border-radius:8px;
}
.grid {
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
    gap:12px;
}
.tip {
    background:#ffffff;
    padding:14px;
    border-radius:10px;
    box-shadow:0 2px 8px rgba(0,0,0,.05);
}
.warn {
    color:#dc2626;
    margin-top:10px;
}
.table {
    width:100%;
    border-collapse:collapse;
}
.table th, .table td {
    padding:12px;
    border-bottom:1px solid #e5e7eb;
}
""") as demo:

    login_page = gr.Column(visible=True)
    clinic = gr.Column(visible=False)

    # -------- LOGIN --------
    with login_page:
        gr.Markdown("## 🏥 Clinic Login")
        user = gr.Textbox(label="Username")
        pwd = gr.Textbox(label="Password", type="password")
        btn = gr.Button("Login")
        msg = gr.Markdown()

    # -------- CLINIC DASHBOARD --------
    with clinic:
        gr.Markdown("# 🏥 Skin Care Clinic System")

        with gr.Tabs():
            with gr.Tab("🧑‍⚕️ Diagnosis"):
                with gr.Row():
                    name = gr.Textbox(label="Patient Name")
                    img = gr.Image(type="pil", label="Upload Skin Image")

                run = gr.Button("Analyze")
                condition = gr.Textbox(label="Detected Condition")
                conf = gr.Textbox(label="Confidence")
                summary = gr.HTML()
                state = gr.State()

                treat = gr.Button("Generate Treatment Plan")
                advice = gr.HTML()

                run.click(analyze, [name, img], [condition, conf, summary, state])
                treat.click(treatment, [name, condition, conf, state], advice)

            with gr.Tab("📋 Patient Records"):
                refresh = gr.Button("Refresh Records")
                table = gr.HTML()
                refresh.click(records, [], table)

    btn.click(login, [user, pwd], [login_page, clinic, msg])

demo.launch(share=True)









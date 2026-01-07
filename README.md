## Advanced AI Techniques Used

- CNN with Transfer Learning (ResNet18)
- Multi-Agent System Architecture
- Medical Image Classification
- Confidence-based Evaluation
- Web-based User Interface

## Multi-Agent Architecture

1. Data Ingestion Agent – Receives skin image
2. Classification Agent – CNN-based disease detection
3. Recommendation Agent – Medical advice generation
4. UI Agent – User interaction and report display


# 🩺 Skin Diagnostic System

A **hospital-style skin diagnostic system** built with Python and Gradio.  
This system simulates a **multi-agent skin analysis**, providing:

- Automated detection of common skin conditions (simulated for demo purposes)
- Confidence levels for each condition
- Recommendations/advice based on detected conditions
- Hospital-style report display directly in the app (no downloads required)

---

## Features

- **Multi-Agent Architecture**
  - **Agent 1:** CNN-based classifier (simulated) detects skin conditions
  - **Agent 2:** Recommender provides advice for each condition
- **Visual Feedback**
  - Confidence bar chart for each detected condition
- **Interactive Web App**
  - Upload an image of your skin
  - Get a full hospital-style report instantly
- **Session History**
  - All analyzed cases are stored in the session history

---

## 🛠️ Setup & Installation

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/skin-diagnostic-system.git
cd skin-diagnostic-system

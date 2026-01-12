from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

class TreatmentLLMAgent:
    def __init__(self, model_name="gpt2"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.generator = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def get_advice(self, condition, confidence, patient_name):
        prompt = f"""
        Patient: {patient_name}
        Detected skin condition: {condition}
        Confidence: {confidence*100:.1f}%
        Provide short, safe treatment advice in 5-8 steps.
        """
        result = self.generator(prompt, max_length=150, num_return_sequences=1)
        advice_text = result[0]['generated_text'].split("Patient:")[0].strip()
        return advice_text

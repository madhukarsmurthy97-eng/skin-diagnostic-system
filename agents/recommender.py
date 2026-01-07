class RecommendationAgent:
    def get_advice(self, condition, confidence):
        if confidence < 0.6:
            return "Low confidence result. Please consult a dermatologist."

        advice = {
            "Acne": "Use mild cleansers and benzoyl peroxide.",
            "Eczema": "Moisturize daily and avoid allergens.",
            "Psoriasis": "Consult dermatologist for topical therapy.",
            "Rosacea": "Avoid spicy food and sun exposure.",
            "Fungal Infection": "Apply antifungal cream.",
            "Vitiligo": "Use sunscreen and consult specialist.",
            "Healthy": "No issues detected. Maintain skin hygiene."
        }
        return advice.get(condition, "Consult a doctor.")



from app.services.ai_service import AIService

class FinancialService:

    def __init__(self):
        self.ai = AIService()

    def classify_profile(self, risk):
        if risk <= 3:
            return "conservador"
        elif risk <= 7:
            return "moderado"
        return "agressivo"

    def simulate(self, amount, rate, years):
        return round(amount * ((1 + rate) ** years), 2)

    def process(self, data):
        profile = self.classify_profile(data.risk)

        suggestion = self.ai.generate_advice(
            profile=profile,
            amount=data.amount,
            goal=data.goal
        )

        return {
            "perfil": profile,
            "recomendacao": suggestion
        }

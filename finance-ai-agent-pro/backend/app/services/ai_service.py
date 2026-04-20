class AIService:

    def generate_advice(self, profile, amount, goal):
        # Aqui você pode integrar OpenAI depois
        return f"""
Perfil identificado: {profile}.
Para o objetivo '{goal}', recomenda-se diversificação compatível com o risco.
Valor analisado: R$ {amount}.
"""

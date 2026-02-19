class Cognition:

    def __init__(self, identity, memory):
        self.identity = identity
        self.memory = memory

    def reflect(self):
        score = self.memory.compound_score()

        if score > 0.8:
            self.identity.evolve_trait("strategic")
        elif score > 0.5:
            self.identity.evolve_trait("adaptive")
        else:
            self.identity.evolve_trait("resilient")

    def generate_decision(self, input_context: str) -> str:
        base = f"{self.identity.name} acts aligned with purpose: {self.identity.purpose}."
        traits = f"Core traits: {', '.join(self.identity.traits)}."
        return f"{base} {traits} Context: {input_context}"

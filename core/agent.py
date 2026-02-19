from core.identity import Identity
from core.memory import Memory, Experience
from core.cognition import Cognition
from core.resilience import ResilienceEngine
from config import MEMORY_CAPACITY, DEFAULT_RESILIENCE_SCORE


class ZyrolatorAgent:

    def __init__(self, name: str, purpose: str, traits: list[str]):
        self.identity = Identity(name=name, purpose=purpose, traits=traits)
        self.memory = Memory(capacity=MEMORY_CAPACITY)
        self.cognition = Cognition(self.identity, self.memory)
        self.resilience = ResilienceEngine(DEFAULT_RESILIENCE_SCORE)

    def experience(self, event: str, impact: float):
        exp = Experience(event=event, impact_score=impact)
        self.memory.add_experience(exp)
        self.cognition.reflect()

    def respond(self, context: str, stress_level: float = 0.2):
        resilience_score = self.resilience.evaluate(stress_level)
        decision = self.cognition.generate_decision(context)

        return {
            "identity": self.identity.summary(),
            "resilience_score": resilience_score,
            "compound_memory_score": self.memory.compound_score(),
            "decision": decision
        }

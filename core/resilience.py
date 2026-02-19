class ResilienceEngine:

    def __init__(self, baseline: float = 0.75):
        self.baseline = baseline

    def evaluate(self, stress_level: float) -> float:
        adjusted = self.baseline - (stress_level * 0.1)
        return max(0.0, min(1.0, adjusted))

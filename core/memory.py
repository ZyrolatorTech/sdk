from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Experience:
    event: str
    impact_score: float
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self):
        return {
            "event": self.event,
            "impact_score": self.impact_score,
            "timestamp": self.timestamp.isoformat()
        }


class Memory:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.experiences: List[Experience] = []

    def add_experience(self, experience: Experience):
        if len(self.experiences) >= self.capacity:
            self.experiences.pop(0)
        self.experiences.append(experience)

    def compound_score(self) -> float:
        if not self.experiences:
            return 0.0
        return sum(e.impact_score for e in self.experiences) / len(self.experiences)

    def to_dict(self):
        return [e.to_dict() for e in self.experiences]

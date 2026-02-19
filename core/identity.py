from dataclasses import dataclass, field
from uuid import uuid4
from datetime import datetime

@dataclass
class Identity:
    name: str
    purpose: str
    traits: list[str]
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime = field(default_factory=datetime.utcnow)

    def evolve_trait(self, trait: str):
        if trait not in self.traits:
            self.traits.append(trait)

    def summary(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "purpose": self.purpose,
            "traits": self.traits,
            "created_at": self.created_at.isoformat()
        }

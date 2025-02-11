""" Alert Model """
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.models.model_base import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    rule_id = Column(Integer, ForeignKey("alert_rules.id"), nullable=False)
    triggered_price = Column(Float, nullable=False)
    reason = Column(String, nullable=False)

    rule = relationship("AlertRule", back_populates="alerts")

    def __repr__(self):
        return f"<Alert(id={self.id}, rule_id={self.rule_id}, triggered_price={self.triggered_price})>"

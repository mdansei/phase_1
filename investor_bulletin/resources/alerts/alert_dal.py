""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from db.models.models import Alert

def get_alerts(session):
    return session.query(Alert).all()

""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
import resources.alerts.alert_dal as AlertDal

def get_alerts(session):
    return AlertDal.get_alerts(session)

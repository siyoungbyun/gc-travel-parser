from gctravelparser import db


class Applicant(db.Model):
    """ A class containing information about the user who submitted the application
    """
    applicant_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    division = db.Column(db.String(60), nullable=False)
    last_awarded = db.Column(db.DateTime, nullable=True)


class BasicApplication(db.Model):
    """ A class containing information about the basic application itself
    """
    application_id = db.Column(db.Integer, primary_key=True)
    submitted = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.applicant_id'), nullable=False)
    event_name = db.Column(db.String(255), nullable=False)
    travel_start = db.Column(db.DateTime, nullable=False)
    travel_end = db.Column(db.DateTime, nullable=False)
    importance = db.Column(db.Text, nullable=False)  # How often do questions change?
    contribution = db.Column(db.Text, nullable=False)
    expenditures = db.Column(db.Text, nullable=False)
    alternative_funding = db.Column(db.Text, nullable=True)
    faculty_name = db.Column(db.String(80), nullable=False)
    faculty_email = db.Column(db.String(120), nullable=False)
    group_size = db.Column(db.Integer, nullable=False)


class AdvancedApplication(db.Model):
    """ A class containing information about the advanced application itself
    """
    application_id = db.Column(db.Integer, primary_key=True)
    submitted = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.applicant_id'), nullable=False)
    event_name = db.Column(db.String(255), nullable=False)
    presentation_type = db.Column(db.String(50), nullable=False)
    travel_start = db.Column(db.DateTime, nullable=False)
    travel_end = db.Column(db.DateTime, nullable=False)
    importance = db.Column(db.Text, nullable=False)
    significance = db.Column(db.Text, nullable=False)
    contribution = db.Column(db.Text, nullable=False)
    expenditures = db.Column(db.Text, nullable=False)
    alternative_funding = db.Column(db.Text, nullable=True)
    faculty_name = db.Column(db.String(80), nullable=False)
    faculty_email = db.Column(db.String(120), nullable=False)


class Reviewer(db.Model):
    """ A class containing information about the user who reviewed the application
    """
    reviewer_id = db.Column(db.Integer, primary_key=True)

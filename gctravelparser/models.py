from gctravelparser import db


class Applicant(db.Model):
    """ A class containing information about the user who submitted the application
    """
    uuid = db.Column(db.Integer, primary_key=True)


class Reviewer(db.Model):
    """ A class containing information about the user who submitted the application
    """
    uuid = db.Column(db.Integer, primary_key=True)


class Application(db.Model):
    """ A class containing information about the application itself
    """
    uuid = db.Column(db.Integer, primary_key=True)

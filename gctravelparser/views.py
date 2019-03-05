from datetime import datetime
from uuid import uuid4
from flask import render_template, request
from gctravelparser import app, db
from gctravelparser.models import Applicant, Application, Recommendation


def get_applicant(form):
    """ Gets applicant info, or adds if necessary
    """
    applicant_result = Applicant.query.filter_by(email=form.get("email")).first()

    if applicant_result:
        applicant_id = applicant_result.applicant_id
        else:
        applicant_id = add_applicant(form)

    return applicant_id


def add_applicant(form):
    """ Adds new applicant to database
    """
        applicant = Applicant(
        first_name=form.get("firstname"),
        last_name=form.get("lastname"),
        email=form.get("email"),
        division=form.get("division")
        )
        db.session.add(applicant)
    db.session.commit()

    return applicant.applicant_id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/basic', methods=['GET', 'POST'])
def basic():
    if request.form:
        application = Application(
            submitted=datetime.now(),
            status='submitted',
            applicant_id=get_applicant(request.form),
            event_name=request.form.get('event-name'),
            travel_start=datetime.strptime(request.form.get('start-date'), '%Y-%m-%d'),
            travel_end=datetime.strptime(request.form.get('end-date'), '%Y-%m-%d'),
            importance=request.form.get('importance'),
            contribution=request.form.get('contribution'),
            expenditures=request.form.get('expenditures'),
            alternative_funding=request.form.get('alternative-funding'),
            faculty_name=request.form.get('faculty-name'),
            faculty_email=request.form.get('faculty-email'),
            group_size=request.form.get('group-size'),
            uuid=str(uuid4())
        )
        db.session.add(application)
        db.session.commit()

    return render_template('basic.html')


@app.route('/advanced', methods=['GET', 'POST'])
def advanced():
    if request.form:
        application = Application(
            submitted=datetime.now(),
            status='submitted',
            applicant_id=get_applicant(request.form),
            event_name=request.form.get('event-name'),
            travel_start=datetime.strptime(request.form.get('start-date'), '%Y-%m-%d'),
            travel_end=datetime.strptime(request.form.get('end-date'), '%Y-%m-%d'),
            importance=request.form.get('importance'),
            significance=request.form.get('significance'),
            contribution=request.form.get('contribution'),
            expenditures=request.form.get('expenditures'),
            alternative_funding=request.form.get('alternative-funding'),
            faculty_name=request.form.get('faculty-name'),
            faculty_email=request.form.get('faculty-email'),
            presentation_type=request.form.get('presentation-type'),
            uuid=str(uuid4())
        )
        db.session.add(application)
        db.session.commit()

    return render_template('advanced.html')


@app.route('/recommendation/<uuid:uuid>', methods=['GET', 'POST'])
def recommendation(uuid):
    if request.form:
        recommendation = Recommendation(
            student_first_name=request.form.get('student-firstname'),
            student_last_name=request.form.get('student-lastname'),
            recommender_first_name=request.form.get('recommender-firstname'),
            recommender_last_name=request.form.get('recommender-lastname'),
            recommender_email=request.form.get('recommender-email'),
            recommender_position=request.form.get('recommender-position'),
            relationship=request.form.get('relationship'),
            merit=request.form.get('merit'),
            conference=request.form.get('conference'),
            representative=request.form.get('representative'),
            additional_comments=request.form.get('additional-comments')
        )

        db.session.add(recommendation)

        application_result = Application.query.filter_by(uuid=str(uuid)).all()

        if application_result:
            if len(application_result) == 0:
                # raise error
                pass
            elif len(application_result) > 1:
                # raise error
                pass
            else:
                application_result[0].status = 'reviewing'

        db.session.commit()

    return render_template('recommendation.html')


@app.route('/review')
def review():
    return render_template('review.html')


@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

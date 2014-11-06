from flask import current_app, session, request, render_template, redirect, url_for
from flask.views import MethodView
from mdr.views.forms.treatmentform import TreatmentForm



class Index(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        ''' Dispatch the request.
        '''
        # First, let's clear the session of variables associated to previous patient registration.
        self.clear_session_variables()

        # Now let's retrieve our list of patients.
        patient_docs = mongo.db.malignantdisease.find({}).sort([("_id", -1)])
        # Render the templates.
        return render_template('index.html', patient_docs=patient_docs)

    #FIXME: It's a bit confusing to have this logic here. Maybe put it in its own class.
    def post(self):
        ''' Process inputted treatment.
            Store treatment data.
            Return to index page.
        '''
        # Log progress.
        current_app.logger.info('Processed treatment for case %s', doc_id)
        current_app.logger.info('Completed registration of case %s', doc_id)


        # We use redirect instead of render_template so that we can run the logic in this view's get() method.
        return redirect(url_for('index'))

    def save_treatment(self, doc_id):

        # Update the patient doc with treatment.
        treatment_form = TreatmentForm(request.form)
        treatment = treatment_form.data

        mongo.db.malignantdisease.update(
            {'_id': doc_id},
            {'$set': {'treatment': treatment}}
        )

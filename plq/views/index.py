from flask import current_app, request, render_template, redirect, url_for
from flask.views import MethodView
from plq.views.indexform import IndexForm
from plq.utils.utils import Utils
from plq import mongo

utils = Utils()


class Index(MethodView):
    methods = ['GET', 'POST']

    def get(self):
        ''' Dispatch the request.
        '''
        form = IndexForm()
        return render_template('index.html', form=form)

    def post(self):
        ''' Process inputted treatment.
            Store treatment data.
            Return to index page.
        '''
        #let's get the doc id from utils.
        doc_id = utils.get_doc_id()
        # Log progress.
        current_app.logger.info('Processed skills form for case %s', doc_id)
        current_app.logger.info('Completed registration of case %s', doc_id)

        self.save_skills_form(doc_id)

        # We use redirect instead of render_template so that we can run the logic in this view's get() method.
        return redirect(url_for('index'))

    def save_skills_form(self, doc_id):

        # Update the patient doc with treatment.
        skills_form = IndexForm(request.form)
        programmer_info = utils.get_structured_skills_form(skills_form)

        mongo.db.developer.update(
            {'_id': doc_id},
            {'$set': {'programmerInfo': programmer_info}},
            True
        )

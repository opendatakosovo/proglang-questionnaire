from flask_wtf import Form
from wtform import TextField, TextAreaField, SelectField, RadioField
from checkboxwidgets import MultiCheckboxField


class IndexForm(Form):

    programing_languages = [
        'Python', 'Java', 'VB', 'C#', 'C++',
        'JavaScript', 'Ruby', 'HTML', 'CSS',
        'Objective-C', 'PHP', 'Perl', 'Tjera'
    ]

    programing_languages_choices = [(x, x) for x in programing_languages]

    emri = TextField('Emri:')
    mbiemri = TextField('Mbiemri:')

    gjinia = RadioField(
        'Gjinia:',
        choices=[('Mashkull', 'Mashkull'), ('Femer', 'Femer')],
        default='Mashkull')

    qyteti = TextField('Qyteti:')
    e_mail = TextField('E-mail:')
    shkollimi = TextField('Shkollimi:')
    departamenti = TextAreaField('Departamenti:')

    gjuhet_programuese = MultiCheckboxField(
        'Gjuhet programuese qe punoni dhe niveli juaj ne ato:',
        choices=programing_languages_choices)

    gjuhet_tjera_programuese = TextAreaField('Tjera (comma separated)')
    shkathesite_tjera = TextAreaField("Shkathesite tjera (comma separated):")

    nivelet = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ])

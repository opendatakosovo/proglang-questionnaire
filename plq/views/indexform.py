from flask_wtf import Form
from wtforms import TextField, TextAreaField, SelectField, RadioField, BooleanField
from checkboxwidgets import MultiCheckboxField


class IndexForm(Form):

    programing_languages = [
        'Python', 'Java', 'VB', 'C#', 'C++',
        'JavaScript', 'Ruby', 'HTML', 'CSS',
        'Objective-C', 'PHP', 'Perl', 'Tjera'
    ]

     # create a list of value/description tuples
    programing_languages_choices = [
        (x, x) for x in programing_languages
    ]

    emri = TextField('Emri:')
    mbiemri = TextField('Mbiemri:')

    gjinia = RadioField(
        'Gjinia:',
        choices=[('Mashkull', 'Mashkull'), ('Femer', 'Femer')],
        default='Mashkull')

    qyteti = TextField('Vendbanimi:')
    e_mail = TextField('E-mail:')
    universiteti = SelectField(
        'Universiteti:',
        choices=[('Universiteti Prishtines', 'Universiteti Prishtines'),
        ('UBT', 'UBT'),
        ])
    departamenti = TextAreaField('Departamenti:')

    viti_studimit = SelectField(
        'Viti studimit',
        choices=[('1', '1'), ('2', '2'),
        ('3', '3'), ('4', '4'), ('i diplomuar', 'i diplomuar'),
        ('1 - Master', '1 - Master'), ('2 - Master', '2 - Master'),
        ('i diplomuar - Master', 'i diplomuar - Master')
        ])

    gjuhet_programuese = MultiCheckboxField(
        'Gjuhet programuese qe punoni dhe niveli juaj ne ato:',
        choices=programing_languages_choices)

    gjuhet_tjera_programuese = TextAreaField('Gjuhet tjera programuese(te ndahen me presje)')

    shkathesite_tjera = TextAreaField("Shkathesite tjera(te ndahen me presje):")

    nivelet = SelectField(
        'Nivelet',
        choices=[('Ekspert', 'Ekspert'),
        ('Mesatar', 'Mesatar'),
        ('Fillestar', 'Fillestar')
        ])
    python_lang = MultiCheckboxField("Python", choices=[('Python', 'Python')])

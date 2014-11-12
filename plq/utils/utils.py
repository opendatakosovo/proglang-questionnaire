from bson import ObjectId


class Utils(object):

    def __init__(self):
        pass

    def get_doc_id(self):
        ''' Get the doc_id.
            First, try to retrieve it from the session.
            If it's not in the session, create one.
        '''
        doc_id = str(ObjectId())
        return doc_id

    def get_structured_skills_form(self, form):

        '''This functions returns a structured json_obj document
            for skills form
        '''

        json_obj = {}

        json_obj = {
            'personalInfo': {
                'emri': form.emri.data,
                'mbiemri': form.mbiemri.data,
                'gjinia': form.gjinia.data,
                'qyteti': form.qyteti.data,
                'e_mail': form.e_mail.data,
                'universiteti': form.universiteti.data,
                'departamenti': form.departamenti.data,
                'viti_studimit': form.viti_studimit.data,
                'shkathesite_tjera': form.shkathesite_tjera.data,
            },
            'languages': {
                'python': {
                    'has_skill': form.python_lang.data,
                    'level': form.niveli_ptyhon.data
                },
                'java': {
                    'has_skill': form.java_lang.data,
                    'level': form.niveli_java_lang.data
                },
                'vb_lang': {
                    'has_skill': form.vb_lang.data,
                    'level': form.niveli_vb_lang.data
                },
                'csharp_lang': {
                    'has_skill': form.csharp_lang.data,
                    'level': form.niveli_csharp_lang.data
                },
                'cpp_lang': {
                    'has_skill': form.cpp_lang.data,
                    'level': form.niveli_cpp_lang.data
                },
                'java_script_lang': {
                    'has_skill': form.java_script_lang.data,
                    'level': form.niveli_java_script_lang.data
                },
                'ruby_lang': {
                    'has_skill': form.ruby_lang.data,
                    'level': form.niveli_ruby_lang.data
                },
                'html_lang': {
                    'has_skill': form.html_lang.data,
                    'level': form.niveli_html_lang.data
                },
                'css_lang': {
                    'has_skill': form.css_lang.data,
                    'level': form.niveli_css_lang.data
                },
                'objective_c_lang': {
                    'has_skill': form.objective_c_lang.data,
                    'level': form.niveli_objective_c_lang.data
                },
                'php_lang': {
                    'has_skill': form.php_lang.data,
                    'level': form.niveli_php_lang.data
                },
                'perl_lang': {
                    'has_skill': form.perl_lang.data,
                    'level': form.niveli_perl_lang.data
                },
                'tjera_lang': {
                    'has_skill': form.gjuhet_tjera_programuese.data
                }
            }
        }

        return json_obj

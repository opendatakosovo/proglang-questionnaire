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
        for key in form:
            if key == "python_lang" and key == "niveli_ptyhon":
                json_obj['pythonLanguage'] = {
                    'gjuhaProgramuese': form.python_lang.data[0],
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "java_lang":
                json_obj['java_lang'] = {
                    'gjuhaProgramuese': form.java_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "vb_lang":
                json_obj['vb_lang'] = {
                    'gjuhaProgramuese': form.vb_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "csharp_lang":
                json_obj['csharp_lang'] = {
                    'gjuhaProgramuese': form.csharp_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "cpp_lang":
                json_obj['cpp_lang'] = {
                    'gjuhaProgramuese': form.cpp_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "java_script_lang":
                json_obj['java_script_lang'] = {
                    'gjuhaProgramuese': form.java_script_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "ruby_lang":
                json_obj['ruby_lang'] = {
                    'gjuhaProgramuese': form.ruby_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "html_lang":
                json_obj['html_lang'] = {
                    'gjuhaProgramuese': form.html_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "css_lang":
                json_obj['css_lang'] = {
                    'gjuhaProgramuese': form.css_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "objective_c_lang":
                json_obj['objective_c_lang'] = {
                    'gjuhaProgramuese': form.objective_c_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "php_lang":
                json_obj['php_lang'] = {
                    'gjuhaProgramuese': form.php_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "perl_lang":
                json_obj['perl_lang'] = {
                    'gjuhaProgramuese': form.perl_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            elif key == "tjera_lang":
                json_obj['tjera_lang'] = {
                    'gjuhaProgramuese': form.tjera_lang.data,
                    'niveliProgramimit': form.niveli_ptyhon.data
                }
            else:
                json_obj = form.data

            return json_obj

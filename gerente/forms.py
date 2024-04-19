from django import forms
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit, Button

class GerenteForm(forms.ModelForm):
    class Meta:
        model = Gerente
        fields = [
            'gerente_nome',
            'gerente_matricula',
            'gerente_cpf',
            'gerente_celular',
            'gerente_email',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'visualizar_gerente'
        self.helper.add_input(
            Submit(
                "submit",
                "Salvar",
                css_class="btn btn-dark"
            )
        )

        self.helper.add_input(
            Button(
                "voltar",
                "Voltar",
                css_class= "btn btn-outline-dark",
                onclick = "javascript:history.back()",
            )
        )

        self.helper.layout = Layout(
            Fieldset(
                "",
                "gerente_nome",
                Div(
                    Field("gerente_matricula", wrapper_class="col"),
                    Field("gerente_cpf", wrapper_class="col"),
                    Field("gerente_celular", wrapper_class="col"),
                    Field("gerente_email", wrapper_class="col"),                    

                    css_class= "row",
                ),

                css_class= "border-bottom mb-3"
            )
        )

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Div, Field, Fieldset, Layout, Submit

from .models import *

class VacinacaoForm(forms.ModelForm):
    class Meta:
        model = CadastroVacinal
        fields = [
            'vacina',
            'paciente',
            'unidade_saude',
            'data_aplicacao',
            'status',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'visualizar_vacinacao'
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
                'paciente',

                Div(
                    Field("vacina", wrapper_class="col"),
                    Field("unidade_saude", wrapper_class="col"),
                    Field("data_aplicacao", wrapper_class="col"),
                    Field("status", wrapper_class="col"),                    

                    css_class= "row",
                ),

                css_class= "border-bottom mb-3"
            )
        )
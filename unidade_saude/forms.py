from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Div, Field, Fieldset, Layout, Submit

from .models import *

class UnidadeForm(forms.ModelForm):
    class Meta:
        model = UnidadeSaude
        fields = [
            'uni_cnes',
            'uni_nome',
            'uni_cnpj',
            'uni_endereco',
            'uni_num_casa',
            'uni_bairro',
            'uni_cidade',
            'uni_uf',
            'uni_cep',
            'uni_email',
            'uni_tipo',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'visualizar_unidade'
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
                "uni_nome",

                Div(
                    Field('uni_cnes', wrapper_class='col'),
                    Field('uni_cnpj', wrapper_class='col'),
                    Field('uni_email', wrapper_class='col'),

                    css_class= 'row',
                ),
                Div(
                    Field('uni_cep', wrapper_class='col'),
                    Field('uni_endereco', wrapper_class='col'),
                    Field('uni_num_casa', wrapper_class='col'),

                    css_class='row',
                ),
                Div(
                    Field('uni_bairro', wrapper_class='col'),
                    Field('uni_cidade', wrapper_class='col'),
                    Field('uni_uf', wrapper_class='col'),
                    Field('uni_tipo', wrapper_class='col'),

                    css_class='row',
                ),
                css_class='border-bottom mb-3'
            )
        )
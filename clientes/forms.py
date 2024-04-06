from django import forms
from django.core.exceptions import ValidationError
from .models import *

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Field, Fieldset, Layout, Submit, Button

class CadastroCriancaForm(forms.ModelForm):
    class Meta:
        model = Crianca
        fields = [
            'crianca_nome',
            'crianca_nascimento',
            'crianca_rg',
            'crianca_cpf',
            'crianca_responsavel',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = '.'
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
                "crianca_nome",
                Div(
                    Field("crianca_nascimento", wrapper_class="col"),
                    Field("crianca_rg", wrapper_class="col"),
                    Field("crianca_cpf", wrapper_class="col"),
                    Field("crianca_responsavel", wrapper_class="col"),                    

                    css_class= "row",
                ),

                css_class= "border-bottom mb-3"
            )
        )

    def clean_crianca(self):
        cleaned_data = self.cleaned_data
        valida_crianca_nome = cleaned_data.get('crianca_nome')
        valida_crianca_responsavel = cleaned_data.get('crianca_responsavel')

        if Crianca.objects.filter(crianca_nome=valida_crianca_nome, 
                                  crianca_responsavel=valida_crianca_responsavel).exists():
            raise ValidationError(f"A criança {valida_crianca_nome} já existe para o responsável {valida_crianca_responsavel}")

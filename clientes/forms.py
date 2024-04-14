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
        self.helper.form_action = 'visualizar_crianca'
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

#Form para Pai/responsável
class CadastroPaiForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = [
            'pai_nome',
            'pai_rg',
            'pai_cpf',
            'pai_celular',
            'pai_cep',
            'pai_endereco',
            'pai_num_casa',
            'pai_complemento_casa',
            'pai_bairro',
            'pai_cidade',
            'pai_uf',
            'pai_email',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = 'visualizar_resp'
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
                "pai_nome",
                Div(
                    Field("pai_rg", wrapper_class="col"),
                    Field("pai_cpf", wrapper_class="col"),                    
                    Field("pai_celular", wrapper_class="col"),                    
                    Field("pai_email", wrapper_class="col"),                    

                    css_class= "row",
                ),
                Div(
                    Field("pai_cep", wrapper_class="col"),
                    Field("pai_endereco", wrapper_class="col"),                    
                    Field("pai_num_casa", wrapper_class="col"),                    
                    Field("pai_complemento_casa", wrapper_class="col"),                    
                    
                    css_class= "row",
                ),
                Div(
                    Field("pai_bairro", wrapper_class="col"),                    
                    Field("pai_cidade", wrapper_class="col"),                    
                    Field("pai_uf", wrapper_class="col"),                    

                    css_class= "row",
                ),
                css_class= "border-bottom mb-3"
                )
            
        )

from flask_restx import fields
from src.server.instance import server
from src.models.id import id

receita_request = server.api.model('Receita',  {
    'nome_produto': fields.String(required=True, min_Length=1, max_Length=200, description='Nome do produto que faz parte'),
    'possiveis_receitas': fields.List(fields.String),
    'nome_receita': fields.String(required=True, min_Length=1, max_Length=200, description='Nome da receita'),
})

receita_response = server.api.inherit('ReceitaResponse', receita_request, id)

receita_update_request = server.api.inherit('ReceitaUpdateRequest',  receita_request, id)

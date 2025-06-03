from rest_framework import viewsets
from toys.models import Toy
from toys.serializers import ToySerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action


class ToyViewSet(viewsets.ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['toy_category', 'was_included_in_home']
    search_fields = ['name', 'description']
    ordering_fields = ['release_date', 'name']
    ordering = ['name']  # ordenação padrão
    
    @swagger_auto_schema(
    operation_summary="Listar brinquedos com filtros, busca e ordenação",
    manual_parameters=[
        openapi.Parameter(
            'search',
            openapi.IN_QUERY,
            description="Busca por nome ou descrição",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'toy_category',
            openapi.IN_QUERY,
            description="Filtrar por categoria",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'was_included_in_home',
            openapi.IN_QUERY,
            description="Filtrar se foi incluído em casa (true/false)",
            type=openapi.TYPE_BOOLEAN
        ),
        openapi.Parameter(
            'ordering',
            openapi.IN_QUERY,
            description="Ordenar por campos (ex: name, -release_date)",
            type=openapi.TYPE_STRING
        ),
        openapi.Parameter(
            'page',
            openapi.IN_QUERY,
            description="Número da página",
            type=openapi.TYPE_INTEGER
        ),
    ]
)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


    @swagger_auto_schema(
    operation_summary="Criar novo brinquedo",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["name", "toy_category", "release_date"],
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING, example="Boneco Ninja"),
            "description": openapi.Schema(type=openapi.TYPE_STRING, example="Brinquedo de ação com acessórios."),
            "toy_category": openapi.Schema(type=openapi.TYPE_STRING, example="Ação"),
            "release_date": openapi.Schema(type=openapi.TYPE_STRING, format="date-time", example="2024-10-01T00:00:00Z"),
            "was_included_in_home": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
        },
    )
)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_summary="Atualizar brinquedo existente",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["name", "toy_category", "release_date"],
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING, example="Boneco Samurai"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, example="Brinquedo com armadura removível."),
                "toy_category": openapi.Schema(type=openapi.TYPE_STRING, example="Colecionável"),
                "release_date": openapi.Schema(type=openapi.TYPE_STRING, format="date-time", example="2023-06-15T00:00:00Z"),
                "was_included_in_home": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=False),
            },
        )
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
    operation_summary="Editar parcialmente um brinquedo",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "name": openapi.Schema(type=openapi.TYPE_STRING, example="Boneco 2.0"),
            "description": openapi.Schema(type=openapi.TYPE_STRING, example="Nova versão com pintura metalizada."),
            "toy_category": openapi.Schema(type=openapi.TYPE_STRING, example="Ação"),
            "release_date": openapi.Schema(type=openapi.TYPE_STRING, format="date-time", example="2024-12-01T00:00:00Z"),
            "was_included_in_home": openapi.Schema(type=openapi.TYPE_BOOLEAN, example=True),
        },
    )
)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_summary="Visualizar detalhes de um brinquedo",
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


    @swagger_auto_schema(
        operation_summary="Excluir um brinquedo existente",
        responses={204: "Removido com sucesso", 404: "Não encontrado"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(description="Uma simples consulta para dizer olá.")

    def resolve_hello(self, info):
        return "Olá, mundo!"

schema = Schema(query=Query)

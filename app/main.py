from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.graphql import GraphQLApp
from graphene import ObjectType, String, Schema

class Query(ObjectType):
    hello = String(description="Uma simples consulta para dizer olá.")

    def resolve_hello(self, info):
        return "Olá, mundo!"

schema = Schema(query=Query)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_route("/graphql", GraphQLApp(schema=schema))

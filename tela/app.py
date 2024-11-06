from fastapi import FastAPI
from ariadne import QueryType,make_executable_schema,graphql
from ariadne.asgi import GraphQl

#defina o esquema graphQL
type_defs="""
    type Query {
        hello:String!
    }
"""
query = QueryType()

@query.field("hello")
async def resolve_hello(_,info):
    return "Olá,mundo!"

schema =make_executable_schema(type_defs,query)

app = FastAPI()

app.add route("/graphql"GraphQl(schema,debug=True))

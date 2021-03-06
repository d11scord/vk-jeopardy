import random

from aiohttp import web
from aiohttp.web_exceptions import HTTPBadRequest
from aiohttp_apispec import (
    docs,
    json_schema,
    response_schema,
    querystring_schema,
)
from sqlalchemy import and_

from app.game.session.models import GameSession, SessionScores
from app.game.session.schemas import (
    GameSessionSchema,
    GameSessionCreateSchema,
    GameSessionListSchema,
    GameSessionDeleteSchema,
    SessionScoresSchema,
    SessionScoresListSchema,
)


class CreateGameSessionView(web.View):
    @docs(tags=["game"], summary="Create game session")
    @json_schema(GameSessionCreateSchema)
    @response_schema(GameSessionSchema)
    async def post(self):
        session = await GameSession.create(
            chat_id=self.request['json']["chat_id"],
            questions=self.request['json']["questions"],
            last_question_id=0,
            is_finished=False,
        )
        return web.json_response(GameSessionSchema().dump(session))


class DeleteGameSessionView(web.View):
    @docs(tags=["game"], summary="Delete game session")
    @json_schema(GameSessionDeleteSchema)
    async def delete(self):
        game_id = self.request['json']["id"]

        game = await GameSession.get(game_id)
        if game:
            await (
                GameSession.delete
                .where(GameSession.id == game_id)
                .gino.status()
            )
            return web.json_response({}, status=204)
        raise HTTPBadRequest(reason="no_such_record")


class GameSessionListView(web.View):
    @docs(tags=["game"], summary="Game sessions list")
    @querystring_schema(GameSessionListSchema)
    @response_schema(GameSessionSchema(many=True))
    async def get(self):
        data = self.request["querystring"]
        conditions = []
        # TODO: add user_id
        if data.get("chat_id"):
            conditions.append(GameSession.chat_id == data["chat_id"])

        games = (
            await GameSession.load()
            .query.where(and_(*conditions))
            .order_by(GameSession.id)
            .limit(data["limit"])
            .offset(data["offset"])
            .gino.all()
        )
        return web.json_response(GameSessionSchema(many=True).dump(games))


class SessionScoresListView(web.View):
    @docs(tags=["game"], summary="Session scores list")
    @querystring_schema(SessionScoresListSchema)
    @response_schema(SessionScoresSchema(many=True))
    async def get(self):
        data = self.request["querystring"]

        session_scores = (
            await SessionScores.load()
            .query.order_by(SessionScores.id)
            .limit(data["limit"])
            .offset(data["offset"])
            .gino.all()
        )
        return web.json_response(SessionScoresSchema(many=True).dump(session_scores))

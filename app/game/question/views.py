from aiohttp import web
from aiohttp.web_exceptions import HTTPBadRequest
from aiohttp_apispec import docs, querystring_schema, response_schema, json_schema
from sqlalchemy import and_

from app.game.question.models import Question
from app.game.question.schemas import (
    QuestionSchema,
    QuestionListSchema,
    QuestionCreateSchema,
    QuestionDeleteSchema, QuestionUpdateSchema,
)


class CreateQuestionView(web.View):
    @docs(tags=["question"], summary="Create question")
    @json_schema(QuestionCreateSchema)
    @response_schema(QuestionSchema)
    async def post(self):
        question = await Question.create(
            theme=self.request['json']["theme"],
            title=self.request['json']["title"],
        )
        return web.json_response(QuestionSchema().dump(question))


class UpdateQuestionView(web.View):
    @docs(tags=["question"], summary="Update question")
    @json_schema(QuestionUpdateSchema)
    @response_schema(QuestionSchema)
    async def put(self):
        question = await Question.get(self.request['json']["id"])
        if question:
            await question.update(
                theme=self.request['json']["theme"],
                title=self.request['json']["title"],
            ).apply()
            return web.json_response(QuestionSchema().dump(question))
        raise HTTPBadRequest(reason="no_such_record")


class DeleteQuestionView(web.View):
    @docs(tags=["question"], summary="Delete question")
    @json_schema(QuestionDeleteSchema)
    async def delete(self):
        question_id = self.request['json']["id"]

        question = await Question.get(question_id)
        if question:
            await (
                Question.delete
                .where(Question.id == question_id)
                .gino.status()
            )
            return web.json_response({}, status=204)
        raise HTTPBadRequest(reason="no_such_record")


class QuestionListView(web.View):
    @docs(tags=["question"], summary="Questions list")
    @querystring_schema(QuestionListSchema)
    @response_schema(QuestionSchema(many=True))
    async def get(self):
        data = self.request["querystring"]
        conditions = []
        if data.get("theme"):
            conditions.append(Question.theme.contains(data["theme"]))

        questions = (
            await Question.load()
            .query.where(and_(*conditions))
            .order_by(Question.id)
            .limit(data["limit"])
            .offset(data["offset"])
            .gino.all()
        )
        return web.json_response(QuestionSchema(many=True).dump(questions))

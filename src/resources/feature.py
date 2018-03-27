from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from src.validators import FeatureSchema
from src.models import FeatureRequest
from src.db import session


class FeatureRequestView(Resource):
    """
    Accept GET and POST method.
    """

    def get(self):
        _filter_params = self._get_filters()
        queryset = session.query(FeatureRequest).filter_by(**_filter_params)
        results = [obj.to_dict() for obj in queryset]
        resp = {'results': results, 'counts': len(results)}
        return resp

    def post(self):
        json_data = request.get_json()
        try:
            data = FeatureSchema().load(json_data)
        except ValidationError as err:
            return err.messages, 400

        instance = FeatureRequest(**data)
        session.add(instance)
        session.commit()
        return instance.to_dict(), 201

    def _get_filters(self):
        return dict((k, request.args.get(k, '')) for k in ('title', 'client', 'priority') if request.args.get(k))

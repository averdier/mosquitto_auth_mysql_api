# -*- coding: utf-8 -*-

from flask_restplus import fields
from .. import api


auth_token = api.model('Auth Token', {
    'token': fields.String(required=True, description='Auth token')
})
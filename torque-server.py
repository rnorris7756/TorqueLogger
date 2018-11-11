#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import falcon
from os import environ as env
from torquedb import TorqueDB

class TorqueLoggerResource(object):

    """A resource for logging torque entries to a database."""

    def __init__(self):
        """TODO: to be defined1. """
        self._client = TorqueDB(env.get("MONGO_HOST"), int(env.get("MONGO_PORT")), env.get("MONGO_INITDB_ROOT_USERNAME"), env.get("MONGO_INITDB_ROOT_PASSWORD"))

    def on_get(self, req, resp):
        """Defines behavior when GET is called on the TorqueLoggerResource.

        :req: TODO
        :resp: TODO
        :returns: TODO

        """
        query_params = req.params
        if query_params:
            self._client.insert_data(query_params)
            resp.body = "OK!"
            resp.status = falcon.HTTP_200
        print(query_params)

api = application = falcon.API()
logger_resource = TorqueLoggerResource()
api.add_route("/log", logger_resource)


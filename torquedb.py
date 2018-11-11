#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymongo


class TorqueDB(object):

    """Docstring for TorqueDB. """

    def __init__(self, host, port, username, password):
        """TODO: to be defined1.

        :host: TODO
        :port: TODO
        :username: TODO
        :password: TODO

        """
        self._client = pymongo.MongoClient(host, port, username = username, password = password)
        self._db = self._client["torque_db"]
        self._data = self._db["torque_data"]
        self._schemas = self._db["torque_schemas"]

    def insert_data(self, data):
        """Inserts data.

        :data: TODO
        :returns: TODO

        """
        self._data.insert_one(data)

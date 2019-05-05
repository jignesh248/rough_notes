from abc import ABCMeta, abstractmethod
from enum import Enum

class Control( object ):
    def handle_request( self, request ):
        raise NotImplementedError( "Should have implemented this" )

    def destination_reached(self, status:"Status"):
        raise NotImplementedError( "Should have implemented this" )

class Direction(Enum):
    UP = 0
    DOWN = 1

class Elevator( object ):

    def to_floor(self, floor:"int"):
        raise NotImplementedError("Should have implemented this")

    def update_intermediate_stops(self, floor:"list"):
        raise NotImplementedError("Should have implemented this")

    def get_status(self)->"Status":
        raise NotImplementedError("Should have implemented this")


class Request(object):
    _request_time = None
    _floor = None
    _direction = None

class RulesManager(object):
    def enqueue(self, request:"Request"):
        raise NotImplementedError("Should have implemented this")

    def get_next_destination(self)->"int":
        raise NotImplementedError("Should have implemented this")

class Status(object):
    _currentFloor = None #int
    _direction = None #Direction
    _finalDestination = None #int

class UserInterface (object):
    def request(request:"Request"):
        raise NotImplementedError("Should have implemented this")
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import hello1_pb2 as hello1__pb2


class HelloEasonStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.HelloEason = channel.unary_unary(
                '/test.HelloEason/HelloEason',
                request_serializer=hello1__pb2.HelloEasonReq.SerializeToString,
                response_deserializer=hello1__pb2.HelloEasonReply.FromString,
                )


class HelloEasonServicer(object):
    """Missing associated documentation comment in .proto file."""

    def HelloEason(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_HelloEasonServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'HelloEason': grpc.unary_unary_rpc_method_handler(
                    servicer.HelloEason,
                    request_deserializer=hello1__pb2.HelloEasonReq.FromString,
                    response_serializer=hello1__pb2.HelloEasonReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'test.HelloEason', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class HelloEason(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def HelloEason(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/test.HelloEason/HelloEason',
            hello1__pb2.HelloEasonReq.SerializeToString,
            hello1__pb2.HelloEasonReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
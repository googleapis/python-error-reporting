# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.cloud.errorreporting_v1beta1.proto import (
    report_errors_service_pb2 as google_dot_cloud_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_report__errors__service__pb2,
)


class ReportErrorsServiceStub(object):
    """An API for reporting error events.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReportErrorEvent = channel.unary_unary(
            "/google.devtools.clouderrorreporting.v1beta1.ReportErrorsService/ReportErrorEvent",
            request_serializer=google_dot_cloud_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_report__errors__service__pb2.ReportErrorEventRequest.SerializeToString,
            response_deserializer=google_dot_cloud_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_report__errors__service__pb2.ReportErrorEventResponse.FromString,
        )


class ReportErrorsServiceServicer(object):
    """An API for reporting error events.
    """

    def ReportErrorEvent(self, request, context):
        """Report an individual error event.

        This endpoint accepts **either** an OAuth token,
        **or** an [API key](https://support.google.com/cloud/answer/6158862)
        for authentication. To use an API key, append it to the URL as the value of
        a `key` parameter. For example:

        `POST
        https://clouderrorreporting.googleapis.com/v1beta1/projects/example-project/events:report?key=123ABC456`
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ReportErrorsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "ReportErrorEvent": grpc.unary_unary_rpc_method_handler(
            servicer.ReportErrorEvent,
            request_deserializer=google_dot_cloud_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_report__errors__service__pb2.ReportErrorEventRequest.FromString,
            response_serializer=google_dot_cloud_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_report__errors__service__pb2.ReportErrorEventResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "google.devtools.clouderrorreporting.v1beta1.ReportErrorsService",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ReportErrorsService(object):
    """An API for reporting error events.
    """

    @staticmethod
    def ReportErrorEvent(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/google.devtools.clouderrorreporting.v1beta1.ReportErrorsService/ReportErrorEvent",
            google_dot_cloud_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_report__errors__service__pb2.ReportErrorEventRequest.SerializeToString,
            google_dot_cloud_dot_devtools_dot_clouderrorreporting__v1beta1_dot_proto_dot_report__errors__service__pb2.ReportErrorEventResponse.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

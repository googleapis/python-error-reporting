# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.devtools.clouderrorreporting.v1beta1",
    manifest={
        "ResolutionStatus",
        "ErrorGroup",
        "TrackingIssue",
        "ErrorEvent",
        "ServiceContext",
        "ErrorContext",
        "HttpRequestContext",
        "SourceLocation",
    },
)


class ResolutionStatus(proto.Enum):
    r"""Resolution status of an error group."""
    RESOLUTION_STATUS_UNSPECIFIED = 0
    OPEN = 1
    ACKNOWLEDGED = 2
    RESOLVED = 3
    MUTED = 4


class ErrorGroup(proto.Message):
    r"""Description of a group of similar error events.

    Attributes:
        name (str):
            The group resource name.
            Example: <code>projects/my-
            project-123/groups/CNSgkpnppqKCUw</code>
        group_id (str):
            Group IDs are unique for a given project. If
            the same kind of error occurs in different
            service contexts, it will receive the same group
            ID.
        tracking_issues (Sequence[google.cloud.errorreporting_v1beta1.types.TrackingIssue]):
            Associated tracking issues.
        resolution_status (google.cloud.errorreporting_v1beta1.types.ResolutionStatus):
            Error group's resolution status.
            An unspecified resolution status will be
            interpreted as OPEN
    """

    name = proto.Field(proto.STRING, number=1,)
    group_id = proto.Field(proto.STRING, number=2,)
    tracking_issues = proto.RepeatedField(
        proto.MESSAGE, number=3, message="TrackingIssue",
    )
    resolution_status = proto.Field(proto.ENUM, number=5, enum="ResolutionStatus",)


class TrackingIssue(proto.Message):
    r"""Information related to tracking the progress on resolving the
    error.

    Attributes:
        url (str):
            A URL pointing to a related entry in an issue tracking
            system. Example:
            ``https://github.com/user/project/issues/4``
    """

    url = proto.Field(proto.STRING, number=1,)


class ErrorEvent(proto.Message):
    r"""An error event which is returned by the Error Reporting
    system.

    Attributes:
        event_time (google.protobuf.timestamp_pb2.Timestamp):
            Time when the event occurred as provided in
            the error report. If the report did not contain
            a timestamp, the time the error was received by
            the Error Reporting system is used.
        service_context (google.cloud.errorreporting_v1beta1.types.ServiceContext):
            The ``ServiceContext`` for which this error was reported.
        message (str):
            The stack trace that was reported or logged
            by the service.
        context (google.cloud.errorreporting_v1beta1.types.ErrorContext):
            Data about the context in which the error
            occurred.
    """

    event_time = proto.Field(proto.MESSAGE, number=1, message=timestamp_pb2.Timestamp,)
    service_context = proto.Field(proto.MESSAGE, number=2, message="ServiceContext",)
    message = proto.Field(proto.STRING, number=3,)
    context = proto.Field(proto.MESSAGE, number=5, message="ErrorContext",)


class ServiceContext(proto.Message):
    r"""Describes a running service that sends errors.
    Its version changes over time and multiple versions can run in
    parallel.

    Attributes:
        service (str):
            An identifier of the service, such as the name of the
            executable, job, or Google App Engine service name. This
            field is expected to have a low number of values that are
            relatively stable over time, as opposed to ``version``,
            which can be changed whenever new code is deployed.

            Contains the service name for error reports extracted from
            Google App Engine logs or ``default`` if the App Engine
            default service is used.
        version (str):
            Represents the source code version that the
            developer provided, which could represent a
            version label or a Git SHA-1 hash, for example.
            For App Engine standard environment, the version
            is set to the version of the app.
        resource_type (str):
            Type of the MonitoredResource. List of
            possible values:
            https://cloud.google.com/monitoring/api/resources
            Value is set automatically for incoming errors
            and must not be set when reporting errors.
    """

    service = proto.Field(proto.STRING, number=2,)
    version = proto.Field(proto.STRING, number=3,)
    resource_type = proto.Field(proto.STRING, number=4,)


class ErrorContext(proto.Message):
    r"""A description of the context in which an error occurred.
    This data should be provided by the application when reporting
    an error, unless the
    error report has been generated automatically from Google App
    Engine logs.

    Attributes:
        http_request (google.cloud.errorreporting_v1beta1.types.HttpRequestContext):
            The HTTP request which was processed when the
            error was triggered.
        user (str):
            The user who caused or was affected by the crash. This can
            be a user ID, an email address, or an arbitrary token that
            uniquely identifies the user. When sending an error report,
            leave this field empty if the user was not logged in. In
            this case the Error Reporting system will use other data,
            such as remote IP address, to distinguish affected users.
            See ``affected_users_count`` in ``ErrorGroupStats``.
        report_location (google.cloud.errorreporting_v1beta1.types.SourceLocation):
            The location in the source code where the
            decision was made to report the error, usually
            the place where it was logged. For a logged
            exception this would be the source line where
            the exception is logged, usually close to the
            place where it was caught.
    """

    http_request = proto.Field(proto.MESSAGE, number=1, message="HttpRequestContext",)
    user = proto.Field(proto.STRING, number=2,)
    report_location = proto.Field(proto.MESSAGE, number=3, message="SourceLocation",)


class HttpRequestContext(proto.Message):
    r"""HTTP request data that is related to a reported error.
    This data should be provided by the application when reporting
    an error, unless the
    error report has been generated automatically from Google App
    Engine logs.

    Attributes:
        method (str):
            The type of HTTP request, such as ``GET``, ``POST``, etc.
        url (str):
            The URL of the request.
        user_agent (str):
            The user agent information that is provided
            with the request.
        referrer (str):
            The referrer information that is provided
            with the request.
        response_status_code (int):
            The HTTP response status code for the
            request.
        remote_ip (str):
            The IP address from which the request
            originated. This can be IPv4, IPv6, or a token
            which is derived from the IP address, depending
            on the data that has been provided in the error
            report.
    """

    method = proto.Field(proto.STRING, number=1,)
    url = proto.Field(proto.STRING, number=2,)
    user_agent = proto.Field(proto.STRING, number=3,)
    referrer = proto.Field(proto.STRING, number=4,)
    response_status_code = proto.Field(proto.INT32, number=5,)
    remote_ip = proto.Field(proto.STRING, number=6,)


class SourceLocation(proto.Message):
    r"""Indicates a location in the source code of the service for which
    errors are reported. ``functionName`` must be provided by the
    application when reporting an error, unless the error report
    contains a ``message`` with a supported exception stack trace. All
    fields are optional for the later case.

    Attributes:
        file_path (str):
            The source code filename, which can include a
            truncated relative path, or a full path from a
            production machine.
        line_number (int):
            1-based. 0 indicates that the line number is
            unknown.
        function_name (str):
            Human-readable name of a function or method. The value can
            include optional context like the class or package name. For
            example, ``my.package.MyClass.method`` in case of Java.
    """

    file_path = proto.Field(proto.STRING, number=1,)
    line_number = proto.Field(proto.INT32, number=2,)
    function_name = proto.Field(proto.STRING, number=4,)


__all__ = tuple(sorted(__protobuf__.manifest))

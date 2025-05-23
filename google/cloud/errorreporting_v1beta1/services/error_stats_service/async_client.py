# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
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
import logging as std_logging
from collections import OrderedDict
import re
from typing import (
    Dict,
    Callable,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.cloud.errorreporting_v1beta1 import gapic_version as package_version

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry_async as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore
import google.protobuf


try:
    OptionalRetry = Union[retries.AsyncRetry, gapic_v1.method._MethodDefault, None]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.AsyncRetry, object, None]  # type: ignore

from google.cloud.errorreporting_v1beta1.services.error_stats_service import pagers
from google.cloud.errorreporting_v1beta1.types import common
from google.cloud.errorreporting_v1beta1.types import error_stats_service
from .transports.base import ErrorStatsServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ErrorStatsServiceGrpcAsyncIOTransport
from .client import ErrorStatsServiceClient

try:
    from google.api_core import client_logging  # type: ignore

    CLIENT_LOGGING_SUPPORTED = True  # pragma: NO COVER
except ImportError:  # pragma: NO COVER
    CLIENT_LOGGING_SUPPORTED = False

_LOGGER = std_logging.getLogger(__name__)


class ErrorStatsServiceAsyncClient:
    """An API for retrieving and managing error statistics as well
    as data for individual events.
    """

    _client: ErrorStatsServiceClient

    # Copy defaults from the synchronous client for use here.
    # Note: DEFAULT_ENDPOINT is deprecated. Use _DEFAULT_ENDPOINT_TEMPLATE instead.
    DEFAULT_ENDPOINT = ErrorStatsServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ErrorStatsServiceClient.DEFAULT_MTLS_ENDPOINT
    _DEFAULT_ENDPOINT_TEMPLATE = ErrorStatsServiceClient._DEFAULT_ENDPOINT_TEMPLATE
    _DEFAULT_UNIVERSE = ErrorStatsServiceClient._DEFAULT_UNIVERSE

    error_group_path = staticmethod(ErrorStatsServiceClient.error_group_path)
    parse_error_group_path = staticmethod(
        ErrorStatsServiceClient.parse_error_group_path
    )
    common_billing_account_path = staticmethod(
        ErrorStatsServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ErrorStatsServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ErrorStatsServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ErrorStatsServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ErrorStatsServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ErrorStatsServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ErrorStatsServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        ErrorStatsServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(ErrorStatsServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        ErrorStatsServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ErrorStatsServiceAsyncClient: The constructed client.
        """
        return ErrorStatsServiceClient.from_service_account_info.__func__(ErrorStatsServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ErrorStatsServiceAsyncClient: The constructed client.
        """
        return ErrorStatsServiceClient.from_service_account_file.__func__(ErrorStatsServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variable is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return ErrorStatsServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ErrorStatsServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            ErrorStatsServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    @property
    def api_endpoint(self):
        """Return the API endpoint used by the client instance.

        Returns:
            str: The API endpoint used by the client instance.
        """
        return self._client._api_endpoint

    @property
    def universe_domain(self) -> str:
        """Return the universe domain used by the client instance.

        Returns:
            str: The universe domain used
                by the client instance.
        """
        return self._client._universe_domain

    get_transport_class = ErrorStatsServiceClient.get_transport_class

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Optional[
            Union[
                str,
                ErrorStatsServiceTransport,
                Callable[..., ErrorStatsServiceTransport],
            ]
        ] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the error stats service async client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Optional[Union[str,ErrorStatsServiceTransport,Callable[..., ErrorStatsServiceTransport]]]):
                The transport to use, or a Callable that constructs and returns a new transport to use.
                If a Callable is given, it will be called with the same set of initialization
                arguments as used in the ErrorStatsServiceTransport constructor.
                If set to None, a transport is chosen automatically.
            client_options (Optional[Union[google.api_core.client_options.ClientOptions, dict]]):
                Custom options for the client.

                1. The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client when ``transport`` is
                not explicitly provided. Only if this property is not set and
                ``transport`` was not explicitly provided, the endpoint is
                determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment
                variable, which have one of the following values:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto-switch to the
                default mTLS endpoint if client certificate is present; this is
                the default value).

                2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide a client certificate for mTLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

                3. The ``universe_domain`` property can be used to override the
                default "googleapis.com" universe. Note that ``api_endpoint``
                property still takes precedence; and ``universe_domain`` is
                currently not supported for mTLS.

            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = ErrorStatsServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

        if CLIENT_LOGGING_SUPPORTED and _LOGGER.isEnabledFor(
            std_logging.DEBUG
        ):  # pragma: NO COVER
            _LOGGER.debug(
                "Created client `google.devtools.clouderrorreporting_v1beta1.ErrorStatsServiceAsyncClient`.",
                extra={
                    "serviceName": "google.devtools.clouderrorreporting.v1beta1.ErrorStatsService",
                    "universeDomain": getattr(
                        self._client._transport._credentials, "universe_domain", ""
                    ),
                    "credentialsType": f"{type(self._client._transport._credentials).__module__}.{type(self._client._transport._credentials).__qualname__}",
                    "credentialsInfo": getattr(
                        self.transport._credentials, "get_cred_info", lambda: None
                    )(),
                }
                if hasattr(self._client._transport, "_credentials")
                else {
                    "serviceName": "google.devtools.clouderrorreporting.v1beta1.ErrorStatsService",
                    "credentialsType": None,
                },
            )

    async def list_group_stats(
        self,
        request: Optional[
            Union[error_stats_service.ListGroupStatsRequest, dict]
        ] = None,
        *,
        project_name: Optional[str] = None,
        time_range: Optional[error_stats_service.QueryTimeRange] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListGroupStatsAsyncPager:
        r"""Lists the specified groups.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import errorreporting_v1beta1

            async def sample_list_group_stats():
                # Create a client
                client = errorreporting_v1beta1.ErrorStatsServiceAsyncClient()

                # Initialize request argument(s)
                request = errorreporting_v1beta1.ListGroupStatsRequest(
                    project_name="project_name_value",
                )

                # Make the request
                page_result = client.list_group_stats(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.errorreporting_v1beta1.types.ListGroupStatsRequest, dict]]):
                The request object. Specifies a set of ``ErrorGroupStats`` to return.
            project_name (:class:`str`):
                Required. The resource name of the Google Cloud Platform
                project. Written as ``projects/{projectID}`` or
                ``projects/{projectNumber}``, where ``{projectID}`` and
                ``{projectNumber}`` can be found in the `Google Cloud
                console <https://support.google.com/cloud/answer/6158840>`__.
                It may also include a location, such as
                ``projects/{projectID}/locations/{location}`` where
                ``{location}`` is a cloud region.

                Examples: ``projects/my-project-123``,
                ``projects/5551234``,
                ``projects/my-project-123/locations/us-central1``,
                ``projects/5551234/locations/us-central1``.

                For a list of supported locations, see `Supported
                Regions <https://cloud.google.com/logging/docs/region-support>`__.
                ``global`` is the default when unspecified. Use ``-`` as
                a wildcard to request group stats from all regions.

                This corresponds to the ``project_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            time_range (:class:`google.cloud.errorreporting_v1beta1.types.QueryTimeRange`):
                Optional. List data for the given time range. If not
                set, a default time range is used. The field
                [time_range_begin]
                [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsResponse.time_range_begin]
                in the response will specify the beginning of this time
                range. Only [ErrorGroupStats]
                [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats]
                with a non-zero count in the given time range are
                returned, unless the request contains an explicit
                [group_id]
                [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsRequest.group_id]
                list. If a [group_id]
                [google.devtools.clouderrorreporting.v1beta1.ListGroupStatsRequest.group_id]
                list is given, also [ErrorGroupStats]
                [google.devtools.clouderrorreporting.v1beta1.ErrorGroupStats]
                with zero occurrences are returned.

                This corresponds to the ``time_range`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.errorreporting_v1beta1.services.error_stats_service.pagers.ListGroupStatsAsyncPager:
                Contains a set of requested error
                group stats.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_name, time_range]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, error_stats_service.ListGroupStatsRequest):
            request = error_stats_service.ListGroupStatsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_name is not None:
            request.project_name = project_name
        if time_range is not None:
            request.time_range = time_range

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_group_stats
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("project_name", request.project_name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListGroupStatsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def list_events(
        self,
        request: Optional[Union[error_stats_service.ListEventsRequest, dict]] = None,
        *,
        project_name: Optional[str] = None,
        group_id: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> pagers.ListEventsAsyncPager:
        r"""Lists the specified events.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import errorreporting_v1beta1

            async def sample_list_events():
                # Create a client
                client = errorreporting_v1beta1.ErrorStatsServiceAsyncClient()

                # Initialize request argument(s)
                request = errorreporting_v1beta1.ListEventsRequest(
                    project_name="project_name_value",
                    group_id="group_id_value",
                )

                # Make the request
                page_result = client.list_events(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.errorreporting_v1beta1.types.ListEventsRequest, dict]]):
                The request object. Specifies a set of error events to
                return.
            project_name (:class:`str`):
                Required. The resource name of the Google Cloud Platform
                project. Written as ``projects/{projectID}`` or
                ``projects/{projectID}/locations/{location}``, where
                ``{projectID}`` is the `Google Cloud Platform project
                ID <https://support.google.com/cloud/answer/6158840>`__
                and ``{location}`` is a Cloud region.

                Examples: ``projects/my-project-123``,
                ``projects/my-project-123/locations/global``.

                For a list of supported locations, see `Supported
                Regions <https://cloud.google.com/logging/docs/region-support>`__.
                ``global`` is the default when unspecified.

                This corresponds to the ``project_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            group_id (:class:`str`):
                Required. The group for which events shall be returned.
                The ``group_id`` is a unique identifier for a particular
                error group. The identifier is derived from key parts of
                the error-log content and is treated as Service Data.
                For information about how Service Data is handled, see
                `Google Cloud Privacy
                Notice <https://cloud.google.com/terms/cloud-privacy-notice>`__.

                This corresponds to the ``group_id`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.errorreporting_v1beta1.services.error_stats_service.pagers.ListEventsAsyncPager:
                Contains a set of requested error
                events.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_name, group_id]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, error_stats_service.ListEventsRequest):
            request = error_stats_service.ListEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_name is not None:
            request.project_name = project_name
        if group_id is not None:
            request.group_id = group_id

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.list_events
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("project_name", request.project_name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEventsAsyncPager(
            method=rpc,
            request=request,
            response=response,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_events(
        self,
        request: Optional[Union[error_stats_service.DeleteEventsRequest, dict]] = None,
        *,
        project_name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, Union[str, bytes]]] = (),
    ) -> error_stats_service.DeleteEventsResponse:
        r"""Deletes all error events of a given project.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import errorreporting_v1beta1

            async def sample_delete_events():
                # Create a client
                client = errorreporting_v1beta1.ErrorStatsServiceAsyncClient()

                # Initialize request argument(s)
                request = errorreporting_v1beta1.DeleteEventsRequest(
                    project_name="project_name_value",
                )

                # Make the request
                response = await client.delete_events(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.errorreporting_v1beta1.types.DeleteEventsRequest, dict]]):
                The request object. Deletes all events in the project.
            project_name (:class:`str`):
                Required. The resource name of the Google Cloud Platform
                project. Written as ``projects/{projectID}`` or
                ``projects/{projectID}/locations/{location}``, where
                ``{projectID}`` is the `Google Cloud Platform project
                ID <https://support.google.com/cloud/answer/6158840>`__
                and ``{location}`` is a Cloud region.

                Examples: ``projects/my-project-123``,
                ``projects/my-project-123/locations/global``.

                For a list of supported locations, see `Supported
                Regions <https://cloud.google.com/logging/docs/region-support>`__.
                ``global`` is the default when unspecified.

                This corresponds to the ``project_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry_async.AsyncRetry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.

        Returns:
            google.cloud.errorreporting_v1beta1.types.DeleteEventsResponse:
                Response message for deleting error
                events.

        """
        # Create or coerce a protobuf request object.
        # - Quick check: If we got a request object, we should *not* have
        #   gotten any keyword arguments that map to the request.
        flattened_params = [project_name]
        has_flattened_params = (
            len([param for param in flattened_params if param is not None]) > 0
        )
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        # - Use the request object if provided (there's no risk of modifying the input as
        #   there are no flattened fields), or create one.
        if not isinstance(request, error_stats_service.DeleteEventsRequest):
            request = error_stats_service.DeleteEventsRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if project_name is not None:
            request.project_name = project_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = self._client._transport._wrapped_methods[
            self._client._transport.delete_events
        ]

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("project_name", request.project_name),)
            ),
        )

        # Validate the universe domain.
        self._client._validate_universe_domain()

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self) -> "ErrorStatsServiceAsyncClient":
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)

if hasattr(DEFAULT_CLIENT_INFO, "protobuf_runtime_version"):  # pragma: NO COVER
    DEFAULT_CLIENT_INFO.protobuf_runtime_version = google.protobuf.__version__


__all__ = ("ErrorStatsServiceAsyncClient",)

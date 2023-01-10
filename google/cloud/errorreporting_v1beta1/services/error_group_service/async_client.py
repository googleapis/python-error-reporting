# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
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
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
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
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.errorreporting_v1beta1.types import common
from google.cloud.errorreporting_v1beta1.types import error_group_service
from .transports.base import ErrorGroupServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import ErrorGroupServiceGrpcAsyncIOTransport
from .client import ErrorGroupServiceClient


class ErrorGroupServiceAsyncClient:
    """Service for retrieving and updating individual error groups."""

    _client: ErrorGroupServiceClient

    DEFAULT_ENDPOINT = ErrorGroupServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = ErrorGroupServiceClient.DEFAULT_MTLS_ENDPOINT

    error_group_path = staticmethod(ErrorGroupServiceClient.error_group_path)
    parse_error_group_path = staticmethod(
        ErrorGroupServiceClient.parse_error_group_path
    )
    common_billing_account_path = staticmethod(
        ErrorGroupServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        ErrorGroupServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(ErrorGroupServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        ErrorGroupServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        ErrorGroupServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        ErrorGroupServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(ErrorGroupServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        ErrorGroupServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(ErrorGroupServiceClient.common_location_path)
    parse_common_location_path = staticmethod(
        ErrorGroupServiceClient.parse_common_location_path
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
            ErrorGroupServiceAsyncClient: The constructed client.
        """
        return ErrorGroupServiceClient.from_service_account_info.__func__(ErrorGroupServiceAsyncClient, info, *args, **kwargs)  # type: ignore

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
            ErrorGroupServiceAsyncClient: The constructed client.
        """
        return ErrorGroupServiceClient.from_service_account_file.__func__(ErrorGroupServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

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
        return ErrorGroupServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> ErrorGroupServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            ErrorGroupServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(ErrorGroupServiceClient).get_transport_class, type(ErrorGroupServiceClient)
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, ErrorGroupServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the error group service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.ErrorGroupServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = ErrorGroupServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def get_group(
        self,
        request: Optional[Union[error_group_service.GetGroupRequest, dict]] = None,
        *,
        group_name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> common.ErrorGroup:
        r"""Get the specified group.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import errorreporting_v1beta1

            async def sample_get_group():
                # Create a client
                client = errorreporting_v1beta1.ErrorGroupServiceAsyncClient()

                # Initialize request argument(s)
                request = errorreporting_v1beta1.GetGroupRequest(
                    group_name="group_name_value",
                )

                # Make the request
                response = await client.get_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.errorreporting_v1beta1.types.GetGroupRequest, dict]]):
                The request object. A request to return an individual
                group.
            group_name (:class:`str`):
                Required. The group resource name. Written as
                ``projects/{projectID}/groups/{group_name}``. Call
                ```groupStats.list`` <https://cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats/list>`__
                to return a list of groups belonging to this project.

                Example: ``projects/my-project-123/groups/my-group``

                This corresponds to the ``group_name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.errorreporting_v1beta1.types.ErrorGroup:
                Description of a group of similar
                error events.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([group_name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = error_group_service.GetGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if group_name is not None:
            request.group_name = group_name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_group,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("group_name", request.group_name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_group(
        self,
        request: Optional[Union[error_group_service.UpdateGroupRequest, dict]] = None,
        *,
        group: Optional[common.ErrorGroup] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> common.ErrorGroup:
        r"""Replace the data for the specified group.
        Fails if the group does not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import errorreporting_v1beta1

            async def sample_update_group():
                # Create a client
                client = errorreporting_v1beta1.ErrorGroupServiceAsyncClient()

                # Initialize request argument(s)
                request = errorreporting_v1beta1.UpdateGroupRequest(
                )

                # Make the request
                response = await client.update_group(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.errorreporting_v1beta1.types.UpdateGroupRequest, dict]]):
                The request object. A request to replace the existing
                data for the given group.
            group (:class:`google.cloud.errorreporting_v1beta1.types.ErrorGroup`):
                Required. The group which replaces
                the resource on the server.

                This corresponds to the ``group`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.errorreporting_v1beta1.types.ErrorGroup:
                Description of a group of similar
                error events.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([group])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = error_group_service.UpdateGroupRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if group is not None:
            request.group = group

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_group,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("group.name", request.group.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("ErrorGroupServiceAsyncClient",)

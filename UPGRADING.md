# 1.0.0 Migration Guide

The 1.0 release of the `google-cloud-error-reporting` client is a significant upgrade based on a [next-gen code generator](https://github.com/googleapis/gapic-generator-python), and includes substantial interface changes. Existing code written for earlier versions of this library will likely require updates to use this version. This document describes the changes that have been made, and what you need to do to update your usage.

If you experience issues or have questions, please file an [issue](https://github.com/googleapis/python-error-reporting/issues).

## Supported Python Versions

> **WARNING**: Breaking change

The 1.0.0 release requires Python 3.6+.


## Method Calls

> **WARNING**: Breaking change

Methods expect request objects. We provide a script that will convert most common use cases.

* Install the library

```py
python3 -m pip install google-cloud-error-reporting
```

* The script `fixup_errorreporting_v1beta1_keywords.py` is shipped with the library. It expects
an input directory (with the code to convert) and an empty destination directory.

```sh
$ fixup_errorreporting_v1beta1_keywords.py --input-directory .samples/ --output-directory samples/
```

**Before:**
```py
from google.cloud import errorreporting_v1beta1

client = errorreporting_v1beta1.AccessApprovalClient()

settings = client.get_access_approval_settings(name="name")
```


**After:**
```py
from google.cloud import errorreporting_v1beta1

client = errorreporting_v1beta1.AccessApprovalClient()

settings = client.get_access_approval_settings(request = {'name': "name"})
```

### More Details

In `google-cloud-error-reporting<1.0.0`, parameters required by the API were positional parameters and optional parameters were keyword parameters.

**Before:**
```py
    def update_access_approval_settings(
        self,
        settings=None,
        update_mask=None,
        retry=google.api_core.gapic_v1.method.DEFAULT,
        timeout=google.api_core.gapic_v1.method.DEFAULT,
        metadata=None,
    ):
```

In the 1.0.0 release, all methods have a single positional parameter `request`. Method docstrings indicate whether a parameter is required or optional.

Some methods have additional keyword only parameters. The available parameters depend on the `google.api.method_signature` annotation specified by the API producer.


**After:**
```py
    def update_access_approval_settings(
        self,
        request: errorreporting_v1beta1.UpdateAccessApprovalSettingsMessage = None,
        *,
        settings: errorreporting_v1beta1.AccessApprovalSettings = None,
        update_mask: field_mask.FieldMask = None,
        retry: retries.Retry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> errorreporting_v1beta1.AccessApprovalSettings:
```

> **NOTE:** The `request` parameter and flattened keyword parameters for the API are mutually exclusive.
> Passing both will result in an error.


Both of these calls are valid:

```py
response = client.update_access_approval_settings(
    request={
        "settings": settings,
        "update_mask": update_mask,
    }
)
```

```py
response = client.update_access_approval_settings(
    settings=settings,
    update_mask=update_mask,
)
```

This call is invalid because it mixes `request` with a keyword argument `update_mask`. Executing this code
will result in an error.

```py
response = client.list_builds(
    request={
        "settings": settings,
    },
    update_mask=update_mask
)
```



## Enums and Types


> **WARNING**: Breaking change

The submodules `enums` and `types` have been removed.

**Before:**
```py
from google.cloud import errorreporting_v1beta1

level = errorreporting_v1beta1.enums.EnrollmentLevel.BLOCK_ALL
settings = errorreporting_v1beta1.types.AccessApprovalSettings(name="name")
```


**After:**
```py
from google.cloud import errorreporting_v1beta1

level = errorreporting_v1beta1.EnrollmentLevel.BLOCK_ALL
settings = errorreporting_v1beta1.AccessApprovalSettings(name="name")
```
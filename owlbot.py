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

import json
import os
from pathlib import Path
import shutil

import synthtool as s
import synthtool.gcp as gcp
from synthtool.languages import python

# ----------------------------------------------------------------------------
# Copy the generated client from the owl-bot staging directory
# ----------------------------------------------------------------------------

clean_up_generated_samples = True

# Load the default version defined in .repo-metadata.json.
default_version = json.load(open(".repo-metadata.json", "rt")).get("default_version")

for library in s.get_staging_dirs(default_version):
    if clean_up_generated_samples:
        shutil.rmtree("samples/generated_samples", ignore_errors=True)
        clean_up_generated_samples = False

    s.move(
        [library],
        excludes=[
            "**/gapic_version.py",
            "docs/index.rst",
            "google/cloud/errorreporting/",
            "setup.py",
            "testing/constraints-3.7.txt",
            "testing/constraints-3.8.txt",
        ],
    )
s.remove_staging_dirs()

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------

templated_files = gcp.CommonTemplates().py_library(
    cov_level=100,
    microgenerator=True,
    versions=gcp.common.detect_versions(path="./google", default_first=True),
)
s.move(
    templated_files,
    excludes=[
        ".coveragerc",
        ".github/release-please.yml",
        ".github/auto-label.yaml",
        "docs/index.rst",
        "testing/constraints-3.7.txt",
    ],
)

python.py_samples(skip_readmes=True)

# run format session for all directories which have a noxfile
for noxfile in Path(".").glob("**/noxfile.py"):
    s.shell.run(["nox", "-s", "blacken"], cwd=noxfile.parent, hide_output=False)

# --------------------------------------------------------------------------
# Modify test configs
# --------------------------------------------------------------------------

# add shared environment variables to test configs
tracked_subdirs = ["continuous", "presubmit", "samples"]
for subdir in tracked_subdirs:
    for path, subdirs, files in os.walk(f".kokoro/{subdir}"):
        for name in files:
            if name == "common.cfg":
                file_path = os.path.join(path, name)
                s.move(
                    ".kokoro/common_env_vars.cfg",
                    file_path,
                    merge=lambda src, dst, _,: f"{dst}\n{src}",
                )

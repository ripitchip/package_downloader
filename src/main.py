from __future__ import annotations
from typing import List
from pathlib import Path
import subprocess

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

# Directory where RPMs and tar.gz files are stored
RPM_DIR = Path("/tmp/rpm_dir")
PIP_DIR = Path("/tmp/pip_dir")


@app.post("/rpm/")
def create_package_yum(pkg_name: str | list[str]) -> FileResponse:
    """
    Create a tar.gz file for the specified RPM/YUM package(s).

    Args:
    ----
    pkg_name (Union[str, List[str]]): The name of the package to download.

    Returns:
    -------
    FileResponse: A response with the tar.gz file for download.

    """
    if isinstance(pkg_name, str):
        pkg_name = [
            pkg_name,
        ]  # Convert single package name to a list for uniform handling

    package_dirs = []
    try:
        for pkg in pkg_name:
            package_dir = RPM_DIR / pkg
            package_dir.mkdir(parents=True, exist_ok=True)
            package_dirs.append(package_dir)

            # Download the package using yumdownloader
            subprocess.run(
                [
                    "yumdownloader",
                    "--assumeyes",
                    f"--destdir={package_dir}",
                    "--resolve",
                    pkg,
                ],
                check=True,
            )

        # Create a tar.gz file with all downloaded packages
        tar_file = RPM_DIR / "packages.tar.gz"
        subprocess.run(
            ["tar", "-czvf", str(tar_file), "-C", str(RPM_DIR)]
            + [str(d.name) for d in package_dirs],
            check=True,
        )

        # Check if the tar file was created successfully
        if not tar_file.exists():
            raise HTTPException(
                status_code=500,
                detail="Failed to create tar file",
            )

        # Return the tar.gz file as a response
        return FileResponse(
            path=str(tar_file),
            media_type="application/gzip",
            filename=tar_file.name,
        )
    except subprocess.CalledProcessError as err:
        raise HTTPException(
            status_code=500,
            detail="Error occurred while creating the package tar file.",
        ) from err


@app.post("/pip/")
def create_package_pip(pkg_name: str | list[str]) -> FileResponse:
    """
    Create a tar.gz file for the specified python package(s).

    Args:
    ----
    pkg_name (Union[str, List[str]]): The name of the package to download.

    Returns:
    -------
    FileResponse: A response with the tar.gz file for download.

    """
    if isinstance(pkg_name, str):
        pkg_name = [
            pkg_name,
        ]  # Convert single package name to a list for uniform handling

    package_dirs = []
    try:
        for pkg in pkg_name:
            package_dir = PIP_DIR / pkg
            package_dir.mkdir(parents=True, exist_ok=True)
            package_dirs.append(package_dir)

            # Download the package using yumdownloader
            subprocess.run(
                [
                    "pip3.12",
                    "download",
                    "--dest",
                    f"{package_dir}",
                    pkg,
                ],
                check=True,
            )

        # Create a tar.gz file with all downloaded packages
        tar_file = PIP_DIR / "packages.tar.gz"
        subprocess.run(
            ["tar", "-czvf", str(tar_file), "-C", str(PIP_DIR)]
            + [str(d.name) for d in package_dirs],
            check=True,
        )

        # Check if the tar file was created successfully
        if not tar_file.exists():
            raise HTTPException(
                status_code=500,
                detail="Failed to create tar file",
            )

        # Return the tar.gz file as a response
        return FileResponse(
            path=str(tar_file),
            media_type="application/gzip",
            filename=tar_file.name,
        )
    except subprocess.CalledProcessError as err:
        raise HTTPException(
            status_code=500,
            detail="Error occurred while creating the package tar file.",
        ) from err

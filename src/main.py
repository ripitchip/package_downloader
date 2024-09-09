from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os
import subprocess

app = FastAPI()

# Directory where RPMs and tar.gz files are stored
RPM_DIR = "/tmp/rpm_dir"


@app.get("/download/{pkg_name}")
def create_package_tar(pkg_name: str) -> FileResponse:
    package_dir = os.path.join(RPM_DIR, pkg_name)
    os.makedirs(package_dir, exist_ok=True)
    subprocess.run(
        [
            "yumdownloader",
            "--assumeyes",
            "--destdir=" + package_dir,
            "--resolve",
            pkg_name,
        ],
        check=True,
    )
    # Create tar.gz file
    tar_file = os.path.join(RPM_DIR, f"{pkg_name}.tar.gz")
    subprocess.run(
        [
            "tar",
            "-czvf",
            tar_file,
            "-C",
            RPM_DIR,
            pkg_name,
        ],
        check=True,
    )

    # Check if the tar file was created successfully
    if not os.path.exists(tar_file):
        raise HTTPException(status_code=500, detail="Failed to create tar file")

    # Return the tar.gz file as a response
    return FileResponse(
        tar_file,
        media_type="application/gzip",
        filename=os.path.basename(tar_file),
    )

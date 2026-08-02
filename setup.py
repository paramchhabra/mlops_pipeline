import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_desc = f.read()


__version__ = "0.0.0"

REPO_NAME = "mlops_pipeline"
AUTHON_USER_NAME = "paramchhabra"
SRC_REPO = "mlops_pipeline"
AUTHOR_EMAIL = "paramchhabra81@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHON_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Practice Project for MLOPs",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHON_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHON_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")

)
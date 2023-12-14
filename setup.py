import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME = "chicken-disease-classification"
AUTHOR_USER_NAME = " Cganesh80"
SRC_REPO = "chicken-disease-classifier"
AUTHOR_EMAIL = "cganaram800@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for chicken-disease-classifier app",
    long_description=long_description,
    long_description_content="text/markdown",
    url= f"https://github.com/Cganesh80/chicken-disease-classification",
    project_urls={
       "Bug Tracker": f"https://github.com/Cganesh80/chicken-disease-classification/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
from setuptools import setup, find_packages


def get_requirements(file_path: str):
    """
    This function reads requirements.txt and returns list of dependencies
    """
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="books_recommender",   # your src folder name
    version="0.0.1",
    author="SIVA PAPARAO MEDISETTI",
    author_email="msivapaparao@gmail.com",
    description="End-to-End ML Based Book Recommendation System using KNN and Collaborative Filtering",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MSIVAPAPARAO13/End-to-End-Book-Recommendation-System",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    python_requires=">=3.7",
    license="MIT",
)
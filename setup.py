from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-testing-isabella",
    version="0.0.1",
    author="elio junior",
    author_email="eliomaiajunior@gmail.com",
    description="Passo a passo passado por Karina Kato.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ejunior89/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smartexecutor",
    version="1.0.0",
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="Une bibliothèque pour exécuter automatiquement des tâches en utilisant threading ou multiprocessing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mohanned29/Limitations-of-Multithreading-in-Python-and-Task-Optimization",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "requests",
    ],
)

from setuptools import setup

setup(
    name="Carbon+Alt+Delete Client",
    version="2024.02.1",
    description="Client SDK to communicate with the Carbon+Alt+Delete API",
    url="https://github.com/CarbonAltDelete/carbonaltdelete-client",
    author="Carbon+Alt+Delete",
    author_email="support@carbonaltdelete.eu",
    license="MIT",
    packages=["carbon_alt_delete"],
    install_requires=[
        "pydantic[email]",
        "python-jose",
        "requests",
        "rich",
    ],
)

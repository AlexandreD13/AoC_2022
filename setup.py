""" Exemple de setup.py

    https://www.educative.io/answers/what-is-setuppy
"""

# from setuptools import setup
# setup(
#     name='app-name'
#     version='1.0',
#     author='Bejamin Frakline',
#     description='A brief synopsis of the project',
#     long_description='A much longer explanation of the project and helpful resources',
#     url='https://github.com/BenjaminFranline',
#     keywords='development, setup, setuptools',
#     python_requires='>=3.7, <4',
#     packages=find_packages(include=['exampleproject', 'exampleproject.*']),
#     install_requires=[
#         'PyYAML',
#         'pandas==0.23.3',
#         'numpy>=1.14.5',
#         'matplotlib>=2.2.0,,
#         'jupyter'
#     ],
#     package_data={
#         'sample': ['sample_data.csv'],
#     },
#     entry_points={
#         'runners': [
#             'sample=sample:main',
#         ]
#     }
# )
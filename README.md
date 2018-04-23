# m3
Repository for all the examples of my 'Minds mastering machines' workshop

## Requirements

The examples inside this repository are tested with Anaconda 4.5.1, Tensorflow 1.7 and Python 3.5.

## Installation

The examples require a lot of Python packages with the right version. The conda package manager and pip will solve a lot of this relations.


### Anaconda installation

First of all, the Anaconda command line version is needed. You can installation it by downloading the right version from Anaconda server. For macOS you should get 

`https://repo.anaconda.com/archive/Anaconda3-5.1.0-MacOSX-x86_64.sh`

and installed it after with 

``$ bash Anaconda3-5.1.0-MacOSX-x86_64.sh

Anaconda will add the nececary paths for you in your .bash_profile. If you need it in .zshrc or any other shell environment, please add the right path into you environment.

You can check the right installation by typing 

``$ conda --version 

on your shell. In some environments, especelly on enterprise environments, you need to define a proxy server to handle all of your HTTP and HTTPS calls. Therefor you can add a proxy_server entry inside your .condarc file like

<p>
channels:
  - defaults

proxy_servers:
  http: http://USER:PASSWORT@HOST:PORT/
  https: https://USER:PASSWORT@HOST:PORT/

ssl_verify: False
</p>

for exampole. For mare information, please take a look to the Anaconda documentation.
If Anaconda is in a right place, please update the base system like

``$ conda update -n base conda


### TensorFlow and TensorFlow environment

Before we can install TensorFlow, we should create a Anaconda environment first. This environment contains all the Python packages and versions and keeps the system clean for other version and dependencies. To create this kind of special TensorFlow environment, please type

``$ conda create -n tensorflow35 pip python=3.5

into you shell. The conda package manager will install all needed dependencies for you. After this installation procerdure, you can activate this environment by typing

``$ source activate tensorflow35

and deactive the environment by typing

``$ source deactivate

The next step is to install TensorFlow itself with a little bit help of pip:

``$ pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.7.0-py3-none-any.whl

This command install TensorFlow 1.7 with Python3 support. 

### Other packages

Some examples needs help from one of the following additional Python packages:

#### Jupyter Notebook

``$ pip install jupyter

To start the right jupyter notebook, please check the installation twice or start with

``$ ~/anaconda3/envs/tensorflow35/bin/jupyter notebook

#### Matplotlib

``$ pip install matplotlib

#### Pandas

``$ pip install pandas

#### Keras

``$ pip install keras

#### Pillow

``$ pip install Pillow

#### ImageIO

``$ pip install imageio





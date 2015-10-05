### Python application for getting The Hindu editorials

Refer to [this
document](https://github.com/venkateshshukla/th-editorials-server/blob/devel/docs/API.md)
for the details about the web API which this application consumes.

####Steps for running the application

**Dependencies**

To run this application, besides having python the following dependencies are
required :

1. libyaml-dev - On debian based systems, execute `sudo apt-get install
   libyaml-dev`. On rpm based systems, execute `su -c 'yum install
   libyaml-devel'`.

2. python-dev - On debian based systems, execute `sudo apt-get install
   python-dev`. On rpm based systems, run `su -c 'yum install python-dev'`.

3. python-pip - On debian based systems, execute `sudo apt-get install
   python-pip`. On rpm based systems, run `su -c 'yum install python-pip`. Using
   python, pip can be installed by first downloading `get-pip.py` securely using
   `wget` or `curl` and subsequently running `python get-pip.py`.
   [This website](http://pip.readthedocs.org/en/stable/installing) gives you
   more information and the link to download `get-pip.py`.

**Virtual Environment**

Once the above dependencies are taken care of, install `virtualenv` using `pip`.

> sudo pip install virtualenv

Now, virtualenv is useful in creating virtual python environments (as can be
gathered by its name). These virtual environments are useful because it does not
interfere with working of other python applications and their dependencies.
Visit [this website](https://virtualenv.pypa.io/en/latest) for more information
on `virtualenv`.

For now, do the following to setup and use a virtual environment for this
application.

1. Make a directory for the virtual environment. Make sure this is outside the
   source directory and not included in the version control system.

   > virtualenv ../pyenv

   This directory (../pyenv) will contain a separate python file and pip file.
   All installations while virtualenv is active (activation in next step) would
   also go in this directory.

2. Activate the virtual environment by running the `pyenv/bin/activate` file. On
   linux do this using

   > source ../pyenv/bin/activate

   You'll notice that your prompt has changed to include `(pyenv)` at the
   beginning. This means your virtual environment is active.

3. When the task is done, deactivate the virtual environment by executing the
   command.

   > deactivate

**Note :** Henceforth, all the commands listed are to be executed in the virtual
environment. Cross check by looking at the prompt.

**Python dependencies**

Install the python dependencies for this project by running the following
command

> pip install -r requirements.txt

This installs every needed dependency for this application. To view those
dependencies, view `requirements.txt` file.

**Configuration**

Before running the scripts, edit the `data.yml` file to modify the `baseurl`
attribute. It should point towards the deployed
[th-editorials-server](https://github.com/venkateshshukla/th-editorials-server/).

**Finally, the scripts**

Now, run the python scripts

> python script_name.py

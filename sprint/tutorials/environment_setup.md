
(environment_setup)=
# Environment setup

## Pre-requisites

### GitHub account
To contribute you'll need a GitHub account. You can create one from [this link](https://github.com/join)

::::{sidebar} New to Git and GitHub?
We have tried to cover all the steps and include both input and output, to make
sure you can follow this tutorial without knowing Git.
However, if you want to learn about Git and understand what is going on,
we recommend [this dataschool tutorial](https://www.dataschool.io/how-to-contribute-on-github/)
::::

### Install Git

::::{tab-set}
:::{tab-item} Linux
:sync: linux
Instructions with installation commands for most Linux distributions
can be found on the [Git project website](https://git-scm.com/download/linux)
:::
:::{tab-item} macosx
:sync: macos
Instructions with installation commands for macosx
can be found on the [Git project
website](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git#_installing_on_macos)
:::
:::{tab-item} Windows
:sync: windows
The recommended way to install Git is using [Git for Windows](https://git-scm.com/download/win).
:::
::::

### Install conda
We recommend you install miniconda and follow the steps below to install only
the libraries you'll need.

::::{tab-set}
:::{tab-item} Linux
:sync: linux
Miniconda installation instructions for linux are available on the [conda website](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)
:::
:::{tab-item} macosx
:sync: macos
Miniconda installation instructions for macosx are available on the [conda website](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html)
:::
:::{tab-item} Windows
:sync: windows
Miniconda installation instructions for windows are available on the [conda website](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html)
:::
::::

### Text editor
You might already have a text editor installed. Check if you have any editor from
the list below, otherwise install _one_, any will do:

* [Atom](https://atom.io/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Sublime text](https://www.sublimetext.com/)
* [PyCharm (community)](https://www.jetbrains.com/pycharm/download)

## Fork the pymc repo
Fork the [project repository](https://github.com/pymc-devs/pymc/)
by clicking on the 'Fork' button near the top right of the main repository page.

![fork_button](https://docs.github.com/assets/cb-6294/images/help/repository/fork_button.jpg)

This creates a copy of the code under your GitHub user account.
You should now see that `https://github.com/<your GitHub handle>/pymc/` exists

## Create a feature branch

```bash
git checkout -b docstring_update
```
and check git indicates you the branch change was successful:
```none
S'ha canviat a la branca nova «docstring_update»
```

:::{tip}
Keep your branch names informative, use one branch per PR and **never**
work on `main`.
:::

:::{admonition} Getting ready for the 2nd PR?
:class: dropdown, attention

If you haven't changed to a different branch, you'll still be in the `docstring_update` one,
but you don't want to work there! Remember, one branch per PR.

_Before_ starting to work on the new changes, move back to main,
update your local copy and then create the new branch.

```
git checkout main
git fetch upstream
git rebase upstream/main
git checkout -b branch_for_2nd_pr
```
:::


## Install PyMC

::::{tab-set}
:::{tab-item} Linux
:sync: linux
```bash
conda env create -f conda-envs/environment-dev-py38.yml
```
:::
:::{tab-item} macosx
:sync: macos
```bash
conda env create -f conda-envs/environment-dev-py38.yml
```
:::
:::{tab-item} Windows
:sync: windows
```
conda env create -f conda-envs/windows-environment-dev-py38.yml
```
:::
::::

This command can also take a while, but should start writing output
immediately. If it finishes successfully, the last lines printed will
be:

```none
done
#
# To activate this environment, use
#
#     $ conda activate pymc-dev-py38
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

Activate the environment and install pymc:
```bash
conda activate pymc-dev-py38
```
This command has no output, but generally adds the environment
name to the start of the command line. If you want, you can check
it has worked with the command `conda list` which should print
all the packages installed, starting with:

```none
# packages in environment at /home/oriol/miniconda3/envs/pymc-dev-py38:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                 conda_forge    conda-forge
_openmp_mutex             4.5                       1_gnu    conda-forge
aeppl                     0.0.18             pyhd8ed1ab_0    conda-forge
aesara                    2.3.2            py38hdc754fd_0    conda-forge
```

Install PyMC:
```bash
pip install -e .
```
We already installed all the dependencies so this should not take long.
If successful, the last printed line will be

```none
Successfully installed pymc-4.0.0b2
```

Then activate `pre-commit`. It will help auto formatting the code for you.

```bash
pre-commit install
```
on success will show
```none
pre-commit installed at .git/hooks/pre-commit
```

Your system is now ready! You are ready to do your first PR.

:::{div} sd-text-center sd-fs-1
{fas}`star;sd-fs-1 sd-text-warning`
:::


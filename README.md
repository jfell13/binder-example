# binder-example
This repo is meant to be an example for using binder.

[![DOI](https://zenodo.org/badge/222008654.svg)](https://zenodo.org/badge/latestdoi/222008654)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/zenodo/10.5281/zenodo.3543808/)

To make a binder, you first need to have a github repository that has the following:

*runtime.txt
*requirements.txt
*readme.md

Within the runtime.txt file, you need to specifiy the coding language and version used.
Example:
`python-3.6).`

Within the requirements.txt you include which modules are required and their specific versions.
Example:
`pandas==0.25.2
matplotlib==3.1.1`

The readme.md will be used to hold the zenodo and binder links, as well as a description of your repo.

Once you have these files ready and your repo is ready for publishing, the next step is too make a release of your repo.
Just click on the `releases` button within your repo, then choose `draft a new release`.  If this is your first release of the repo, make this release version v1.0. Fill out the release title and description.

The next step is making a zenodo DOI. Go to `https://zenodo.org/`, make an account and link your zenodo account to your github account. Once your accounts are linked go to the github page of zenodo, find the repo you want to share and click `ON`. This will make a zenodo DOI that you can share.

The last step is creating the binder. Go to `https://mybinder.org/`, and you can either choose to link via a zenodo DOI (preferred) or github link. Enter the link and the form will fill out a copy-able link to your new binder. 

Copy the links from zenodo and binder into your readme.md in your repo to let other people cite and use your repo!

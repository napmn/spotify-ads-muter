#!/bin/bash

virtualenv_name=venv
project_dir=$(dirname -- "$(readlink -- "$BASH_SOURCE")")

source $project_dir/$virtualenv_name/bin/activate
python $project_dir/spotify_ads_muter.py

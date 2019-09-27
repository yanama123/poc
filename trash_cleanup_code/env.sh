virtualenv tas_venv -p python3.6 --never-download
source tas_venv/bin/activate
pip install -r requirements.txt
python worker.py

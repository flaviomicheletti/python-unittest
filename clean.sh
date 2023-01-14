echo "Remove __pycache__ files"
sudo find . -type d -name __pycache__ -exec rm -r {} \+
sudo find . -type d -name .pytest_cache -exec rm -r {} \+
sudo find . -type d -name __queuestorage__ -exec rm -r {} \+
sudo find . -type d -name .venv -exec rm -r {} \+        
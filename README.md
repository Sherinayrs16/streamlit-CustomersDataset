## Setup Environment - Miniconda
```
conda create --name myenv python=3.12.4
conda activate myenv
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir CustomerDataset
cd CustomerDataset
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run stream-datasetcustomer.py
```

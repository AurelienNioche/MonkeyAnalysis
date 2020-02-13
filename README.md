# Monkey Analysis


## Config

* Install Python3 (and pip) 
        
        # [on Mac using brew]
        brew install python3
        
        
* Create a virtual environment (optional)

    source venv/bin/activate
    
    (If using venv, replace 'pip3' by pip)

* Python libraries

        pip3 install -r requirements.txt

* Django setup

        python3 manage.py makemigrations
        python3 manage.py migrate
        
    For data viewing (optional if only doing analysis)
        
        python3 manage.py createsuperuser
        
 
 * Import data from excel file
 
        python3 import_xlsx.py
        

## Data viewing

* Launch the server
    
       python3 manage.py runserver
    
    
* Go to http://127.0.0.1:8000/

## Run analysis

    python3 main.py
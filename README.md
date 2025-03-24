# GeoJSON Backend Assignment
This django application features a small REST API to view and update GeoJSON fature objects representing municipalities.
The api allows all CRUD operations and filtering municipalities with a boundingbox.

## Setup
To run this app you need
  - python3
  - a postgres database with PostGIS installed

The file `requirements.txt` contains all required python packages.
These can be installed using `pip`: `pip install -r requirements.txt`.
Using a virtual environment is highly recommended. 

To create a database, make sure you have postgres installed.
Create a database with the PosGIS extension enabled.
See [django's documentation](https://docs.djangoproject.com/en/5.1/ref/contrib/gis/install/postgis/) on how to install PostGIS and enable the extension.\
The database settings in `geojson_backend/settings.py` are configured for a database on `localhost` and standard postgres port `5432`, with name, user and password `geodjango`.
Feel free to adjust this to your liking.

#### A note on security
This project lists its database password as plaintext in a settings file.
In any other context than local testing, this is not safe.
Sensitive information such as passwords should be left out of repositories and be read from a local source, configured on the server.
The same goes in lesser extent for the database name and username.\
Since this is an assignment which is not supposed to be deployed anywhere, I kept it like this out of simplicity.

After setting up the database and environment run the Django migrations to finish: `python manage.py migrate` and run the server with `python manage.py runserver`.

## Usage

### Seed database

To use the application it first needs data.
A dataset has been provided in the `data` folder.
The script `upload_municipailities.py` can be used to upload the data.\
Make sure the application is up and running by executing the `python manage.py runserver` command in your chosen environment.

The script `upload_municipailities.py` expects two commandline arguments:
- data_filename: the source datafile, containing geojson municipality information.
- url: the creation endpoint to send the creation request to.

E.g. with the project running on `localhost`,port `8000` and running the scripts in its own folder:\
`python upload_municipality_data.py data/municipalities_nl.geojson http://localhost:8000/rest_api/municipalities/ `

### Using the API

Conforming to the DRF format the api has two urls with multiple uses/endpoints:
- `rest_api/municipalities/`
- `rest_api/municipalities/<int:pk>/`

The first retrieves all available municipality data and can be used to add a new municipality.
The second can be used to retrieve a specific municipality and update or delete it.
Both endpoints can return the data in json by using the `format=json` url arguments.
Retrieving all municipalities can be filtered by a bounding box by using the `in_bbox` url argument and two points which define the bounding box, e.g.: `/rest_api/municipalities/?in_bbox=6,52,7,53`
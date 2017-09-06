# Open Source Ratsinformationssystem

Open Source RIS für Prototype Fund

## Development

### Installing the project

Create a virtualenv at `venv`. Add a local domain https://opensourceris.local/ with self-signed certificates in your webserver which redirects to localhost:8080

```bash
pip install -r requirements.txt
npm install
```

### Starting the development server

```bash
source venv/bin/activate
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

For compiling SCSS/JS automatically:

```bash
npm run watch
```

To load the dummy data for development:

```bash
./manage.py loaddata mainapp/initdata.json
```

To save the modified dummy data

```bash
./manage.py dumpdata mainapp --indent 4 > mainapp/initdata.json
```

### Important URLs:

- https://opensourceris.local/
- https://opensourceris.local/admin/

## Data model

The names of the models and the fields are highly inspired by the OParl standard. 


## Shell commands

Straßen einer Stadt importieren:
```bash
./manage.py import-streets 05315000 1 # Gemeindeschlüssel von Köln, Body-ID 1
```

POIs anhand einer OSM-Amenity importieren:
```bash
./manage.py import-amenities 05315000 school 1 # Gemeindeschlüssel von Köln, Amenity, Body-ID 1
```

Gemeindeschlüssel (Beispiele):
- München: 09162000
- Augsburg: 09761000
- Neumarkt Sankt Veit: 09183129
- Köln: 05315000

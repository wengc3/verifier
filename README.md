# Next Generation E-Voting Visualizer
This application is the result of the bachelor thesis "Universelle Verifizierung des Genfer E-Voting Systems" and has been realized by Christian Wenger
The goal was to complete the bachelor thesis "Visualizing Geneva's Next E-Voting System", which has been realized by Kevin Häni and Yannick Denzer, with a fully developed Verifier. 

# Components

- Backend
  - MongoDB
  - Python 3.5+ and `virtualenv`
- Frontend
  - [Vue.js 2.3.3](https://vuejs.org/)
  - [Vuetify 1.0.0-beta.2](https://vuetifyjs.com/)
  - For a full dependency list, see `frontend/package.json`

- Development
  - Python 3.5+
  - Docker
  - Node
  - Preferrably `tmuxp` and `urxvt`
- Production
  - Docker
  - A reverse proxy like Nginx or Apache

# Production setup

Build the Docker images:
```sh
docker-compose build
```

Start the Docker images:
```sh
docker-compose up
```

As soon as the Docker images have been started, the application will be
available via the following TCP ports:

- MongoDB: 27017
- Backend: 5000
- Frontend: 8080

In order to serve the frontend and make the backend accessible, a reverse proxy is required. As an example, nginx can be used with the following configuration:

```
location / {
        proxy_pass http://127.0.0.1:8080;
}

location ~ ^/api/(.*) {
        proxy_pass http://127.0.0.1:5000/$1;
}

location /socket.io {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_pass_request_headers on;
        proxy_set_header Host localhost;
        proxy_redirect off;
        proxy_buffering off;
        proxy_http_version 1.1;
}
```

# Development setup

Using `tmuxp` and `urxvtc`:

```sh
make dev
```

Alternatively:

1. `docker-compose up mongodb`
2. `cd backend; make dev`
3. `cd frontend; npm install; make dev

## Translations

The main language (English) is stored in the YAML file
`frontend/src/translations.preset.yaml`, as well as manual translations. By
using the translation script `frontend/src/translate.js`, the main languages
can translated automatically to predefined target languages.

Automatical translations (Google Translate) are stored together in the YAML file
`frontend/src/translations.yaml` together with the main language and manual
translations. This file will be used to provide translations for the frontend
application.

**Note:** never edit the file `frontend/src/translations.yaml` directly in order
to store translations.

### Add a new manually translated language

In order to add a new manually translated language, edit the file
`frontend/src/translations.preset.yaml` and adjust the key `_languages` on the
top of the document:

```yaml
_languages:
  - en: English
  - de: Deutsch
  - $NEW_LANGUAGE_CODE: $NEW_LANGUAGE_NAME
```

To add the translations, add the new language code key to each existing key
together with the according translation:

```yaml
close:
  en: Close
  de: Schliessen
  $NEW_LANGUAGE_CODE: $TRANSLATION
```

After adding the new language information, run the following command to start
the automatic translations:

```sh
npm run translate
```

### Add new automatically translated language

In order to add a new automatically translated language, edit the file
`frontend/src/translations.preset.yaml` and adjust the keys `_keep` and
`_languages` on the top of the document:

```yaml
_keep:
  - en
  - de
  - $NEW_LANGUAGE_CODE
_languages:
  - en: English
  - de: Deutsch
  - $NEW_LANGUAGE_CODE: $NEW_LANGUAGE_NAME
```

To generate the automatic translations using Google Translate, run the
following command:

```sh
npm run translate-auto
```

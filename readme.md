# Roy Dumps

Simple Python + Flask app with Docker support.

## Run locally

```bash
docker build -t royapp .
docker run -d -p 3000:3000 --name royapp-container royapp

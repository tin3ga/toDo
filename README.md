# toDo

Simple ToDo web application.

![Docker Image Build](https://github.com/tin3ga/toDo/actions/workflows/docker-build.yml/badge.svg)
![Vercel Deploy](https://therealsujitk-vercel-badge.vercel.app/?app=todo-phi-blue)
![GitHub top language](https://img.shields.io/github/languages/top/tin3ga/toDo)
![GitHub License](https://img.shields.io/github/license/tin3ga/toDo)
![GitHub last commit](https://img.shields.io/github/last-commit/tin3ga/toDo)

## Technologies

- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/intro.html#documentation-overview)
- [gunicorn](https://gunicorn.org/#quickstart)
- [flask-login](https://flask-login.readthedocs.io/en/latest/)
- [vercel](https://vercel.com/docs)
- [PostgreSQL](http://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

- ...

## Demo

![toDo Gif](https://res.cloudinary.com/tinegadev/image/upload/v1698136447/gif_demo/tcniszydkm2zmbjqvpcm.gif)

## Quick Start

1. Clone the repo:

```
$ git clone https://github.com/tin3ga/toDo.git
$ cd toDo
```

2. Initialize and activate a virtualenv:

```
# windows
$ python -m venv venv
$ venv\Scripts\activate

# mac/linux
$ python -m venv venv
$ source env/bin/activate or . venv/bin/activate
```

3. Install the dependencies:

```
$ pip install -r requirements.txt
```

4. Navigate to todo:

```
$ cd todo
```

5. Run the development server:

```
$ python main.py
```

6. Navigate to [http://localhost:5000](http://localhost:5000)

## Build and start the application using Docker Compose:

1. Build images and run containers in the background, run:

```bash
docker compose up -d --build
```

Visit [http://localhost](http://localhost:80) in your web browser.

## Stopping the Application

2. To stop the application and remove the containers, run:

```bash
docker compose down --rmi local
```

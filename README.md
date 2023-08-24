# bard-api

Bard API with FastAPI

## Install

### Create Env (Mac)

- python -m venv bardapi
- bardapi/bin/activate

### Install libs

```shell
pip install fastapi uvicorn
```

> Create requirements
>
> ```shell
> pip freeze > requirements.txt
> ```

### Run

```shell
uvicorn main:app --reload --port 5040 --host 0.0.0.0
```

- reload: Automatically reload
- port: Port to run
- host: 0.0.0.0 public scope

## Work History

### Swagger

- Access
  ```
  http://localhost:5040/docs
  ```

#### Tips

- app.title: Title for API Swagger.
- app.version: Version.
- @app.get(route, tags): Tags are added to each route.

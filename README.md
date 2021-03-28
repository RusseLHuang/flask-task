# Run using docker compose

Build local docker image
```
docker-compose build
```

Run
```
docker-compose up -d
```

> Apply database migration after database is running: alembic upgrade head

# Unit Test

# Migration Script

## Generate
```
alembic revision -m "${REVISION_MESSAGE}"
```

## Apply
```
alembic upgrade head
```
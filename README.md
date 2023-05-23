# Quiz API

Quiz API generates random questions

Database: Postgresql

## Startup

Use [docker-compose](https://docs.docker.com/compose/) to start project.

Edit env.example to .env and enter your data


For start project use:
```bash
docker compose up
```

## API

### Endpoints

POST /questions - Get new questions

```bash
curl -X 'POST' \
  'http://localhost:8000/questions/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions_num": 1
}'
```
Answer 
```json
{
  "id": 0,
  "question": "string",
  "answer": "string",
  "created_at": "2023-05-23T16:48:41.883Z"
}
```
### API DOCS /docs

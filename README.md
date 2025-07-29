### function-from-zero
Training from Coursera

[![Python application test with Github Actions](https://github.com/Arjuninet/function-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/Arjuninet/function-from-zero/actions/workflows/main.yml)

### To call the microservices

```bash
curl -X 'POST' \
  'https://literate-space-couscous-wwjvpq7ppxxc57xq-8000.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Mircosoft"
}'
```

### Build Container
`docker build .`
`docker image ls`

### Run Container
somthing like this

`docker run 127.0.0.1:8000:8000 fdda411807a1`
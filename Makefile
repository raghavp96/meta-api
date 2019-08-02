PORT=8080

build:
	docker build -t api-svc .

run:
	docker run --name api-svc -p 8000:$(PORT) --detach api-svc

stop:
	docker stop api-svc
	docker container rm api-svc

clean:
	docker container prune
	docker image prune -a
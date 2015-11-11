target:=vie_apache_mysqlclient
host:=localhost
port:=5000

build:
	docker build -t ${target} .

rebuild:
	docker build -t ${target} --no-cache .

run: build
	docker run -dit --name ${target} ${target}

stoprm:
	docker stop ${target}
	docker rm ${target}

rerun: stoprm run

exec: run
	docker exec -it ${target} bash

tag:
	docker tag ${target} ${host}:${port}/${target}

push: tag
	docker push ${host}:${port}/${target}

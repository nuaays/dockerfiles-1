target:=vie_apache_proxy

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

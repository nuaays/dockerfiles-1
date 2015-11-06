target:=vie_apache

build:
	docker build -t ${target} .

run: build
	docker run -dit --name ${target} ${target}

stoprm:
	docker stop ${target}
	docker rm ${target}

rerun: stoprm run

exec: run
	docker exec -it ${target} bash

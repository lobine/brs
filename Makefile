SQL = mysql:8.0.23
PY  = pythonsql

.PHONY: db
db:
	docker run --name=bourse \
		--detach \
		--volume=`pwd`/data:/data \
		--env=MYSQL_ROOT_PASSWORD=root \
		--publish=3306:3306 \
		$(SQL) --datadir=/data

.PHONY: build-pythonsql
build-pythonsql: build.Dockerfile.pythonsql
	docker build -f $< -t $(PY) .

.PHONY: run-generate
run-generate: python/generate.py
	docker run --rm -t --volume=`pwd`/python:/run $(PY) \
		python /run/generate.py

.PHONY: run-populate
run-populate: python/populate.py
	docker run --rm -t --volume=`pwd`/python:/run $(PY) \
		python /run/populate.py

.PHONY: run-test-query
run-test-query: python/test_query.py
	docker run --rm -t --volume=`pwd`/python:/run $(PY) \
		python /run/test_query.py

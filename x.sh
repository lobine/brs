#!/bin/bash

PY=pythonsql

function import_nasdaq {
	docker run --rm -t \
        --volume=`pwd`/python:/run \
        --volume=`pwd`/csv:/data \
        ${PY} python /run/import_nasdaq.py $1 $2 /data
}

import_nasdaq "$1" "$2"

#Makefile

install:
	poetry install

start:
	poetry run python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker
	
lint: # run_linter
	poetry run flake8 task_manager
	
build:
	./build.sh
	
stop:
	sudo fuser -k 8000/tcp
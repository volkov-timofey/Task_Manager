#Makefile

install:
	poetry install

	
lint: # run_linter
	poetry run flake8 task_manager
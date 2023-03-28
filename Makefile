DATE="$(shell date -u +%Y%m%d)"
VERSION="1.1.0-${DATE}-$(shell git rev-parse --short=8 HEAD)"
NAME="garebear"

ifeq (, $(shell which docker))
  $(error "docker was not found your path. Try installing it by going to https://www.docker.com/get-started")
endif

default:setup_local_dev

# Updates the requirements.txt with any pip modules the code is using.
update_requirements_txt: setup_local_dev
	@echo "Updating requirements.txt" 
	source venv/bin/activate && \
	  pipreqs --force  ./ && \
	  pip --isolated install -r requirements.txt

# Creates a python virtual environment (venv).  If it exists nothing happens. 
create_venv:
	@echo "Creating a python virtual environment (venv)" 
	python3 -m venv venv

# Creates a python virtual environment (venv) and installs pip moduels requried to 
# run the app and run tests.
setup_local_dev: create_venv
	@echo "Installing all the pip things" 
	source venv/bin/activate && \
	  pip --isolated install --upgrade pip && \
	  pip install pipreqs && \
	  pip --isolated install -r requirements.txt && \
	  pip --isolated install -r tests/requirements.txt 

	@echo "#### User Instructions ####"
	@echo "To activate type 'source venv/bin/activate'"
	@echo "To deactivate type 'deactivate'"

build_docker:
	@docker build --rm -q -t ${NAME}:${VERSION} .
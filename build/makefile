SHELL=cmd.exe
SEED_BINARY=seedApp

## up: starts all containers in the background without forcing build
build_protos: build_seed_sorting_proto build_helper_sorting_proto
	@echo all protos all generated

build_seed_sorting_proto:
	@echo generating code for seed sorting proto....
	chdir ..\seed-service\proto\sorting && protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative sorting.proto
	@echo Done!

build_helper_sorting_proto:
	@echo generating code for helper sorting proto....
	chdir ..\helper-service\proto && python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. .\sorting.proto
	@echo Done!

start:
	@echo front is up....
	chdir ..\front && node .\x.js

seed:
	@echo starting seed service
	chdir ..\seed-service && go run .\cmd\.

helper:
	@echo starting helper service
	chdir ..\helper-service && python .\grpcServer.py


build_seed:
	@echo Building seedmail binary...
	chdir ..\seed-service && set GOOS=linux&& set GOARCH=amd64&& set CGO_ENABLED=0 && go build -o ${SEED_BINARY} ./cmd/
	@echo Done!

docker_all_build: build_seed
	@echo Stopping docker images (if running...)
	docker-compose down
	@echo Building (when required) and starting docker images...
	docker-compose up --build -d
	@echo Docker images built and started!

docker_all: build_seed
	@echo Stopping docker images (if running...)
	docker-compose down
	@echo Building (when required) and starting docker images...
	docker-compose up -d
	@echo Docker images built and started!

docker_down:
	@echo Stopping docker images (if running...)
	docker-compose down




SHELL=cmd.exe
SEED_BINARY=seedApp

build_protos: build_seed_sorting_proto build_helper_sorting_proto
	@echo proto file codes are generated.

build_seed_sorting_proto:
	@echo generating code for seed sorting proto....
	chdir ..\seed-service\proto\sorting && protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative sorting.proto
	@echo Done!

build_helper_sorting_proto:
	@echo generating code for helper sorting proto....
	chdir ..\helper-service\proto && python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. .\sorting.proto
	@echo Done!

build_seed:
	@echo craeting binary file for seed service...
	chdir ..\seed-service && set GOOS=linux&& set GOARCH=amd64&& set CGO_ENABLED=0 && go build -o ${SEED_BINARY} ./cmd/
	@echo Done!

docker_local_up_build: build_seed
	@echo Stopping docker images...
	docker-compose down
	@echo Building and starting docker images...
	docker-compose up --build -d
	@echo Docker images built and started!

docker_up_build:
	@echo Stopping docker images...
	docker-compose down
	@echo Building and starting docker images...
	docker-compose up --build -d
	@echo Docker images built and started!

#no need to download all packages every time we need to build docker image
docker_local_up: build_seed
	@echo Stopping docker images...
	docker-compose down
	@echo Starting docker images...
	docker-compose up -d
	@echo Docker images started!

docker_up:
	@echo Stopping docker images...
	docker-compose down
	@echo Starting docker images...
	docker-compose up -d
	@echo Docker images started!

docker_down:
	@echo Stopping docker images (if running...)
	docker-compose down




package api

import (
	"context"
	"log"
	"net/http"
	"seed/proto/sorting"
)

type Handler struct{}

func (socket *server) NewHandler() Handler {
	return Handler{}
}

const GRPC_ADDR = "helper-service:50001"

func (h *Handler) Sort(w http.ResponseWriter, r *http.Request) {
	socket, err := NewSocket(w, r)
	if err != nil {
		log.Panicln("socket connection error: ", err)
	}
	var sortingPayload *Sorting
	err = socket.Read(&sortingPayload)
	if checkIfErrNotNil(socket, err) {
		return
	}
	ctx, cancel := generateContex(3)
	defer cancel()
	conn, err := dialGRPC(ctx, GRPC_ADDR)
	if checkIfErrNotNil(socket, err) {
		return
	}
	defer conn.Close()
	grpcClient := sorting.NewSortingServiceClient(conn)
	stream, err := grpcClient.Sort(context.TODO(), generateSortingRequestProto(sortingPayload))
	if checkIfErrNotNil(socket, err) {
		return
	}
	done := make(chan bool)
	go readGRPCResponseAndWriteToSocket(done, stream, socket)

	<-done
	log.Printf("finished")

}

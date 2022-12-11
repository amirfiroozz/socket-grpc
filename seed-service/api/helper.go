package api

import (
	"context"
	"encoding/json"
	"io"
	"log"
	"seed/proto/sorting"
	"time"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func checkIfErrNotNil(s *socket, err error, status ...int) bool {
	if err != nil {
		b, _ := JSON(newSortingResponseWithErrorForSocketWrite(err))
		s.Write(b)
		return true
	}
	return false
}

func generateContex(timeout int) (context.Context, context.CancelFunc) {
	return context.WithTimeout(context.Background(), time.Duration(timeout)*time.Second)
}

func dialGRPC(ctx context.Context, addr string) (conn *grpc.ClientConn, err error) {
	return grpc.DialContext(ctx, addr, grpc.WithTransportCredentials(insecure.NewCredentials()), grpc.WithBlock())
}

func generateSortingRequestProto(sortingPayload *Sorting) *sorting.RequestSorting {
	return &sorting.RequestSorting{
		Type:      sortingPayload.Type,
		Array:     sortingPayload.Array,
		IsDone:    sortingPayload.IsDone,
		SleepTime: sortingPayload.SleepTime,
	}
}

func readGRPCResponseAndWriteToSocket(done chan bool, stream sorting.SortingService_SortClient, socket *socket) {
	for {
		resp, err := stream.Recv()
		if err == io.EOF {
			done <- true //close(done)
			return
		}
		if err != nil {
			log.Fatalf("can not receive %v\n", err)
			return
		}
		log.Printf("Resp received: %v\n", resp.Array)
		sortingResp := newSortingResponseFromGRPCSortingResponse(resp)
		b, err := JSON(sortingResp)
		if err != nil {
			log.Fatalf("failed building json %v\n", err)
		}
		err = socket.Write(b)
		if err != nil {
			return
		}
	}
}

func JSON(data any) ([]byte, error) {
	b, err := json.Marshal(data)
	if err != nil {
		return nil, err
	}
	return b, nil
}

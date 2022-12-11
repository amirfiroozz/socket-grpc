package api

import "seed/proto/sorting"

type Error struct {
	IsError bool   `json:"isError"`
	Message string `json:"message"`
}

type Sorting struct {
	Type      string  `json:"type"`
	Array     []int64 `json:"array"`
	IsDone    bool    `json:"isDone"`
	SleepTime float32 `json:"sleepTime"`
}
type SortingResponse struct {
	Array  []int64 `json:"array"`
	IsDone bool    `json:"isDone"`
	Left   int64   `json:"left"`
	Right  int64   `json:"right"`
	Error  *Error  `json:"error"`
}

func newSortingResponseFromGRPCSortingResponse(grpcSortingResp *sorting.ResponseSorting) SortingResponse {
	return SortingResponse{
		Array:  grpcSortingResp.GetArray(),
		IsDone: grpcSortingResp.GetIsDone(),
		Left:   grpcSortingResp.GetLeft(),
		Right:  grpcSortingResp.GetRight(),
		Error:  newError(grpcSortingResp.Error.GetMessage(), grpcSortingResp.Error.GetIsError()),
	}
}

func newSortingResponseWithErrorForSocketWrite(err error) SortingResponse {
	return SortingResponse{
		IsDone: false,
		Error:  newError(err.Error(), true),
	}
}

func newError(message string, isError bool) *Error {
	return &Error{
		Message: message,
		IsError: isError,
	}
}

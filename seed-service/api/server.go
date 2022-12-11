package api

import (
	"fmt"
	"log"
	"net/http"
)

type server struct{}

const (
	WEB_PORT = "8080"
)

func NewServer() server {
	return server{}
}

func (s *server) Start() error {
	srv := &http.Server{
		Addr:    fmt.Sprintf("[::]:%s", WEB_PORT),
		Handler: createRoutes(s.NewHandler()),
	}
	log.Printf("starting seed server on address %v\n", srv.Addr)
	err := srv.ListenAndServe()
	if err != nil {
		return err
	}
	return nil
}

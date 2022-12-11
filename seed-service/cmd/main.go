package main

import (
	"log"
	"seed/api"
)

func main() {
	server := api.NewServer()
	err := server.Start()
	if err != nil {
		log.Panicln("seed server stoped: ", err)
	}
}

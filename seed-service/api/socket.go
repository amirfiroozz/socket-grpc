package api

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"

	"github.com/gorilla/websocket"
)

type socket struct {
	Conn *websocket.Conn
}

var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool {
		return true
	},
}

func NewSocket(w http.ResponseWriter, r *http.Request) (*socket, error) {
	ws, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println("web socket upgrade error: ", err)
		return nil, err
	}
	return &socket{Conn: ws}, nil
}

func (s *socket) Read(data any) error {
	fmt.Println("wating for new message")
	_, message, err := s.Conn.ReadMessage()
	if err != nil {
		fmt.Println("err: ", err.Error())
		if websocket.IsUnexpectedCloseError(err, websocket.CloseGoingAway, websocket.CloseAbnormalClosure) {
			log.Printf("error: %v", err)
			return err
		}
	}
	err = json.Unmarshal(message, data)
	if err != nil {
		fmt.Println(err)
		return err
	}
	return nil
}
func (s *socket) Write(data []byte) error {
	err := s.Conn.WriteMessage(websocket.TextMessage, data)
	if err != nil {
		log.Println("write:", err)
		return err
	}
	return nil
}

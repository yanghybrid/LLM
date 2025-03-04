package main

import (
	"fmt"
	"log"
	"net/http"
	"github.com/gin-gonic/gin"
	"github.com/gorilla/websocket"
)

// WebSocket Upgrader
var upgrader = websocket.Upgrader{
	CheckOrigin: func(r *http.Request) bool { return true },
}

func wsHandler(c *gin.Context) {
	conn, err := upgrader.Upgrade(c.Writer, c.Request, nil)
	if err != nil {
		log.Println("WebSocket Upgrade failed:", err)
		return
	}
	defer conn.Close()

	for {
		messageType, msg, err := conn.ReadMessage()
		if err != nil {
			log.Println("WebSocket Error:", err)
			break
		}
		fmt.Println("Received:", string(msg))
		conn.WriteMessage(messageType, []byte("Acknowledged: "+string(msg)))
	}
}

func main() {
	router := gin.Default()
	router.GET("/ws", wsHandler)
	log.Println("Server running on :8080")
	router.Run(":8080")
}


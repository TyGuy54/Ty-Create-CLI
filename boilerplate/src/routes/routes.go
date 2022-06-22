package routes

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// write your routes here
func Routes(router *gin.Engine) {
	router.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "demo.html", gin.H{
			"title": "Home Page",
		})
	})
}

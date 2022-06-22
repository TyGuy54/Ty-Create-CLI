package main

import (
	config "ty-create/src/config"
	routes "ty-create/src/routes"

	"github.com/gin-gonic/gin"
)

var router *gin.Engine

// application starts here
func main() {
	config.Config()

	router := gin.Default()
	router.LoadHTMLGlob("public/staticPages/*.html")

	routes.Routes(router)

	router.Run()

}

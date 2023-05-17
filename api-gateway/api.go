package main
import (
	"fmt"

	"time"

	//"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	router.GET("/test", getTest)

	t := time.Now().Unix()
	fmt.Println(t)

	router.Run("localhost:8080")
}

// GET posts from scraper
func getDailyScrapedPosts(c *gin.Context) {
	fmt.Println("test")
	// Make call to cloudflare endpoint
	// massage data
	// post to SA api
	// push daily data up to DB
}

func getTest(c *gin.Context) {
	fmt.Println("test")
}
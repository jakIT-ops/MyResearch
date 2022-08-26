package main

import "github.com/gofiber/fiber"

func welcome(c *fiber.Ctx) error {
	return c.SendString("Welcome to my awesome API")
}

func main() {
	app := fiber.New()

	app.Get("/api", welcome)
}

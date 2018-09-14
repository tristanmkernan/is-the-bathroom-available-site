# Is the Bathroom Available?

For the truly lazy, or otherwise inconvenienced.

## Motivation

There is only one bathroom in my apartment. Due to the layout, it is impossible to predict the occupancy of the restroom without approaching it. This is annoying and demands a hi-tech solution!

## How

A spare Android phone running the [Is the Bathroom Available? app](). This app is programmed to watch for changes to the ambient light and send updates to this backend server.

When the ambient light is high (based on some pre-defined threshold), the bathroom is occupied and unavailable. Otherwise, the bathroom is probably unoccupied and probably available.

## Setup

1. Set a good password in `app.config`.
2. Build the application: `$ docker-compose build`
3. Let mysql perform its first-run initialization: `$ docker-compose up db`
4. When it's done, about a minute later, kill it with `Control-c`
5. Run the full application: `$ docker-compose up`

Use the typical `docker-compose` commands to run in the background.

## Changelog

### V0.1

- Display current bathroom availability.

## License

GPL-3.0

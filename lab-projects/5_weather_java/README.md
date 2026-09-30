# Weather App (Java + OpenWeatherMap)

Console app that shows the current weather of any city using the OpenWeatherMap API.

## Setup
1. Create a free account at https://openweathermap.org and copy your API key.
2. Java 11 or higher is required.

## Compile & Run
```bash
javac Weather.java

# Linux / Mac
export OPENWEATHER_API_KEY=your_key_here
java Weather Jaipur

# Windows (PowerShell)
$env:OPENWEATHER_API_KEY="your_key_here"
java Weather Jaipur
```

New API keys can take a little while to activate. Never commit your key to GitHub.

import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/** Fetches current weather for a city from the OpenWeatherMap API. */
public class Weather {

    static String find(String json, String regex) {
        Matcher m = Pattern.compile(regex).matcher(json);
        return m.find() ? m.group(1) : "N/A";
    }

    public static void main(String[] args) throws Exception {
        String apiKey = System.getenv("OPENWEATHER_API_KEY");
        if (apiKey == null || apiKey.isEmpty()) {
            System.out.println("Set your key first: OPENWEATHER_API_KEY=<your key>");
            return;
        }
        String city = args.length > 0 ? String.join(" ", args) : "Jaipur";

        String url = "https://api.openweathermap.org/data/2.5/weather?q="
                + URLEncoder.encode(city, StandardCharsets.UTF_8)
                + "&units=metric&appid=" + apiKey;

        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> res = client.send(
                HttpRequest.newBuilder(URI.create(url)).GET().build(),
                HttpResponse.BodyHandlers.ofString());

        if (res.statusCode() != 200) {
            System.out.println("Error " + res.statusCode() + ": " + res.body());
            return;
        }

        String json = res.body();
        System.out.println("City        : " + find(json, "\"name\":\"([^\"]+)\""));
        System.out.println("Weather     : " + find(json, "\"description\":\"([^\"]+)\""));
        System.out.println("Temperature : " + find(json, "\"temp\":([-0-9.]+)") + " °C");
        System.out.println("Feels like  : " + find(json, "\"feels_like\":([-0-9.]+)") + " °C");
        System.out.println("Humidity    : " + find(json, "\"humidity\":([0-9]+)") + " %");
        System.out.println("Wind speed  : " + find(json, "\"speed\":([0-9.]+)") + " m/s");
    }
}

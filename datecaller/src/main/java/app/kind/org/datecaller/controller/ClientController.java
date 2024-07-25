package app.kind.org.datecaller.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.reactive.function.client.WebClient;

@RestController
public class ClientController {

    private final WebClient webClient;

    public ClientController(WebClient.Builder webClientBuilder) {
        this.webClient = webClientBuilder.baseUrl("http://dateresponder.app.kind.org:31080").build();
    }

    @GetMapping("/fetch-date")
    public String fetchDate() {
        return webClient.get()
                .uri("/current-date")
                .retrieve()
                .bodyToMono(String.class)
                .block();
    }
}

package sec.hellolist;

import fi.helsinki.cs.tmc.edutestutils.Points;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import static org.assertj.core.api.Assertions.assertThat;
import org.fluentlenium.adapter.FluentTest;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;
import org.springframework.boot.context.embedded.LocalServerPort;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@Points("5")
public class HelloListTest extends FluentTest {

    public WebDriver webDriver = new HtmlUnitDriver();

    @Override
    public WebDriver getDefaultDriver() {
        return webDriver;
    }

    @LocalServerPort
    private Integer port;

    @Test
    public void contentFromFormAddedToList() {
        List<String> shouldNotContainItems = new ArrayList<>();
        Collections.addAll(shouldNotContainItems, "Abracadabra", "Alakazam", "Bibbidi-Bobbidi-Boo", "By the Power of Grayskull, I HAVE THE POWER", "Open sesame", "Shazam", "sudo get me a sandwich");

        List<String> shouldContainItems = new ArrayList<>();

        while (!shouldNotContainItems.isEmpty()) {
            goTo("http://localhost:" + port + "/");
            shouldNotContainItems.stream().forEach(s -> assertThat(pageSource()).doesNotContain(s));

            String content = shouldNotContainItems.get(0);
            shouldNotContainItems.remove(0);
            shouldContainItems.add(content);

            fill("input[type=text]").with(content);
            click("input[type=submit]");

            shouldContainItems.stream().forEach(s -> assertThat(find("li").getTexts().contains(s)));
        }
    }
}

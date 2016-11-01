package sec.hellotemplates;

import fi.helsinki.cs.tmc.edutestutils.Points;
import org.fluentlenium.adapter.FluentTest;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.htmlunit.HtmlUnitDriver;
import org.springframework.boot.context.embedded.LocalServerPort;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.context.SpringBootTest.WebEnvironment;
import org.springframework.test.context.junit4.SpringRunner;
import static org.assertj.core.api.Assertions.assertThat;

@RunWith(SpringRunner.class)
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
@Points("4")
public class HelloTemplatesTest extends FluentTest {

    public WebDriver webDriver = new HtmlUnitDriver();

    @Override
    public WebDriver getDefaultDriver() {
        return webDriver;
    }

    @LocalServerPort
    private Integer port;

    @Test
    public void indexShownAtRoot() {
        goTo("http://localhost:" + port + "/");
        assertThat(pageSource()).contains("Hello Thymeleaf");
        assertThat(pageSource()).doesNotContain("dQw4w9WgXcQ");
    }

    @Test
    public void videoShownAtVideo() {
        goTo("http://localhost:" + port + "/video");
        assertThat(pageSource()).contains("dQw4w9WgXcQ");
        assertThat(pageSource()).doesNotContain("Hello Thymeleaf");
    }

    @Test
    public void linkFromRootLeadsToVideo() {
        goTo("http://localhost:" + port + "/");
        find("a").click();
        assertThat(pageSource()).contains("dQw4w9WgXcQ");
    }
}

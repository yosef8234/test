package sec.hellolist;

import java.util.ArrayList;
import java.util.List;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class HelloListController {

    private List<String> list;

    public HelloListController() {
        this.list = new ArrayList<>();
        this.list.add("Hello world!");
    }

    @RequestMapping("/")
    public String home(Model model, @RequestParam(required = false) String content) {
        if (content != null && !content.trim().isEmpty()) {
            this.list.add(content.trim());
        }

        model.addAttribute("list", list);
        return "index";
    }

}

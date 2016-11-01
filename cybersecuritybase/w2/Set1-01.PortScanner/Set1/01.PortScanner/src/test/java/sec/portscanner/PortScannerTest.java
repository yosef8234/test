package sec.portscanner;

import fi.helsinki.cs.tmc.edutestutils.Points;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Set;
import static org.junit.Assert.assertTrue;
import org.junit.Test;

@Points("1")
public class PortScannerTest {

    @Test
    public void testPortScanner() throws Throwable {
        Random rnd = new Random();
        List<Integer> randomPorts = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            randomPorts.add(rnd.nextInt(20000) + 10000);
        }

        for (Integer randomPort : randomPorts) {
            Server s = new Server(randomPort);
            Thread serverThread = new Thread(s);
            serverThread.start();

            while (!serverThread.isAlive()) {
                Thread.sleep(100);
            }

            Set<Integer> ports = PortScanner.getAccessiblePorts("localhost", randomPort - rnd.nextInt(5), randomPort + rnd.nextInt(5));
            assertTrue(ports.size() == 1);
            assertTrue(ports.contains(randomPort));

            serverThread.interrupt();
        }
    }
}

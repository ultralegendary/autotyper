import java.awt.Robot;
import java.awt.AWTException;
import java.awt.event.KeyEvent;

public class AutoTyper {
    private static volatile boolean typing = true;
    private static Thread typingThread;
    private static volatile boolean stopTyping = false;

    public static void main(String[] args)throws AWTException {
        System.out.println("Auto Clicker activated.");
        Robot robot;
        try {
            robot = new Robot();
        } catch (AWTException e) {
            System.err.println("Failed to create Robot: " + e.getMessage());
            return;
        }

        while (true) {
            // System.out.print("E");

            if (typing && !stopTyping) {
                startTyping(robot);
            }

            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    private static void startTyping(Robot robot)throws AWTException {
        System.out.println("Start typing...");
        String wordsToType = "isworking";

        for (char c : wordsToType.toCharArray()) {
            robot.delay(100);
            robot.keyPress(KeyEvent.getExtendedKeyCodeForChar(c));
            robot.keyRelease(KeyEvent.getExtendedKeyCodeForChar(c));
        }
    }

//    shiniisworkingsubashiniiswork
}

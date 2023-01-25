import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Shell {

    public static void executeCmd(String cmd) throws IOException {

        Process process = Runtime.getRuntime().exec(cmd);

        printCmdOutput(process);
        printCmdErrors(process);

    }

    static private void printCmdOutput(Process process) throws IOException {
        BufferedReader stdInput = new BufferedReader(new
                InputStreamReader(process.getInputStream()));
        // Read the output from the command
        String s;

        System.out.println("\033[0;33m");
        while ((s = stdInput.readLine()) != null) {
            System.out.println("[Shell OUTPUT] : " + s);
        }
        System.out.println("\033[0m");
    }

    static private void printCmdErrors(Process process) throws IOException {
        String s;
        BufferedReader stdError = new BufferedReader(new
                InputStreamReader(process.getErrorStream()));

        System.out.println("\033[0;31m\n");
        // Read any errors from the attempted command
        System.out.println("Here is the standard error of the command (if any):\n");
        while ((s = stdError.readLine()) != null) {
            System.out.println("[Shell ERROR] : " + s);
        }
        System.out.println("\033[0m");
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Shell {

    public static List<String> executeCmd(String cmd) throws IOException {

        Process process = Runtime.getRuntime().exec(cleanCmd(cmd));
        System.out.println(cleanCmd(cmd));
        List<String> output = printCmdOutput(process);
        printCmdErrors(process);
        return output;
    }

    static private String cleanCmd(String cmd) {
        return cmd.replace("\\", ".");
    }

    static private List<String> printCmdOutput(Process process) throws IOException {
        BufferedReader stdInput = new BufferedReader(new
                InputStreamReader(process.getInputStream()));
        // Read the output from the command
        String s;

        System.out.println("\033[0;33m");
        List<String> output = new ArrayList<>();
        while ((s = stdInput.readLine()) != null) {
            System.out.println("[Shell OUTPUT] : " + s);
            output.add(s);
        }
        System.out.println("\033[0m");
        return output;
    }

    static private void printCmdErrors(Process process) throws IOException {
        String s;
        BufferedReader stdError = new BufferedReader(new
                InputStreamReader(process.getErrorStream()));

        System.out.println("\033[0;31m\n");
        List<String> output = new ArrayList<>();
        // Read any errors from the attempted command
        while ((s = stdError.readLine()) != null) {
            System.out.println("[Shell ERROR] : " + s);
        }
        System.out.println("\033[0m");
    }
}

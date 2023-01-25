import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Random;

/**
 * @author couedrao on 27/11/2019.
 * @project gctrl
 */
class MANOAPI {

    void deploy_monitoring_vnf() {
        String command = "curl -s -X PUT http://127.0.0.1:5001/restapi/compute/dc1/mntr-vnf -H 'Content-Type: application/json' -d '{\"image\":\"vnf:latest\", \"network\":\"(id=vnf-eth0,ip=10.0.0.21/24, port=5001)\"}'";
        try {
            Shell.executeCmd(command);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    String deploy_gw(Map<String, String> vnfinfos) {
        String ip = "192.168.0." + (new Random().nextInt(253) + 1);
        Main.logger(this.getClass().getSimpleName(), "Deploying VNF ...");

        //printing
        for (Entry<String, String> e : vnfinfos.entrySet()) {
            Main.logger(this.getClass().getSimpleName(), "\t" + e.getKey() + " : " + e.getValue());
        }
        //TODO

        return ip;
    }

    List<String> deploy_multi_gws_and_lb(List<Map<String, String>> vnfsinfos) {
        List<String> ips = new ArrayList<>();
        //TODO

        for (Map<String, String> vnfsinfo : vnfsinfos) {
            ips.add(deploy_gw(vnfsinfo));
        }

        return ips;
    }
}

import logging
from mininet.log import setLogLevel
from emuvim.dcemulator.net import DCNetwork
from emuvim.api.rest.rest_api_endpoint import RestApiEndpoint
from emuvim.api.openstack.openstack_api_endpoint import OpenstackApiEndpoint

logging.basicConfig(level=logging.INFO)
setLogLevel('info')  # set Mininet loglevel
logging.getLogger('werkzeug').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.base').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.compute').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.keystone').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.nova').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.neutron').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.heat').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.heat.parser').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.glance').setLevel(logging.DEBUG)
logging.getLogger('api.openstack.helper').setLevel(logging.DEBUG)


def create_topology():
    net = DCNetwork(monitor=False, enable_learning=True)

    dc1 = net.addDatacenter("dc1")
    # add OpenStack-like APIs to the emulated DC
    api1 = OpenstackApiEndpoint("0.0.0.0", 6001)
    api1.connect_datacenter(dc1)
    api1.start()
    api1.connect_dc_network(net)
    # add the command line interface endpoint to the emulated DC (REST API)
    rapi1 = RestApiEndpoint("0.0.0.0", 5001)
    rapi1.connectDCNetwork(net)
    rapi1.connectDatacenter(dc1)
    rapi1.start()

    srv = net.addDocker('srv', dimage='kyriios188/node_server:latest', ip='10.0.0.1', mem_limit="512m", environment={'CONTAINER_TYPE': 'srv'})
    gwi = net.addDocker('gwi', dimage='kyriios188/node_server:latest', ip='10.0.0.2', mem_limit="512m", environment={'CONTAINER_TYPE': 'gwi'})
    gwf1 = net.addDocker('gwf1', dimage='kyriios188/node_server:latest', ip='10.0.0.3', mem_limit="512m", environment={'CONTAINER_TYPE': 'gwf1'})
    gwf2 = net.addDocker('gwf2', dimage='kyriios188/node_server:latest', ip='10.0.0.4', mem_limit="512m", environment={'CONTAINER_TYPE': 'gwf2'})
    gwf3 = net.addDocker('gwf3', dimage='kyriios188/node_server:latest', ip='10.0.0.5', mem_limit="512m", environment={'CONTAINER_TYPE': 'gwf3'})
    dev1 = net.addDocker('dev1', dimage='kyriios188/node_server:latest', ip='10.0.0.6', mem_limit="512m", environment={'CONTAINER_TYPE': 'dev1'})
    dev2 = net.addDocker('dev2', dimage='kyriios188/node_server:latest', ip='10.0.0.7', mem_limit="512m", environment={'CONTAINER_TYPE': 'dev2'})
    dev3 = net.addDocker('dev3', dimage='kyriios188/node_server:latest', ip='10.0.0.8', mem_limit="512m", environment={'CONTAINER_TYPE': 'dev3'})
    app = net.addDocker('app', dimage='kyriios188/node_server:latest', ip='10.0.0.9', mem_limit="512m", environment={'CONTAINER_TYPE': 'app'})

    f_switch1 = net.addSwitch('s1')
    f_switch2 = net.addSwitch('s2')
    f_switch3 = net.addSwitch('s3')
    gwi_switch = net.addSwitch('s4')
    srv_switch = net.addSwitch('s5')

    net.addLink(dev1, f_switch1)
    net.addLink(gwf1, f_switch1)
    net.addLink(dev2, f_switch2)
    net.addLink(gwf2, f_switch2)
    net.addLink(dev3, f_switch3)
    net.addLink(gwf3, f_switch3)

    net.addLink(gwi_switch, f_switch1)
    net.addLink(gwi_switch, f_switch2)
    net.addLink(gwi_switch, f_switch3)
    net.addLink(gwi_switch, gwi)
    net.addLink(gwi_switch, dc1)
    net.addLink(gwi_switch, srv_switch)

    net.addLink(srv_switch, srv)
    net.addLink(srv_switch, app)

    net.start()
    net.CLI()
    # when the user types exit in the CLI, we stop the emulator
    net.stop()


def main():
    create_topology()


if __name__ == '__main__':
    main()

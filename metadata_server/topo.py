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

    srv = net.addDocker('srv', dimage='ubuntu:trusty', mem_limit="512m", environment={'CONTAINER_TYPE': 'srv'})
    app = net.addDocker('app', dimage='ubuntu:trusty', mem_limit="512m", environment={'CONTAINER_TYPE': 'app'})
    gwi = net.addDocker('gwi', dimage='ubuntu:trusty', mem_limit="512m", environment={'CONTAINER_TYPE': 'gwi'})
    gwf1 = net.addDocker('gwf1', dimage='ubuntu:trusty', mem_limit="512m", environment={'CONTAINER_TYPE': 'gwf1'})
    gwf2 = net.addDocker('gwf2', dimage='ubuntu:trusty', mem_limit="512m", environment={'CONTAINER_TYPE': 'gwf2'})
    gwf3 = net.addDocker('gwf3', dimage='ubuntu:trusty', mem_limit="512m", environment={'CONTAINER_TYPE': 'gwf3'})
    dev1 = net.addDocker('dev1', dimage='ubuntu:trusty', mem_limit="512m", environment={'CONTAINER_TYPE': 'dev1'})
    dev2 = net.addDocker('dev2', dimage='ubuntu:trusty', mem_limit="512m", environment={'CONTAINER_TYPE': 'dev2'})
    dev3 = net.addDocker('dev3', dimage='ubuntu:trusty', mem_limit="512m", environment={'CONTAINER_TYPE': 'dev3'})

    gwf_switch = net.addSwitch('gwf_switch')
    out_switch = net.addSwitch('out_switch')
    gwi_switch = net.addSwitch('gwi_switch')
    srv_switch = net.addSwitch('srv_switch')

    net.addLink(dev1, gwf1)
    net.addLink(dev2, gwf2)
    net.addLink(dev3, gwf3)

    net.addLink(gwi_switch, gwf_switch)
    net.addLink(gwi_switch, out_switch)
    net.addLink(gwf_switch, out_switch)

    net.addLink(dc1, out_switch)

    net.addLink(gwi, gwi_switch)
    net.addLink(gwi, srv_switch)
    net.addLink(srv, srv_switch)
    net.addLink(srv, app)

    net.start()
    net.CLI()
    # when the user types exit in the CLI, we stop the emulator
    net.stop()


def main():
    create_topology()


if __name__ == '__main__':
    main()

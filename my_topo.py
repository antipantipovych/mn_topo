from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.link import TCLink, Intf

def topology():
	net = Mininet(controller = Controller, link = TCLink, switch = OVSKernelSwitch)
	s2 = net.addSwitch('s2')
	h1 = net.addHost('h1', ip = "10.0.1.1")
	h2 = net.addHost('h2', ip = "10.0.1.2")
	h3 = net.addHost('h3', ip = "10.0.1.3")
	h4 = net.addHost('h4', ip = "10.0.1.4")
	h5 = net.addHost('h5', ip = "10.0.1.5")
	c0 = net.addController('c0', controller = RemoteController, ip = '172.25.1.9', port = 6633)
	net.addLink(h1,s2)
	net.addLink(h2,s2)
	net.addLink(h3,s2)
	net.addLink(h4,s2)
	net.addLink(h5,s2)
	c0.start()
	s2.start([c0])
	s2.cmd("ip link add s2-gre1 type gretap local 172.25.1.8 remote 172.25.1.4 ttl 64")
	s2.cmd("ip link set s2-gre1 up")
	Intf("s2-gre1", node = s2)
	
	net.start()
	CLI(net)
	s2.cmd("ip link del dev s2-gre1")
	net.stop()

if __name__ == '__main__':
	topology()
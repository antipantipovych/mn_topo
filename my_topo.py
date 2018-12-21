from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.link import TCLink, Intf

def topology():
	net = Mininet(controller = Controller, link = TCLink, switch = OVSKernelSwitch)
	s2 = net.addSwitch('s2')
	s1 = net.addSwitch('s1')
	h1 = net.addHost('h1', ip = "10.0.1.1")
	h2 = net.addHost('h1', ip = "10.0.1.2")
	c0 = net.addController('c0')
	net.addLink(h1,s1)
	net.addLink(h2,s2)
	net.addLink(s1,s2)
	c0.start()
	s2.start([c0])
	net.start()
	CLI(net)
	net.stop()

if __name__ == '__main__':
	topology()
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        r1 = self.addSwitch("r1")
        r2 = self.addSwitch("r2")
        r3 = self.addSwitch("r3")
        r4 = self.addSwitch("r4")
        h1 = self.addHost("h1")

        self.addLink(r1, r2)
        self.addLink(r1, r3)
        self.addLink(r1, r4)
        self.addLink(r1, h1)

topos = { 'mytopo': ( lambda: MyTopo() ) }
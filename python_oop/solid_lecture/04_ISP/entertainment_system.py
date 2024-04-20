class EntertainmentDevice:
    def power_outlet_connect(self, device):
        pass


class ConnectRCA():

    def rca_cable_connect(self, obj):
        pass


class ConnectHDMI():

    def hdmi_cable_connect(self, obj):
        pass

class ConnectEthernet():

    def ethernet_cable_connect(self, obj):
        pass




class Television(EntertainmentDevice, ConnectRCA, ConnectHDMI):
    def connect_to_dvd(self, dvd_player):
        super().rca_cable_connect(dvd_player)

    def connect_to_game_console(self, game_console):
        super().hdmi_cable_connect(game_console)

    def plug_in_power(self, ):
        self.power_outlet_connect(self)


class DVDPlayer(EntertainmentDevice, ConnectHDMI):
    def connect_to_tv(self, television):
        super().hdmi_cable_connect(television)

    def plug_in_power(self):
        self.power_outlet_connect(self)


class GameConsole(EntertainmentDevice, ConnectHDMI, ConnectEthernet):
    def connect_to_tv(self, television):
        super().hdmi_cable_connect(television)

    def connect_to_router(self, router):
        super().ethernet_cable_connect(router)

    def plug_in_power(self):
        self.power_outlet_connect(self)


class Router(EntertainmentDevice, ConnectEthernet):
    def connect_to_tv(self, television):
        super().ethernet_cable_connect(television)

    def connect_to_game_console(self, game_console):
        super().ethernet_cable_connect(game_console)

    def plug_in_power(self):
        self.power_outlet_connect(self)

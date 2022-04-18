"""We have been hired to create a game where the player sets up entertainment systems.
 Each piece of the system (television, game console, etc.) uses a specific cable to connect to another
  device. The TV uses an HDMI cable to connect to a game console. Both the game console and TV connect
to a router via an ethernet cable to access the internet. And lastly, all the devices are connected
to the wall via a power cable so they can turn on. Your job is to extend this behavior in the device classes."""
from abc import  ABC,abstractmethod

class Connection_way(ABC):
    __WAY= "START"

    @abstractmethod
    def connect_to(self,device):
        return  self.__WAY



class connect_to_device_via_hdmi_cable(Connection_way):
    __WAY = "HDMI"





class connect_to_device_via_rca_cable(Connection_way):
    __WAY = "RCA"

class connect_to_device_via_ethernet_cable(Connection_way):
    __WAY = "ETHERNET"


class connect_device_to_power_outlet(Connection_way):
    __WAY = "220V"


class EntertainmentDevice:
    def plug_in_power(self):
        return "Connected to 220 V"

    # def connect_to_device_via_hdmi_cable(self, device):
    #     pass
    # def connect_to_device_via_rca_cable(self, device):
    #     pass
    # def connect_to_device_via_ethernet_cable(self, device):
    #     pass
    # def connect_device_to_power_outlet(self, device):
    #     pass


class Television(EntertainmentDevice,
                 connect_to_device_via_rca_cable,connect_to_device_via_hdmi_cable,connect_device_to_power_outlet):

    def connect_to_dvd(self, dvd_player):
        return connect_to_device_via_hdmi_cable.connect_to(dvd_player)

    def connect_to_game_console(self, game_console):
        return connect_to_device_via_hdmi_cable.connect_to(game_console)

    def plug_in_power(self):
        return connect_device_to_power_outlet.connect_to(self)


class DVDPlayer(EntertainmentDevice,connect_to_device_via_hdmi_cable):
    def connect_to_tv(self, television):
        a= connect_to_device_via_hdmi_cable.connect_to(television)
        return f"{self.__class__.__name__} are connected via {a} to {television}"



class GameConsole(EntertainmentDevice,connect_to_device_via_hdmi_cable,connect_to_device_via_ethernet_cable):
    def connect_to_tv(self, television):
        return connect_to_device_via_hdmi_cable.connect_to(television)

    def connect_to_router(self, router):
        return connect_to_device_via_ethernet_cable.connect_to(router)




class Router(EntertainmentDevice,connect_to_device_via_ethernet_cable):
    def connect_to_tv(self, television):
        return connect_to_device_via_ethernet_cable.connect_to(television)

    def connect_to_game_console(self, game_console):
        return connect_to_device_via_ethernet_cable.connect_to(game_console)




dvd=DVDPlayer()
print(dvd.connect_to_tv("DD"))
print(dvd.plug_in_power())

class Televison:

    def __init__(self):
        self._channel = 1
        self._volume = 40

    @property
    def current_channel(self):
        return self._channel

    @current_channel.setter
    def current_channel(self, channel):
        self._channel = channel

    @property
    def current_volume(self):
        return self._volume

    @current_volume.setter
    def current_volume(self, volume):
        self._volume = volume

    def increase_volume(self, quant):
        if self.current_volume + quant <= 100:
            self.current_volume += quant
            print(f"Done, actual volume is {self.current_volume}")
        else:
            print(f"Limit volume is 100, actual is {self.current_volume}")

    def decrease_volume(self, quant):
        if self.current_volume - quant >= 0:
            self.current_volume -= quant
            print(f"Done, actual volume is {self.current_volume}")
        else:
            print(f"Limit volume is 100, actual is {self.current_volume}")

    def increase_channel(self, quant):
        self.current_channel += quant
        print(f"Done, actual channel is {self.current_channel}")

    def decrease_channel(self, quant):
        if self.current_channel - quant > 0:
            self.current_channel -= quant
            print(f"Done, current channel is {self.current_channel}")
        else:
            print(
                f"Impossible, actual channel is {self.current_channel} and you're trying to decrease {quant} channels")

    def change_channel(self, channel):
        if channel > 0:
            self.current_channel = channel
            print(f"Done, actual channel is {self.current_channel}")
        else:
            print(f"Impossible to reach the {channel}º channel")

    def check_info(self):
        print(
            f"Actual volume is {self.current_volume} and channel is {self.current_channel}")


class RemoteControl:

    def __init__(self):
        pass

    def increase_one_volume(self, tv):
        tv.increase_volume(1)

    def decrease_one_volume(self, tv):
        tv.decrease_volume(1)

    def increase_one_channel(self, tv):
        tv.increase_channel(1)

    def decrease_one_channel(self, tv):
        tv.decrease_channel(1)

    def goto_channel(self, tv, channel):
        tv.change_channel(channel)

    def check_info(self, tv):
        tv.check_info()


tv1 = Televison()
rc1 = RemoteControl()
while True:
    try:
        op = int(input("Select a option:\n1 - Increase 1 volume\n2 - Decrease 1 volume\n3 - Increase 1 channel\n4 - Decrease 1 channel\n5 - Go to a channel\n6 - Check channel and volume\n"))
        if op == 1:
            rc1.increase_one_volume(tv1)
        elif op == 2:
            rc1.decrease_one_volume(tv1)
        elif op == 3:
            rc1.increase_one_channel(tv1)
        elif op == 4:
            rc1.decrease_one_channel(tv1)
        elif op == 5:
            channel = int(input("Input the channel: "))
            rc1.goto_channel(tv1, channel)
        elif op == 6:
            rc1.check_info(tv1)
    except ValueError as e:
        print(f"Input should be integer - {e}")

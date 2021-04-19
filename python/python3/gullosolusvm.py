#!/usr/bin/python3
import requests


class solusVM_Client():
    def init(self):
        self.apiurl = "solusvm.gullo.me"
        self.apikey = "NQ9RU-H4ET0-AL9NO"
        self.apihash = "f1666148fc00fba83bf327eaf4af58f04eaea6e9"
        self.tgbot = "1653363243:AAHx5w1nkyMto_f5G5pjPMNOoajeJdr1atI"
        self.tgchat = "1054232996"
        self.node = "Nat-Fin-Gullo-01"

    def sQuery(self, values):
        values.update({'rdtype': 'json', 'hash': self.apihash, 'key': self.apikey})
        response = requests.get(
            'https://'+self.apiurl+':5656/api/client/command.php', params=values, timeout=10)
        return response.text

    def get_status(self):
        return self.sQuery({'action': 'status'})

    def get_info(self):
        return self.sQuery({'action': 'info', 'ipaddr': 'true', 'hdd': 'true', 'mem': 'true', 'bw': 'true'})

    def shutdown(self):
        return self.sQuery({'action': 'shutdown'})

    def boot(self):
        return self.sQuery({'action': 'boot'})

    def reboot(self):
        return self.sQuery({'action': 'reboot'})

    def telegram(self, text):
        values = {'chat_id': self.tgchat, 'text': '§'+self.node+'§ '+text}
        response = requests.get(
            'https://api.telegram.org/bot'+self.tgbot+'/sendMessage?parse_mode=HTML', params=values, timeout=10)
        return response.text


if __name__ == "__main__":
    svmc = solusVM_Client()
    status = svmc.get_status()
    print(status)
    if "online" not in status:
        print("已离线，正在启动")
        svmc.boot()
        svmc.telegram("已离线，已重新启动")
    else:
        print("在线")
        svmc.telegram("在线")

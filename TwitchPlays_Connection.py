import socket, sys, re
class Twitch:
    user = "";
    oauth = "";
    s = None;
    def twitch_login_status(self, data):
        if not re.match(b'^:(testserver\.local|tmi\.twitch\.tv) NOTICE \* :Login unsuccessful\r\n$', data): return True
        else: return False
    def twitch_connect(self, user, key):
        self.user = user;
        self.oauth= key;
        print("Connecting to twitch.tv");
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        s.settimeout(0.9);
        connect_host = "irc.twitch.tv";
        connect_port = 6667;
        try:
            s.connect((connect_host, connect_port));
        except:
            print("Failed to connect to twitch");
            sys.exit();
        print("Connected to twitch");
        print("Sending our details to twitch...");
        s.send(b'USER %s\r\n' % user.encode());
        s.send(b'PASS %s\r\n' % key.encode());
        s.send(b'NICK %s\r\n' % user.encode());
        if not self.twitch_login_status(s.recv(256)):
            print("... and they didn't accept our details");
            sys.exit();
        else:
            print("... they accepted our details");
            print("Connected to twitch.tv!")
            self.s = s;
            s.send(b'JOIN #%s\r\n' % user.encode())
            s.recv(256);
    def check_has_message(self, data):
        return re.match(b'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) PRIVMSG #[a-zA-Z0-9_]+ :.+$', data)
    def parse_message(self, data):
        return {
            'channel': re.findall(b'^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ PRIVMSG (.*?) :', data)[0],
            'username': re.findall(b'^:([a-zA-Z0-9_]+)\!', data)[0],
            'message': re.findall(b'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)[0].decode('utf_8')
        }
    def twitch_recieve_messages(self, amount=256):
        data = None
        try: data = self.s.recv(256);
        except: return False;
        if not data:
            print("Lost connection to Twitch, attempting to reconnect...");
            self.twitch_connect(self.user, self.oauth);
            return None
        if self.check_has_message(data):
            return [self.parse_message(line) for line in [_f for _f in data.split(b'\r\n') if _f]];
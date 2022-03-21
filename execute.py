from mcrcon import MCRcon

def send_command(ip, password, command, port : int = 25575):
    with MCRcon(host = ip, port = port,password = password) as con:
        return con.command(command)
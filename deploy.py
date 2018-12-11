from fabric import Connection

HOST = '18.223.15.54'

con = Connection(HOST, user='ubuntu')

with con.cd('~/wallpapers/wallpapers/'):
    con.run('sudo docker-compose down')
    con.run('sudo git pull --rebase')
    con.run('sudo docker-compose up --build -d')


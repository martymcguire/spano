import os
from fabric import task

branch = os.environ['CIRCLE_BRANCH']
port = 5050
volume = 'mp-root'
image = f'desmondrivet/spano:{branch}'
name = 'spano'

@task(hosts=["dcr@spano.desmondrivet.com"])
def deploy(c):
    c.run(f'docker pull {image}')
    c.run(f'docker stop {name}', warn=True)
    c.run(f'docker run --name {name} ' +
          f'-p {port}:5000 ' +
          f'-v {volume}:/data --rm -d {image}')

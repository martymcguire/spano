from invoke import task


@task
def run(c):
    c.run('python run.py')


@task
def dbuild(c):
    c.run('docker image build -t ' +
          'desmondrivet/spano:$CIRCLE_BRANCH .')


@task
def dlogin(c):
    c.run('echo "$DOCKER_PASS" | ' +
          'docker login --username $DOCKER_USER --password-stdin')


@task
def dpush(c):
    c.run('docker push desmondrivet/spano:$CIRCLE_BRANCH')

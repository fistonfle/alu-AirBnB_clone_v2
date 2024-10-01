from fabric import task
from fabric.connection import Connection
from invoke import run as local_run  # For local commands
from datetime import datetime
from os.path import exists, isdir

# Define the hosts and user details
env_hosts = ['54.242.122.123', '54.147.161.62']
user = 'ubuntu'

@task
def do_pack(c):
    """Generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local_run("mkdir versions")
        file_name = f"versions/web_static_{date}.tgz"
        local_run(f"tar -cvzf {file_name} web_static")
        print(f"Archive created: {file_name}")
        return file_name
    except Exception as e:
        print(f"Error in do_pack: {e}")
        return None

@task
def do_deploy(c, archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        print(f"Archive path does not exist: {archive_path}")
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        c.put(archive_path, '/tmp/')
        c.run(f'mkdir -p {path}{no_ext}/')
        c.run(f'tar -xzf /tmp/{file_n} -C {path}{no_ext}/')
        c.run(f'rm /tmp/{file_n}')
        c.run(f'mv {path}{no_ext}/web_static/* {path}{no_ext}/')
        c.run(f'rm -rf {path}{no_ext}/web_static')
        c.run(f'rm -rf /data/web_static/current')
        c.run(f'ln -s {path}{no_ext}/ /data/web_static/current')
        print(f"Deployed {file_n} to {path}{no_ext}/")
        return True
    except Exception as e:
        print(f"Error in do_deploy: {e}")
        return False

@task
def deploy(c):
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack(c)
    if not archive_path:
        print("do_pack failed")
        return False

    for host in env_hosts:
        conn = Connection(host=host, user=user, connect_kwargs={"key_filename": "~/.ssh/school"})
        if not do_deploy(conn, archive_path):
            print(f"Failed to deploy to {host}")
            return False
    print("Deployment complete")
    return True

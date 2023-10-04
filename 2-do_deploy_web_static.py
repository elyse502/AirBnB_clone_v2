#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
'''
fabric script to distribute an archive to web servers
----NEEDS TO REVISIT SCRIPT
'''

def do_deploy(archive_path):
    """deploy package to remote server
    Arguments:
        archive_path: path to archive to deploy
    """
    if not archive_path or not exists(archive_path):
        return False
    put(archive_path, '/tmp')
    ar_name = archive_path[archive_path.find("/") + 1: -4]
    try:
        run('mkdir -p /data/web_static/releases/{}/'.format(ar_name))
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/'.format(
                ar_name, ar_name
        ))
        run('rm /tmp/{}.tgz'.format(ar_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(
                ar_name, ar_name
        ))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(
            ar_name
        ))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(
            ar_name
        ))
        print("New version deployed!")
        return True
    except:
        return False

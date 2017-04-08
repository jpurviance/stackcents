import json
json_ = {'cpu': {'load_avg': {'10_min': 0.08, '1_min': 0.72, '5_min': 0.23}},
       'id': 'i-05020f6bf46efe6d9',
       'mem': {'active': 367558656,
               'available': 738959360,
               'buffers': 65253376,
               'cached': 799965184,
               'free': 67403776,
               'inactive': 447320064,
               'percent': 29.1,
               'shared': 5234688,
               'total': 1041674240,
               'used': 109051904},
       'meta': {'ami-manifest-path': '(unknown)', 'instance-type': 't2.micro', 'instance-id': 'i-05020f6bf46efe6d9',
                'local-hostname': 'ip-172-31-14-187.ec2.internal', 'network': {'interfaces': {'macs': {
               '02:6c:10:50:15:12': {'local-hostname': 'ip-172-31-14-187.ec2.internal',
                                     'security-groups': 'launch-wizard-1',
                                     'public-hostname': 'ec2-34-200-242-196.compute-1.amazonaws.com',
                                     'vpc-ipv4-cidr-blocks': '172.31.0.0/16', 'subnet-id': 'subnet-e2b3f287',
                                     'public-ipv4s': '34.200.242.196', 'interface-id': 'eni-16284e02',
                                     'mac': '02:6c:10:50:15:12', 'security-group-ids': 'sg-e8ee9197',
                                     'vpc-ipv4-cidr-block': '172.31.0.0/16', 'owner-id': '272636870845',
                                     'local-ipv4s': '172.31.14.187', 'subnet-ipv4-cidr-block': '172.31.0.0/20',
                                     'vpc-id': 'vpc-c6bb9ba0', 'device-number': '0',
                                     'ipv4-associations': {'34.200.242.196': '172.31.14.187'}}}}},
                'hostname': 'ip-172-31-14-187.ec2.internal', 'ami-id': 'ami-22ce4934', 'instance-action': 'none',
                'profile': 'default-hvm', 'reservation-id': 'r-0bb94836d41fb6638', 'security-groups': 'launch-wizard-1',
                'metrics': {'vhostmd': '<?xml version="1.0" encoding="UTF-8"?>'}, 'mac': '02:6c:10:50:15:12',
                'public-ipv4': '34.200.242.196', 'services': {'domain': 'amazonaws.com', 'partition': 'aws'},
                'num_cpu': {'num_cpu': 1}, 'local-ipv4': '172.31.14.187',
                'placement': {'availability-zone': 'us-east-1a'}, 'ami-launch-index': '0',
                'public-hostname': 'ec2-34-200-242-196.compute-1.amazonaws.com', 'public-keys': {'BUTCAMP': [
               'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDEgxL+HEgFVicLsVnrzuBNQXifMfx6sUnymYUvyQhG0t82EKOBOZnHRNK5/HClPkaLdf3tT7CAeMKu9NQMaoR1GqyiWRknrQ/eojL/AJOlK7eiBlif1T4BvgzE4ORczT/KR2XZKmY1IyIDDT2/2QNVicLvCJJ667DcfJjzHF5keJVhxWjnqokG4hzr13BTI9nJQjSVQR7P7F6weJj5Y8SWhI9L9WldQp6C+1eUNGyk6WKHLdby9Tk8if47YDTZCUdSu0KlDFD5N+Ga1F6m+n0x5O3NjmQgZiinpd1Yjpkf19fx0QtnXQnfoGQ6DHiq5raoMhGzOA4Gf8ao1SoMzthl BUTCAMP',
               '']}, 'block-device-mapping': {'ami': '/dev/xvda', 'root': '/dev/xvda'}},
         'network': {'bytes_recv': 261096068,
                   'bytes_sent': 88935245,
                   'dropin': 0,
                   'dropout': 0,
                   'errin': 0,
                   'errout': 0,
                   'packets_recv': 577942,
                   'packets_sent': 458073},
         'processes': {'mongod': {'cmdline': ['/usr/bin/mongod',
                                            '-f',
                                            '/etc/mongod.conf'],
                                'connections': None,
                                'cpu_affinity': [0],
                                'cpu_num': 0,
                                'cpu_percent': 0.0,
                                "memory_percent": 20.3,
                                "pid": 200,
                                "num_threads": 5,
                                'username': 'mongod'},
                     'python': {'cmdline': ['python', 'eventloop.py'],
                                'connections': [],
                                'cpu_affinity': [0],
                                'cpu_num': 0,
                                'cpu_percent': 0.0,
                                'create_time': 1491672773.37,
                                'cwd': '/home/ec2-user/glowing-meme',
                                'environ': {'AWS_AUTO_SCALING_HOME': '/opt/aws/apitools/as',
                                            'AWS_CLOUDWATCH_HOME': '/opt/aws/apitools/mon',
                                            'AWS_ELB_HOME': '/opt/aws/apitools/elb',
                                            'AWS_PATH': '/opt/aws',
                                            'EC2_AMITOOL_HOME': '/opt/aws/amitools/ec2',
                                            'EC2_HOME': '/opt/aws/apitools/ec2',
                                            'HISTCONTROL': 'ignoredups',
                                            'HISTSIZE': '1000',
                                            'HOME': '/home/ec2-user',
                                            'HOSTNAME': 'ip-172-31-14-187',
                                            'JAVA_HOME': '/usr/lib/jvm/jre',
                                            'LANG': 'en_US.UTF-8',
                                            'LESSOPEN': '||/usr/bin/lesspipe.sh %s',
                                            'LESS_TERMCAP_mb': '\x1b[01;31m',
                                            'LESS_TERMCAP_md': '\x1b[01;38;5;208m',
                                            'LESS_TERMCAP_me': '\x1b[0m',
                                            'LESS_TERMCAP_se': '\x1b[0m',
                                            'LESS_TERMCAP_ue': '\x1b[0m',
                                            'LESS_TERMCAP_us': '\x1b[04;38;5;111m',
                                            'LOGNAME': 'ec2-user',
                                            'LS_COLORS': 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=01;05;37;41:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=01;36:*.au=01;36:*.flac=01;36:*.mid=01;36:*.midi=01;36:*.mka=01;36:*.mp3=01;36:*.mpc=01;36:*.ogg=01;36:*.ra=01;36:*.wav=01;36:*.axa=01;36:*.oga=01;36:*.spx=01;36:*.xspf=01;36:',
                                            'MAIL': '/var/spool/mail/ec2-user',
                                            'OLDPWD': '/home/ec2-user',
                                            'PATH': '/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/opt/aws/bin:/home/ec2-user/.local/bin:/home/ec2-user/bin',
                                            'PWD': '/home/ec2-user/glowing-meme',
                                            'SHELL': '/bin/bash',
                                            'SHLVL': '1',
                                            'SSH_CLIENT': '100.36.117.3 62805 22',
                                            'SSH_CONNECTION': '100.36.117.3 62805 172.31.14.187 22',
                                            'SSH_TTY': '/dev/pts/0',
                                            'TERM': 'xterm',
                                            'USER': 'ec2-user',
                                            '_': '/usr/bin/python'},
                                'exe': '/usr/bin/python2.7',

                                'memory_percent': 2.1115545681536676,
                                'name': 'python',
                                'nice': 0,
                                'num_fds': 5,
                                'num_threads': 1,
                                'open_files': [],
                                'pid': 31690,
                                'ppid': 30124,
                                'status': 'running',
                                'terminal': '/dev/pts/0',
                                'username': 'ec2-user'}},
       'storage': {'free': 6370885632,
                   'percent': 22.5,
                   'total': 8318783488,
                   'used': 1845243904}}

def get_obj(id):
    import random
    json_['id'] = id
    json_['cpu']['load_avg']['1_min'] = random.randint(0, 10000)
    return json_

while True:
    for i in range(3):
        j = get_obj(str(i))
        #st = json.dumps(j)
        import os
        import sys
        import time
        import requests

        url = "http://localhost:8000/save_data/"
        data = j
        print(data)
        # pprint.pprint(data)
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print(r.status_code)
    time.sleep(1)
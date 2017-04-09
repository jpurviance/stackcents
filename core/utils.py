import json

from models import EC2


def get_cpu(instance):
    this_instance = get_all().filter(name=instance).first()
    if this_instance is not None:
        return this_instance['cpu']
    else:
        return None


def get_all():
    return EC2.objects.all()


def get_json(ec2):
    return json.loads(ec2.stats)


def get_storage_timeseries(instance):
    data = instance
    all_mem = list(sorted(data['storage'], key=lambda x: x['index']))
    return [float(mem['%util']) for mem in all_mem]

def get_all_storage_timeseries():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [get_storage_timeseries(data) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(sum(lll) / float(len(lll)))
    return ll

def get_memory_timeseries(instance):
    data = instance
    all_mem = list(sorted(data['mem'], key=lambda x: x['index']))
    return [float(mem['%memused']) for mem in all_mem]

def get_all_mem_timeseries():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [get_memory_timeseries(data) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(sum(lll) / float(len(lll)))
    return ll

def get_cpu_timeseries(instance):
    data = instance
    ncpu =  data['meta']['num_cpu']['num_cpu']
    all_cpus = list(sorted(data['cpu'], key=lambda x: x['index']))
    return [max(1.0, (float(cpu['load_avg_1'])*0.75)/ncpu) for cpu in all_cpus]


def get_all_cpu_timeseries():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [get_cpu_timeseries(data) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(float(x[i]))
        ll.append(sum(lll) / float(len(lll)))
    return ll


def should_recommend_bigger_instance(instance):
    ts = get_cpu_timeseries(instance)
    avg = sum(ts)/ float(len(ts))
    if avg >= 0.9:
        return True


def get_mongop(instance):
    if "mongod" in instance['processes']:
        return instance['processes']["mongod"]
    return None


def should_use_specific_db(instance):
    mongo = get_mongop(instance)
    if not mongo:
        return False
    return float(mongo['cpu_percent']) >= 70

def should_lambda(instance):
    process_list = instance['processes']
    # now iter

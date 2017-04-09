import json
import datetime
import statistics

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


def get_swap_used_timeseries(instance):
    data = instance
    all_mem = list(sorted(data['swap'], key=lambda x: x['index']))
    return [float(mem['%swpused']) for mem in all_mem]


def get_all_swap_used_timeseries():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_swap_used_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(sum(lll) / float(len(lll)))
    return list(reversed(ll))

def get_all_swap_used_timeseries_max():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_swap_used_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(max(lll))
    return list(reversed(ll))

def get_all_swap_used_timeseries_min():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_swap_used_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(min(lll))
    return list(reversed(ll))


def get_storage_timeseries(instance):
    data = instance
    all_mem = list(sorted(data['storage'], key=lambda x: x['index']))
    return [float(mem['%util']) for mem in all_mem]


def get_all_storage_timeseries():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_storage_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(sum(lll) / float(len(lll)))
    return list(reversed(ll))

def get_all_storage_timeseries_max():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_storage_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(max(lll))
    return list(reversed(ll))

def get_all_storage_timeseries_min():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_storage_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(min(lll))
    return list(reversed(ll))

def get_memory_timeseries(instance):
    data = instance
    all_mem = list(sorted(data['mem'], key=lambda x: x['index']))
    return [float(mem['%memused']) for mem in all_mem]


def get_all_mem_timeseries():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_memory_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(sum(lll) / float(len(lll)))
    return list(reversed(ll))

def get_all_mem_timeseries_max():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_memory_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(max(lll))
    return list(reversed(ll))

def get_all_mem_timeseries_min():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_memory_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(x[i])
        ll.append(min(lll))
    return list(reversed(ll))


def get_cpu_timeseries(instance):
    data = instance
    ncpu = data['meta']['num_cpu']['num_cpu']
    all_cpus = list(sorted(data['cpu'], key=lambda x: x['index']))
    return [min(1.0, (float(cpu['load_avg_1']) * 0.75) / ncpu) * 100 for cpu in all_cpus]


def get_all_cpu_timeseries():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_cpu_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(float(x[i]))
        ll.append(sum(lll) / float(len(lll)))
    return list(reversed(ll))


def get_all_cpu_timeseries_min():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_cpu_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(float(x[i]))
        ll.append(min(lll))
    return list(reversed(ll))


def get_all_cpu_timeseries_max():
    all_data = (get_json(ec2) for ec2 in get_all())
    l = [list(reversed(get_cpu_timeseries(data))) for data in all_data]
    max_idx = max(len(x) - 1 for x in l)
    ll = []
    for i in range(max_idx):
        lll = []
        for x in l:
            if i < len(x):
                lll.append(float(x[i]))
        ll.append(max(lll))
    return list(reversed(ll))


def should_recommend_bigger_instance(instance):
    ts = get_cpu_timeseries(instance)
    avg = sum(ts) / float(len(ts))
    if avg >= 0.9:
        return True


def get_mongop(process):
    if process[0]["name"] != "mongod":
        return None
    mx = max([float(proc['cpu_percent']) for proc in process])
    return {'cpu_percent': mx}


def get_postgres(process):
    if process[0]["name"] != "postmaster":
        return None
    mx = max([float(proc['cpu_percent']) for proc in process])
    return {'cpu_percent': mx}


def should_use_rds(process):
    postgres = get_postgres(process)
    if not postgres:
        return False
    return True
    #return float(postgres['cpu_percent']) >= 70

def should_use_dynamo(process):
    mongo = get_mongop(process)
    if not mongo:
        return False
    return float(mongo['cpu_percent']) >= 70


def should_lambda(process):
    #mx = max((float(proc['cpu_percent']) for proc in process))
    #md = statistics.median((proc['cpu_percent'] for proc in process))
    #return float(mx) - float(md) >= 70
    avg = float(sum((float(proc['cpu_percent']) for proc in process))) / max(len([float(proc['cpu_percent']) for proc in process]), 1)
    return (3 <= avg) and (avg <= 8)


def decide_rec(process):
    if should_use_rds(process):
        return ("You should consider running this database in a Relational Database (RDS) instead."
                , "This process is taking up high usage on the system and would be cheaper to run as a standalone "
                  "database instance")
    if should_use_dynamo(process):
        return ("You should consider running this database in DynamoDB instead."
                , "This process is taking up high usage on the system and would be cheaper to run as a standalone "
                  "database instance")
    if should_lambda(process):
        return ("you should consider running this function as an AWS lambda function", "This process has occasional "
                                                                                       "need of the instances "
                                                                                       "resources but has period of "
                                                                                       "downtime where there are is "
                                                                                       "no load. Running this as a "
                                                                                       "lambda would allow you to only "
                                                                                       "pay when the function is run.")
    else:
        return None, None


def should_add_disk_space(instance):
    print(instance['disk'])
    return float(instance['disk']['percent']) >= 90


def should_pay_upfront(instance):
    # return float(instance['meta']['uptime']) > 24000000
    return float(instance['meta']['uptime']) > 86400

def should_recommend_special_disk(instance):
    return float(instance['storage']['%util']) >= 70

def should_add_ram(instance):
    return float(instance['mem']['%memused']) >= 70

def get_instance_rec(instance):
    r,j = decide_instance_rec(instance)
    if r is None:
        r = "DO_NOT_USE"
        j = "DO_NOT_USE"
    return {"recommendation": r, "justification": j}
def decide_instance_rec(instance):
    if should_recommend_special_disk(instance):
        return "You should consider changing your instance type to a specialized instance with better read/write capabilities.",\
               "Your instance spends a lot of time reading/writing to disk."
    if should_add_ram(instance):
        return "You should consider upgrading your instance to a type with more RAM or try downloading more at http://www.downloadmoreram.com/download.html", "Your instance is using most of it's ram and/or swap."
    if should_add_disk_space(instance):
        return "You should consider adding another EBS volume or moving some of your files to S3.", "You have reached 90% " \
                                                                                                    "disk utilization and will soon run out of space."
    if should_pay_upfront(instance):
        return "You should consider making this a reserved instance.", "Since this instance has been running for " \
                                                                       "almost a year, it would have been cheaper to pay the reserved pricing than on demand pricing. Note that " \
                                                                       "this hack only checks for an uptime of over a day as a proof of concept."
    if should_recommend_bigger_instance(instance):
        return "You should consider a larger tier instance because your instance spends most of its life at the " \
               "hardware limitations", "A larger tier node would allow you to give amazon more money "
    return None, None


def get_recommendation_process(process, default):
    rec, just = decide_rec(process)
    if not rec:
        rec, just = default
    return {"recommendation": rec, "justification": just}


def get_recommendation_instance(instance, default):
    rec, just = decide_rec(instance)
    if not rec:
        rec, just = default
    return {"recommendation": rec, "justification": just}


def get_top_25_cpu_rec(process):
    return get_recommendation_process(process, ("DO_NOT_USE", "DO_NOT_USE"))


def get_bottom_25_cpu_rec(process):
    return get_recommendation_process(process, ("DO_NOT_USE", "DO_NOT_USE"))


def get_top_25_mem_rec(process):
    return get_recommendation_process(process, ("DO_NOT_USE", "DO_NOT_USE"))


def get_bottom_25_mem_rec(process):
    return get_recommendation_process(process, ("DO_NOT_USE", "DO_NOT_USE"))


def get_top_25_cpu(processes):
    processes_cpu = list(
        sorted([(proc, float(list(sorted(proc, key=lambda x: x['index']))[-1]['cpu_percent'])) for proc in processes],
               key=lambda x: x[1], reverse=True))
    fourth = max(len(processes_cpu) // 4, 1)
    top_25 = processes_cpu[:fourth]
    just_proc = map(lambda x: x[0], top_25)
    plist = []
    for proc in just_proc:
        p_data = list(sorted(proc, key=lambda x: x['index']))[-1]
        name = proc[0]['name']
        result = get_top_25_cpu_rec(proc)
        p = {
            "name": name,
            "command_line": p_data['cmdline'],
            "cpu": processes_cpu[0][1],
            "memory": p_data['memory_percent'],
            "pid": p_data['pid'],
            "threads": p_data['num_threads'],
            'recommendation': result["recommendation"],
            'justification': result["justification"]
        }
        plist.append(p)
    return plist


def get_top_25_mem(processes):
    processes_mem = list(
        sorted(
            [(proc, float(list(sorted(proc, key=lambda x: x['index']))[-1]['memory_percent'])) for proc in processes],
            key=lambda x: x[1], reverse=True))
    fourth = max(len(processes_mem) // 4, 1)
    # print(fourth)
    top_25 = processes_mem[:fourth]
    just_proc = map(lambda x: x[0], top_25)
    plist = []
    for proc in just_proc:
        p_data = list(sorted(proc, key=lambda x: x['index']))[-1]
        name = proc[0]['name']
        result = get_top_25_mem_rec(proc)
        p = {
            "name": name,
            "command_line": p_data['cmdline'],
            "cpu": p_data['cpu_percent'],
            "memory": processes_mem[0][1],
            "pid": p_data['pid'],
            "threads": p_data['num_threads'],
            'recommendation': result["recommendation"],
            'justification': result["justification"]
        }
        plist.append(p)
    return plist


def get_bottom_25_mem(processes):
    processes_mem = list(
        sorted(
            [(proc, float(list(sorted(proc, key=lambda x: x['index']))[-1]['memory_percent'])) for proc in processes],
            key=lambda x: x[1]))
    fourth = max(len(processes_mem) // 4, 1)
    top_25 = processes_mem[:fourth]
    just_proc = map(lambda x: x[0], top_25)
    plist = []
    for proc in just_proc:
        p_data = list(sorted(proc, key=lambda x: x['index']))[-1]
        name = proc[0]['name']
        result = get_bottom_25_mem_rec(proc)
        p = {
            "name": name,
            "command_line": p_data['cmdline'],
            "cpu": p_data['cpu_percent'],
            "memory": processes_mem[0][1],
            "pid": p_data['pid'],
            "threads": p_data['num_threads'],
            'recommendation': result["recommendation"],
            'justification': result["justification"]
        }
        plist.append(p)
    return plist


def get_bot_25_cpu(processes):
    processes_cpu = list(
        sorted([(proc, float(list(sorted(proc, key=lambda x: x['index']))[-1]['cpu_percent'])) for proc in processes],
               key=lambda x: x[1]))
    fourth = max(len(processes_cpu) // 4, 1)
    bot_25 = processes_cpu[:fourth]
    just_proc = map(lambda x: x[0], bot_25)
    plist = []
    for proc in just_proc:
        p_data = list(sorted(proc, key=lambda x: x['index']))[-1]
        name = proc[0]['name']
        result = get_bottom_25_cpu_rec(proc)
        p = {
            "name": name,
            "command_line": p_data['cmdline'],
            "cpu": processes_cpu[0][1],
            "memory": p_data['memory_percent'],
            "pid": p_data['pid'],
            "threads": p_data['num_threads'],
            'recommendation': result["recommendation"],
            'justification': result["justification"]
        }
        plist.append(p)
    return plist

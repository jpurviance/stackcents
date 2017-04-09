import json
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
    ncpu = data['meta']['num_cpu']['num_cpu']
    all_cpus = list(sorted(data['cpu'], key=lambda x: x['index']))
    return [max(1.0, (float(cpu['load_avg_1']) * 0.75) / ncpu) for cpu in all_cpus]


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
    avg = sum(ts) / float(len(ts))
    if avg >= 0.9:
        return True


def get_mongop(process):
    if process[0]["name"] != "mongod":
        return None
    mx = max([float(proc['cpu_percent']) for proc in process])
    return {'cpu_percent': mx}


def should_use_specific_db(process):
    mongo = get_mongop(process)
    if not mongo:
        return False
    return float(mongo['cpu_percent']) >= 70


def should_lambda(process):
    mx = max((float(proc['cpu_percent']) for proc in process))
    md = statistics.median((proc['cpu_percent'] for proc in process))
    return float(mx) - float(md) >= 70


def decide_rec(process):
    if should_use_specific_db(process):
        return ("you should consider running this as a specific database instance (insert AWS jargon here)"
                , "This process is taking up high usage on the system so would be cheaper to run as a standalone "
                  "database with (AWS service)")
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


def decide_instance_rec(instance):
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
    return get_recommendation_process(process, ("default top 25 cpu", "this is a default"))


def get_bottom_25_cpu_rec(process):
    return get_recommendation_process(process, ("default bottom 25 cpu", "this is a default"))


def get_top_25_mem_rec(process):
    return get_recommendation_process(process, ("default top 25 memory", "this is a default"))


def get_bottom_25_mem_rec(process):
    return get_recommendation_process(process, ("default bottom 25 memory", "this is a default"))


def get_top_25_cpu(processes):
    processes_cpu = list(
        sorted([(proc, float(list(sorted(proc, key=lambda x: x['index']))[-1]['cpu_percent'])) for proc in processes],
               key=lambda x: x[1], reverse=True))
    fourth = max(len(processes_cpu) // 4, 1)
    top_25 = processes_cpu[:fourth]
    just_proc = map(lambda x: x[0], top_25)
    for proc in just_proc:
        result = get_top_25_cpu_rec(proc)
        just_proc["recommendation"] = result["recommendation"]
        just_proc["justification"] = result["justification"]
    return just_proc


def get_bot_25_cpu(processes):
    processes_cpu = list(
        sorted([(proc, float(list(sorted(proc, key=lambda x: x['index']))[-1]['cpu_percent'])) for proc in processes],
               key=lambda x: x[1]))
    fourth = max(len(processes_cpu) // 4, 1)
    bot_25 = processes_cpu[:fourth]
    just_proc = map(lambda x: x[0], bot_25)
    for proc in just_proc:
        result = get_bottom_25_cpu_rec(proc)
        just_proc["recommendation"] = result["recommendation"]
        just_proc["justification"] = result["justification"]
    return just_proc

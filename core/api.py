import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from utils import EC2, get_json, get_all, get_cpu, get_all_cpu_timeseries, get_all_mem_timeseries, \
    get_all_storage_timeseries


@csrf_exempt
def save_data(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        try:
            id = json_data['id']
            try:
                instance = EC2.objects.get(name=id)
                instance.stats = request.body
            except EC2.DoesNotExist:
                instance = EC2(name=id, stats=request.body)
            instance.save()
        except KeyError:
            return HttpResponse(status=400)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


# API GETS
@csrf_exempt
def get_instances(request):
    instances = get_all()
    l = [e.name for e in instances]
    return JsonResponse({"instances": l})


@csrf_exempt
def get_all_cpu(request):
    instances = get_all()
    l = []
    for instance in instances:
        l.append(get_cpu(instance))
    return JsonResponse({"all_cpu": l})


@csrf_exempt
def get_instances_summary(request):
    all_data = (get_json(ec2) for ec2 in get_all())
    l = []
    for data in all_data:
        t = {'id': data['id'],
             'cpu': list(sorted(data['cpu'],key=lambda x: x['index']))[-1]['load_avg_1'],
             'memory': list(sorted(data['mem'], key=lambda x: x['index']))[-1]['%memused'],
             'network': 100000,
             'storage': list(sorted(data['storage'], key=lambda x: x['index']))[-1]['%util']
             }
        l.append(t)
    return JsonResponse({"total": l})


@csrf_exempt
def get_cpu_for_instance(request, instance):
    i = get_cpu(instance)
    if i:
        return JsonResponse(i)
    else:
        return HttpResponse(status=404)


@csrf_exempt
def get_instance_details(request):
    instance = request.GET.get('instance', None)
    print(instance)
    if instance is None:
        return HttpResponse(status=404)
    try:
        instance = EC2.objects.get(name=instance)
        data = get_json(instance)
        processes = []
        for process in data['processes']:
            p_data = data['processes'][process]
            p = {
                "name": process,
                "command_line": p_data['cmdline'],
                "cpu": p_data['cpu_percent'],
                "memory": p_data['memory_percent'],
                "pid": p_data['pid'],
                "threads": p_data['num_threads']
            }
            processes.append(p)
        instance_stats = {'id': data['id'],
             'cpu': list(sorted(data['cpu'],key=lambda x: x['index']))[-1]['load_avg_1'],
             'memory': list(sorted(data['mem'], key=lambda x: x['index']))[-1]['%memused'],
             'network': 100000,
             'storage': list(sorted(data['storage'], key=lambda x: x['index']))[-1]['%util'],
             'metadata': {
                 "num_cpu": data['meta']['num_cpu']['num_cpu'],
                 "os":  "???????????!?!?!?!?!?",
                 "hostname": data['meta']['hostname'],
                 "type": data['meta']['instance-type'],
                 "ip": data['meta']['public-ipv4'],
                 "id": data['id']
                },
              "processes": processes
             }
        return JsonResponse(instance_stats)

    except EC2.DoesNotExist:
        return HttpResponse(status=404)


@csrf_exempt
def get_all_time_series(request):
    return JsonResponse({"CPU": get_all_cpu_timeseries(), "MEM": get_all_mem_timeseries(),
                         "STORAGE": get_all_storage_timeseries()})

#-*-coding:utf-8 -*-
__author__ = 'guyu'

import sys
import gevent
import gevent.monkey
import time, requests
import urllib2
import simplejson as json
import more_itertools
import signal
import multiprocessing
from multiprocessing import Process
from memory_profiler import profile
gevent.monkey.patch_socket()

if 'threading' in sys.modules:
    del sys.modules['threading']
    # raise Exception('threading module loaded before patching!')
gevent.monkey.patch_all()



def time_decorator(func,**kwargs):
    def run_time(*args,**kwargs):
        start=time.time()
        # print 'start:', start
        func(*args,**kwargs)
        stop=time.time()
        print 'run_time:',(stop-start)
    return run_time
urlone='http://10.6.115.145/render?&target=collectd.cl0notify02_prep_searchone_tsk.sensor-service_stats.gauge-tps&from=-150000minutes&format=json'
urltwo='http://10.6.115.145/render?&target=collectd.cl0cnd02_prep_searchone_tsk.aggregation-cpu-average.cpu-idle&from=-150000minutes&format=json'

# urls = ['http://10.6.115.129:5001/status','http://10.6.115.130:5001/status','http://10.6.115.131:5001/status',
#         'http://10.6.115.129:5001/status','http://10.6.115.130:5001/status','http://10.6.115.131:5001/status',
#         'http://10.6.115.129:5001/status','http://10.6.115.130:5001/status','http://10.6.115.131:5001/status',
#         'http://10.6.115.129:5001/status','http://10.6.115.130:5001/status','http://10.6.115.131:5001/status',
#         'http://10.6.115.129:5001/status','http://10.6.115.130:5001/status','http://10.6.115.131:5001/status',
#         'http://10.6.115.129:5001/status','http://10.6.115.130:5001/status','http://10.6.115.131:5001/status',
#         'http://10.6.115.129:5001/status','http://10.6.115.130:5001/status','http://10.6.115.131:5001/status',]

wholeurls = [urlone,urlone,urlone,urlone,urlone,urlone,urlone,urlone,urlone,urlone,urlone,urlone,urlone,urlone,urlone,urlone,
            urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,
            urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,urltwo,]

# wholeurls = [urlone,urlone,urlone,urlone,urlone,urlone,urlone]

# urls = [urlone,urlone,urlone,urlone,urlone,urlone]

def get_data(url,pid):
    #
    gevent.sleep(0)
    # data = requests.get(url).json()
    # print('Process %s' % (pid))
    # return data

    response = urllib2.urlopen(url)
    result = response.read()
    json_result = json.loads(result)
    # datetime = json_result['datetime']

    # print('Process %s: %s' % (pid, datetime))
    # print('Process %s' % (pid))
    # return json_result['datetime']
    return result

@time_decorator
# @profile
def sync_get_data():
    num = 0
    for url in wholeurls:
        num = num +1
        get_data(url,num)


@time_decorator
# @profile
def async_get_data():
    list = []
    num = 0
    for url in wholeurls:
        num = num+1
        list.append(gevent.spawn(get_data, url,num))
    gevent.joinall(list)


def tasks_start(tasklist):
    task = get_tasks(tasklist)
    gevent.joinall(task)

def get_tasks(urls):
    list = []
    num = 0
    for url in urls:
        num = num+1
        list.append(gevent.spawn(get_data, url,num))
    return list

@time_decorator
# @profile
def multiprocess_start():

    cpu_core = multiprocessing.cpu_count()
    process_num = cpu_core + 1
    part_step = len(wholeurls) / process_num

#不是把list等分成几分，是几个一组把list切分


    div_urls_list = list(more_itertools.chunked(wholeurls, part_step))
    # print "LENGTH OF WHOLEURLS_LIST: ",len(wholeurls)
    print "CUT WHOLERULS_LIST INTO ",len(div_urls_list), "PARTS"
    print "LENTH OF EACH PARTS: ",part_step
    # print "LENGTH OF DIV_URLS_LIST:",len(div_urls_list)
# div_task_list
# [[],[],[]]
#     print "USE", cpu_core ,"PROCESS"
    processlist=[]
    for urls in div_urls_list:
        p = Process(target=tasks_start,args=(urls,))
        p.start()
        processlist.append(p)
    # print processlist
    print "USE",len(processlist), "PROCESS"
    for pl in processlist:
        pl.join()

        # p.join()
        # print p.is_alive()

    # tasks0 = get_tasks(div_urls_list[0])
    # tasks1 = get_tasks(div_urls_list[1])
    # tasks2 = get_tasks(div_urls_list[2])
    #
    # Process(target=tasks_start,args=(div_urls_list[0],)).start()
    # Process(target=tasks_start,args=(div_urls_list[1],)).start()
    # Process(target=tasks_start,args=(tasks2,)).start()
    #

if __name__ == '__main__':

    # print "Syncget_data:"
    # sync_get_data()
    # print '-'*50
    print "Asyncget_data:"
    async_get_data()
    print '-'*50
    time.sleep(0.2)
    print "Multiprocess_asyncget_data:"
    multiprocess_start()



#这个不是后台的..
    # gevent.signal(signal.SIGQUIT, gevent.shutdown)
    # thread = gevent.spawn(run_forever)
    # thread.join()







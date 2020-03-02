import pymqi

queue_manager = 'QM1'
channel = 'DEV.APP.SVRCONN'
host = '127.0.0.1'
port = '1414'
queue_name = 'TEST.1'
conn_info = '%s(%s)' % (host, port)

md = pymqi.MD()

gmo = pymqi.GMO()
gmo.Options = pymqi.CMQC.MQGMO_WAIT | pymqi.CMQC.MQGMO_FAIL_IF_QUIESCING
gmo.WaitInterval = 5000

qmgr = pymqi.connect(queue_manager, channel, conn_info)
queue = pymqi.Queue(qmgr, queue_name)

keep_running = True

while keep_running:
    try:
        message = queue.get(None, md, gmo)
        # handle message
        print(message)
        md.MsgId = pymqi.CMQC.MQMI_NONE
        md.CorrelId = pymqi.CMQC.MQCI_NONE
        md.GroupId = pymqi.CMQC.MQGI_NONE

    except pymqi.MQMIError as e:
        if e.comp == pymqi.CMQC.MQCC_FAILED and e.reason == pymqi.CMQC.MQRC_NO_MSG_AVAILABLE:
            pass
        else:
            raise

queue.close()
qmgr.disconnect()

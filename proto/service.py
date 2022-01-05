'''
Descripttion: 
Version: 1.0
Author: easonhe
Date: 2022-01-05 23:01:13
LastEditors: easonhe
LastEditTime: 2022-01-05 23:13:39
'''
import time
import grpc
import hello1_pb2 as pb2
import hello1_pb2_grpc as pb2_grpc
from concurrent import futures

class HelloEaon(pb2_grpc.HelloEasonServicer):
    def HelloEason(self, request, context):
        name = request.name
        age = request.age
        result =  f'my name is {name},i am {age} years old'
        return pb2.HelloEasonReply(result=result)


def run():
    grpc_server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=4)
    )
    pb2_grpc.add_HelloEasonServicer_to_server(HelloEaon(),grpc_server)
    grpc_server.add_insecure_port('0.0.0.0:5000')
    print('server will start')
    grpc_server.start()

    try:
        while 1:
            time.sleep(3600)
    except KeyboardInterrupt:
        grpc_server.stop(0)

if __name__ =='__main__':
    run()
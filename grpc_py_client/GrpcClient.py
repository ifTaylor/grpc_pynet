import grpc

from grpc_tools import protoc

protoc.main([
    'grpc_tools.protoc',
    '-I{}'.format('../protos'),
    '--python_out={}'.format('.'),
    '--grpc_python_out={}'.format('.'),
    '../protos/pynet_proto.proto'
])


from pynet_proto_pb2 import HelloRequest
from pynet_proto_pb2_grpc import GreeterStub

def main():

    channel = grpc.insecure_channel("127.0.0.1:5000")
    greeter_client = GreeterStub(channel)
    response = greeter_client.SayHello(HelloRequest(name='\nGeneralKenobi'))
    print(response)
    print("Press any key to exit...")
    input()

if __name__ == "__main__":
    main()
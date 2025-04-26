import grpc
import chat_pb2
import chat_pb2_grpc

def generate_messages():
    # This simulates the user sending messages to the server.
    for i in range(10):
        yield chat_pb2.Message(user="Client", text=f"Hello from client {i}")
        time.sleep(1)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatServiceStub(channel)

    # This starts the chat stream
    response_iterator = stub.ChatStream(generate_messages())

    for response in response_iterator:
        print(f"Server says: {response.text}")

if __name__ == '__main__':
    run()

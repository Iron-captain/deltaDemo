import grpc
from concurrent import futures
import time
import chat_pb2
import chat_pb2_grpc

class ChatService(chat_pb2_grpc.ChatServiceServicer):
    def ChatStream(self, request_iterator, context):
        for msg in request_iterator:
            # This is where we process incoming messages.
            print(f"Message from {msg.user}: {msg.text}")
            # Here we send the message back to the client.
            yield chat_pb2.Message(user="Server", text=f"Received: {msg.text}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started, listening on port 50051...")
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

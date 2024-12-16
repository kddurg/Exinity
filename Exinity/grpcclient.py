import grpc
import tick_service_pb2
import tick_service_pb2_grpc

def run():
    # Step 1: Set up a connection to the gRPC server
    channel = grpc.insecure_channel('localhost:50051')  # Adjust the address as needed
    stub = tick_service_pb2_grpc.TickServiceStub(channel)

    # Step 2: Start streaming price ticks
    try:
        for price_tick in stub.StreamTicks(tick_service_pb2.Empty()):
            # Process each price tick here
            print(f"Received tick - Symbol: {price_tick.symbol}, Price: {price_tick.price}, Volume: {price_tick.volume}, Timestamp: {price_tick.timestamp}")
    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")

if __name__ == '__main__':
    run()
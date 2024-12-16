import grpc
import chart_service_pb2
import chart_service_pb2_grpc

def run(symbol, interval):
                                                                                # Step 1: Set up a connection to the gRPC server
    channel = grpc.insecure_channel('localhost:50051') 
    stub = chart_service_pb2_grpc.ChartServiceStub(channel)

                                                                                 # Step 2: Create a ChartRequest message
    request = chart_service_pb2.ChartRequest(symbol=symbol, interval=interval)

    # Step 3: Start streaming chart data
    try:
        for chart_data in stub.StreamChartData(request):
            # Process and print the chart data
            print(f"Symbol: {chart_data.symbol}")
            for tick in chart_data.price_ticks:
                print(f"Time: {tick.timestamp}, Open: {tick.open}, High: {tick.high}, Low: {tick.low}, Close: {tick.close}")
    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")

if __name__ == '__main__':
    # Example usage of the function
    run('AAPL', 5)  
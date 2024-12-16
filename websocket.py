import websocket
import grpc
import data_service_pb2
import data_service_pb2_grpc
import json

# Function to send data to gRPC server
def send_to_grpc(stub, message_id, message_value):
    data_message = data_service_pb2.DataMessage(id=message_id, value=message_value)
    try:
        response = stub.SendData(data_message)
        print("Data sent to gRPC:", message_id, message_value)
    except grpc.RpcError as e:
        print(f"gRPC error: {e.code()} - {e.details()}")

# Callback for receiving messages from WebSocket
def on_message(ws, message):
    print("Received WebSocket message:", message)
    # Assuming the message is JSON formatted
    data = json.loads(message)
    
    # Extract required fields from the received data
    message_id = data.get("id")
    message_value = data.get("value")
    
    # Send the extracted data to gRPC
    send_to_grpc(grpc_stub, message_id, message_value)

# Callback for error handling
def on_error(ws, error):
    print("WebSocket error:", error)

# Callback for WebSocket close
def on_close(ws):
    print("WebSocket closed")

# Main function to run the script
if __name__ == '__main__':
    # Step 1: Set up gRPC connection
    grpc_channel = grpc.insecure_channel('localhost:50051')  # Adjust based on your gRPC server's address
    grpc_stub = data_service_pb2_grpc.DataServiceStub(grpc_channel)

    # Step 2: Set up WebSocket connection
    websocket_url = "ws://your.websocket.api"  # Replace this with your WebSocket API URL
    ws = websocket.WebSocketApp(websocket_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    
    try:
        ws.run_forever()  # Keep the WebSocket connection open
    except KeyboardInterrupt:
        ws.close()
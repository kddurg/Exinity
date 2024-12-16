syntax = "proto3";

package ticker;

// The message representing a price tick
message PriceTick {
    string symbol = 1;
    double price = 2;
    int32 volume = 3;
    int64 timestamp = 4; // Unix timestamp
}

// The service for receiving price ticks
service TickService {
    rpc StreamTicks(Empty) returns (stream PriceTick);
}

// A message for empty requests
message Empty {}
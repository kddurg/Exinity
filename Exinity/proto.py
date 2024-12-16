syntax = "proto3";

package chart;

// Message representing chart data
message ChartData {
    string symbol = 1;
    repeated PriceTick price_ticks = 2; // List of price ticks
}

// Message representing a price tick
message PriceTick {
    double open = 1;
    double high = 2;
    double low = 3;
    double close = 4;
    int64 timestamp = 5; // Unix timestamp
}

// Service for streaming chart data
service ChartService {
    rpc StreamChartData(ChartRequest) returns (stream ChartData);
}

// Message for the request
message ChartRequest {
    string symbol = 1;
    int32 interval = 2; // e.g., 1 minute, 5 minutes, etc.
}
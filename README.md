# gRPC Project: Python Client and .NET 6 Server

This project demonstrates how to use gRPC to establish communication between a Python client and a .NET 6 server.

## Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x
- .NET 6 SDK

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/ifTaylor/grpc_pynet.git
    ```

2. Change to the project directory:

    ```shell
    cd grpc_pynet
    ```

## Run .NET 6 Server

1. Change to the server directory from root:

    ```shell
    cd grcp_net_server
    cd GrpcService
    ```

2. Start the server:

    ```shell
    dotnet run
    ```

## Run Python Client

1. Create and activate a virtual environment:

    ```shell
    python -m venv venv
    cd venv\Scripts
    activate.bat
    ```

2. Install the required Python dependencies:

    ```shell
    pip install -r client/requirements.txt
    ```

3. Change to the client script directory:

    ```shell
    cd grpc_py_client
    ```

3. Run the client request:

    ```shell
    python GrpcClient.py
    ```

## Run .NET 6 Client

1. Change to the server directory from root:

    ```shell
    cd grcp_net_client2test
    cd GrpcClient
    ```

2. Start the client:

    ```shell
    dotnet run
    ```

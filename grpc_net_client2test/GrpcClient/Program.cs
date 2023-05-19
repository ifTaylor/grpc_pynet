using Grpc.Net.Client;

var handler = new HttpClientHandler
{
    ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator
};

var channelOptions = new GrpcChannelOptions
{
    HttpHandler = handler
};

var channel = GrpcChannel.ForAddress("http://127.0.0.1:5000",channelOptions);

var client = new Greeter.GreeterClient(channel);
 var reply = await client.SayHelloAsync(
                  new HelloRequest { Name = "\nGeneral Kenobi" });
Console.WriteLine("Greeting: " + reply.Message);
Console.WriteLine("Press any key to exit...");
Console.ReadKey();
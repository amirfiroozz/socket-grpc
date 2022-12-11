from concurrent import futures
import proto.sorting_pb2_grpc as sorting_pb2_grpc
import server.sorting as sorting
import grpc
class SortingServicer(sorting_pb2_grpc.SortingServiceServicer):
    def Sort(self, request, context):
        print("request recived")
        sortingClass = sorting.sortingFactory(request.type)
        yield from sortingClass.sort(request.array , request.sleepTime)
        

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
    sorting_pb2_grpc.add_SortingServiceServicer_to_server(SortingServicer() , server)
    server.add_insecure_port('[::]:50001')
    print("grpc server is running on localhost:50001.....")
    server.start()
    server.wait_for_termination()

if __name__=="__main__":
    serve()
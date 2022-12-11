import proto.sorting_pb2 as sorting_pb2
def generateNoErrorGRPCResponse():
    err = sorting_pb2.Error()
    err.isError = False
    err.message = "all fine!"
    return err

def generateErrorGRPCResponse():
    err = sorting_pb2.Error()
    err.isError = True
    err.message = "something happend!!"
    return err

def setSortingResponseArray(arr , isDone , err , left=0 , right=0):
    response = sorting_pb2.ResponseSorting()
    response.array.extend(arr)
    response.isDone = isDone
    response.left = left
    response.right = right
    response.error.CopyFrom(err)
    yield response

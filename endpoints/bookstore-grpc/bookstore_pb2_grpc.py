# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import bookstore_pb2 as bookstore__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class BookstoreStub(object):
  """A simple Bookstore API.

  The API manages shelves and books resources. Shelves contain books.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListShelves = channel.unary_unary(
        '/endpoints.examples.bookstore.Bookstore/ListShelves',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=bookstore__pb2.ListShelvesResponse.FromString,
        )
    self.CreateShelf = channel.unary_unary(
        '/endpoints.examples.bookstore.Bookstore/CreateShelf',
        request_serializer=bookstore__pb2.CreateShelfRequest.SerializeToString,
        response_deserializer=bookstore__pb2.Shelf.FromString,
        )
    self.GetShelf = channel.unary_unary(
        '/endpoints.examples.bookstore.Bookstore/GetShelf',
        request_serializer=bookstore__pb2.GetShelfRequest.SerializeToString,
        response_deserializer=bookstore__pb2.Shelf.FromString,
        )
    self.DeleteShelf = channel.unary_unary(
        '/endpoints.examples.bookstore.Bookstore/DeleteShelf',
        request_serializer=bookstore__pb2.DeleteShelfRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.ListBooks = channel.unary_unary(
        '/endpoints.examples.bookstore.Bookstore/ListBooks',
        request_serializer=bookstore__pb2.ListBooksRequest.SerializeToString,
        response_deserializer=bookstore__pb2.ListBooksResponse.FromString,
        )
    self.CreateBook = channel.unary_unary(
        '/endpoints.examples.bookstore.Bookstore/CreateBook',
        request_serializer=bookstore__pb2.CreateBookRequest.SerializeToString,
        response_deserializer=bookstore__pb2.Book.FromString,
        )
    self.GetBook = channel.unary_unary(
        '/endpoints.examples.bookstore.Bookstore/GetBook',
        request_serializer=bookstore__pb2.GetBookRequest.SerializeToString,
        response_deserializer=bookstore__pb2.Book.FromString,
        )
    self.DeleteBook = channel.unary_unary(
        '/endpoints.examples.bookstore.Bookstore/DeleteBook',
        request_serializer=bookstore__pb2.DeleteBookRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class BookstoreServicer(object):
  """A simple Bookstore API.

  The API manages shelves and books resources. Shelves contain books.
  """

  @staticmethod
  def ListShelves(request, context):
    """Returns a list of all shelves in the bookstore.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  @staticmethod
  def CreateShelf(request, context):
    """Creates a new shelf in the bookstore.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  @staticmethod
  def GetShelf(request, context):
    """Returns a specific bookstore shelf.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  @staticmethod
  def DeleteShelf(request, context):
    """Deletes a shelf, including all books that are stored on the shelf.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  @staticmethod
  def ListBooks(request, context):
    """Returns a list of books on a shelf.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  @staticmethod
  def CreateBook(request, context):
    """Creates a new book.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  @staticmethod
  def GetBook(request, context):
    """Returns a specific book.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  @staticmethod
  def DeleteBook(request, context):
    """Deletes a book from a shelf.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BookstoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListShelves': grpc.unary_unary_rpc_method_handler(
          servicer.ListShelves,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=bookstore__pb2.ListShelvesResponse.SerializeToString,
      ),
      'CreateShelf': grpc.unary_unary_rpc_method_handler(
          servicer.CreateShelf,
          request_deserializer=bookstore__pb2.CreateShelfRequest.FromString,
          response_serializer=bookstore__pb2.Shelf.SerializeToString,
      ),
      'GetShelf': grpc.unary_unary_rpc_method_handler(
          servicer.GetShelf,
          request_deserializer=bookstore__pb2.GetShelfRequest.FromString,
          response_serializer=bookstore__pb2.Shelf.SerializeToString,
      ),
      'DeleteShelf': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteShelf,
          request_deserializer=bookstore__pb2.DeleteShelfRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'ListBooks': grpc.unary_unary_rpc_method_handler(
          servicer.ListBooks,
          request_deserializer=bookstore__pb2.ListBooksRequest.FromString,
          response_serializer=bookstore__pb2.ListBooksResponse.SerializeToString,
      ),
      'CreateBook': grpc.unary_unary_rpc_method_handler(
          servicer.CreateBook,
          request_deserializer=bookstore__pb2.CreateBookRequest.FromString,
          response_serializer=bookstore__pb2.Book.SerializeToString,
      ),
      'GetBook': grpc.unary_unary_rpc_method_handler(
          servicer.GetBook,
          request_deserializer=bookstore__pb2.GetBookRequest.FromString,
          response_serializer=bookstore__pb2.Book.SerializeToString,
      ),
      'DeleteBook': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteBook,
          request_deserializer=bookstore__pb2.DeleteBookRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'endpoints.examples.bookstore.Bookstore', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))

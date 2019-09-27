class channelmock:
    def queue_declare(self, queue="myqueue", durable=True):
        return 1

    def queue_bind(self, exchange="ex_name",
                   queue="queue_name", routing_key="my_key"):
        return 1

    def exchange_declare(self, exchange='ex_name', exchange_type="topic"):
        return 2

    def basic_publish(self, exchange="ex_name", routing_key="my_key",
                      body="message", properties="wdw"):
        return None


class rabbitmqmockmethods:
    def channel(self):
        return channelmock()

    def close(self):
        return 1

class method:
    delivery_tag = 2
    pass
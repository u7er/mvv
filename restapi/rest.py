from http.server import BaseHTTPRequestHandler,HTTPServer, SimpleHTTPRequestHandler
import json
import dbtool
import time
import traceback

class Ordering:
    __conn = None
    def __init__(self):
        self.__conn = dbtool.DBTool()

    def newOrder(self):
        order_id = None
        sql_reg_order = f"""
            insert into requests (state, date) values('new', {time.time()})
        """
        try:
            order_id = self.__conn.execute_sql(sql_reg_order).lastrowid
        except:
            traceback.print_exc()
        return order_id
    
    def delOrder(self, order_id):
        isDeleted = False
        sql_reg_order = f"""
            delete from requests where rqst_id = {order_id}
        """
        try:
            self.__conn.execute_sql(sql_reg_order)
            isDeleted = True
        except:
            traceback.print_exc()
        return isDeleted

    def checkOrder(self, order_id):
        position = 1
        # TODO: Можно переписать на rqst_id
        sql_reg_order = f"""
            select count(date) from requests where date < (select date from requests where rqst_id = {order_id})
        """
        try:
            res = self.__conn.execute_sql(sql_reg_order).fetchone()
            position = res[0] + 1
        except:
            traceback.print_exc()
        return position

    def getOrder(self):
        order = None
        sql_reg_order = f"""
            select rqst_id from requests where state = "new" order by rqst_id asc limit 1
        """
        sql_reg_order_change_state = """
            update requests set state = "proccessing" where rqst_id = {}
        """
        try:
            res = self.__conn.execute_sql(sql_reg_order).fetchone()
            if res is None:
                order = 0
            else:
                order = res[0]
                res = self.__conn.execute_sql(sql_reg_order_change_state.format(order))
                print(f'Статус {order} обновлен')
        except:
            traceback.print_exc()
        return order


ordering = None


class GetHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.path = 'pages/index.html'
                return SimpleHTTPRequestHandler.do_GET(self)

        def __newOrder(self):
            order = ordering.newOrder()
            response = {
                'order': order
            }
            return json.dumps(response).encode('utf-8')

        def __delOrder(self, order_id):
            isDel = ordering.delOrder(order_id)
            response = {
                'state': 'deleted'
            }
            return json.dumps(response).encode('utf-8')

        def __checkOrder(self, order_id):
            position = ordering.checkOrder(order_id)
            response = {
                'position': position
            }
            return json.dumps(response).encode('utf-8')

        def __getOrder(self):
            order = ordering.getOrder()
            response = {
                'order': order
            }
            return json.dumps(response).encode('utf-8')

        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.data_string = self.rfile.read(int(self.headers['Content-Length']))
            body = None
            order_id = None
            try:
                body = json.loads(self.data_string) if self.data_string else {}
                order_id = body.get('order')
            except:
                pass
            if self.path == '/new':
                data = self.__newOrder()
            elif self.path == '/check':
                if order_id is None:
                    self.send_response(404)
                    self.wfile.write(bytes(b'send me order_id in the body'))
                    return
                data = self.__checkOrder(order_id)
            elif self.path == '/del':
                if order_id is None:
                    self.send_response(404)
                    self.wfile.write(bytes(b'send me order_id in the body'))
                    return
                data = self.__delOrder(order_id)
            elif self.path == '/get':
                data = self.__getOrder()
            else:
                data = b'EMPTY REQUEST'
            self.wfile.write(bytes(data))
            return

def goRest():
    global ordering
    ordering = Ordering()
    Handler=GetHandler
    httpd=HTTPServer(("localhost", 50000), Handler)
    httpd.serve_forever()


goRest()
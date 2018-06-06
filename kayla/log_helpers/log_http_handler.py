"""
HTTP Handlers
"""
from logging.handlers import HTTPHandler
import requests


class LogHttpHandler(HTTPHandler):
    """
    Simple HTTP Handler
    """

    def __init__(self, logPath, host, url, method, protocol='http'):
        """
        Constructor
        :param logPath: log path on HTTP server
        :param host: Host name or IP
        :param url: URL of web services
        :param method: HTTP method
        :param protocol: HTTP or HTTPS
        """
        HTTPHandler.__init__(self, host, url, method)
        self.logPath = logPath
        self.session = requests.Session()
        self.protocol = protocol

    def mapLogRecord(self, record):
        """
        Map log record as required format of HTTP/HTTPS server
        :param record:
        :return:
        """
        record_modified = HTTPHandler.mapLogRecord(self, record)
        record_modified['logPath'] = self.logPath
        record_modified['msg'] = record_modified['msg'].encode('utf-8')
        return record_modified

    def emit(self, record):
        """
        Emit log
        :param record:
        :return:
        """
        try:
            host = self.host
            url = self.url
            url = self.protocol + '://' + host + '/' + url
            data = self.mapLogRecord(record)

            self.session.post(url, data=data, timeout=10)

        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            self.handleError(record)

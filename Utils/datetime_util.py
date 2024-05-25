import datetime
import time

class DateTimeUtil:
    
    @staticmethod
    def now_timestamp():
        now = datetime.datetime.now()
        return int(now.timestamp())
    
    @staticmethod
    def now_date():
        time_local = time.localtime(DateTimeUtil.now_timestamp())
        dt = time.strftime("%Y-%m-%d", time_local)
        return dt
    
    @staticmethod
    def now_datetime():
        time_local = time.localtime(DateTimeUtil.now_timestamp())
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return dt

    @staticmethod
    def datetime_2_timestamp(datetime):
        pass

    @staticmethod 
    def timestamp_2_datetime(timestamp):
        if timestamp == None:
            return ""
        
        time_local = time.localtime(timestamp / 1000)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return dt
        
    @staticmethod
    def timestamp_2_date(timestamp):
        time_local = time.localtime(timestamp / 1000)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return dt

import json
import subprocess
from pprint import pprint
from influxdb import InfluxDBClient

# InfluxDB connections settings
host = 'cloudhost'
port = 8086
user = 'root'
password = 'root'
dbname = 'glances'

def main():


    proc = subprocess.Popen('./unifi_get_data.sh', stdout=subprocess.PIPE)
    tmp = proc.stdout.read() 
    data = json.loads(tmp)

    series = []
    for f in data["data"]:
        if 'hostname' in f:
            f["name"]=f["hostname"]
        #pprint(f)
        pointValues = {
                "measurement": 'wifi_clients',
                'fields':  {
                    'rssi': f["rssi"],
                    'rx_bytes': f["rx_bytes"],
                    'tx_bytes': f["rx_bytes"],
                    'noise': f["noise"],
                    'signal': f["signal"],
                    'tx_rate': f["tx_rate"],
                    'rx_rate': f["rx_rate"],
                    'tx_power': f["tx_power"],
                },
                'tags': {
                    'name': f["name"],
                    'client': f["user_id"],
                    'essid': f["essid"],
                    'radio_proto': f["radio_proto"],
                    'channel': f["channel"],
                    'user_id': f["user_id"],
                    'ap_mac': f["ap_mac"],
                },
            }
        series.append(pointValues)
    print(series)
 
    client = InfluxDBClient(host, port, user, password, dbname)
 
#    print("Create a retention policy")
#    retention_policy = 'awesome_policy'
#    client.create_retention_policy(retention_policy, '3d', 3, default=True)
 
    print("Write points #:\n")
    #client.write_points(series, retention_policy=retention_policy)
    client.write_points(series)
 
    #time.sleep(2)
 
    #query = 'SELECT MEAN(value) FROM "%s" WHERE time &amp;amp;gt; now() - 10d GROUP BY time(500m);' % (metric)
    #result = client.query(query, database=DBNAME)
    #print (result)
    #print("Result: {0}".format(result))
 
if __name__ == '__main__':
    main()


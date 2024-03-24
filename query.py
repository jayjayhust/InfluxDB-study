from influxdb_client import InfluxDBClient, QueryApi  # pip install influxdb-client
 
# 配置你的 InfluxDB 2.0 服务器和认证信息
url = "http://localhost:8086"
token = "UKbhzH9_pO3rsMDACHrhfV-qjVHYA0n3MG8FuXrQqq9yoYLlTWzKKUILONCZ8n1ky020LenGg_cXQrpdSiGSdQ=="
org = "jvbenov"
bucket = "jvbenov"
 
# 创建客户端实例
client = InfluxDBClient(url=url, token=token, org=org)
 
# 创建查询API实例
query_api = client.query_api()
 
# 构建查询并指定存储桶和时间范围
query = 'from(bucket:"' + bucket + '")' + \
    ' |> range(start: -1d)' + \
    ' |> filter(fn: (r) => r["_measurement"] == "airSensor")'
# query = 'from(bucket:"' + bucket + '")' + \
#     ' |> range(start: -1d)' + \
#     ' |> filter(fn: (r) => r["_measurement"] == "airSensor")' + \
#     ' |> map(fn: (r) => ({r with state: if r._value < 10 then "ok" else "warning"}))'
# query = 'from(bucket:"' + bucket + '")' + \
#     ' |> range(start: -1d)' + \
#     ' |> filter(fn: (r) => r["_measurement"] == "airSensor")' + \
#     ' |> filter(fn: (r) => r["state"] == "warning")'

# 执行查询
result = query_api.query(query)
 
# 遍历查询结果
for table in result:
    for record in table.records:
        print(f'{record.get_time()}: {record.get_field()}: {record.get_value()}')
 
# 关闭客户端连接
client.close()
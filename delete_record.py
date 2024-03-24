from influxdb_client import InfluxDBClient, Point  # pip install influxdb-client
from influxdb_client.client.write_api import SYNCHRONOUS
 
# 配置您的InfluxDB 2.0访问信息
url = "http://localhost:8086"
token = "UKbhzH9_pO3rsMDACHrhfV-qjVHYA0n3MG8FuXrQqq9yoYLlTWzKKUILONCZ8n1ky020LenGg_cXQrpdSiGSdQ=="
org = "jvbenov"
bucket = "jvbenov"
 
# 创建客户端实例
client = InfluxDBClient(url, token, org)
 
# 创建写入API实例
write_api = client.write_api(write_options=SYNCHRONOUS)
 
# 准备查询删除语句
delete_query = 'from(bucket:"' + bucket + '") |> range(start: -1h) |> filter(fn: (r) => r._measurement == "measurement_name" and r._field == "field_name" and r.tag_key == "tag_value") |> drop()'
 
# 执行删除操作
client.query_api().query(delete_query)
 
# 关闭客户端连接
client.close()

# 请注意，删除操作通常是重要的，因此请谨慎使用，并确保您有适当的备份。此外，删除操作可能会影响查询性能，因为它们会移除数据并可能重写磁盘上的数据文件。
# 在上述代码中，您需要替换url, token, org, 和 bucket 为您的InfluxDB实例的实际信息。delete_query 是InfluxDB的Flux语言编写的删除语句，您需要根据实际情况调整，例如修改时间范围、测量名、字段名和标签值。
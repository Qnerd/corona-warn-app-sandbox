#!/usr/bin/env python3

import requests
import zipfile
import io
#protoc -I . --python_out=generated  src/cwa-server/common/protocols/target/classes/app/coronawarn/server/common/protocols/external/exposurenotification/temporary_exposure_key_export.proto
# check: protoc --decode_raw < 2020-06-27\ \(1\)/decode.bin | more
from generated.temporary_exposure_key_export_pb2 import TemporaryExposureKeyExport

url = "https://svc90.main.px.t-online.de/version/v1/diagnosis-keys/country/DE/date/2020-06-27"

s = requests.Session()
r = s.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
export = z.read('export.bin')
protb = export[16:]	

tek = TemporaryExposureKeyExport()
tek.ParseFromString(protb)

print(tek)

## QingStor Service Class

QingStor Service Class provides QingStor Service API (API Version 2016-01-06)

### Parameters

|Name|Type|Description|
|-|-|-|
|config|Config|Config that initializes a QingStor service|

### Attribute

|Name|Type|Description|
|-|-|-|
|config|Config|Config that initializes a QingStor service|
|client|requests.Session|Client that sends requests|

### Functions

    
### list_buckets_request
Build request for list_buckets


See Also: https://docs.qingcloud.com/qingstor/api/service/get.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|location|string|Limits results to buckets that in the location|

##### Returns

Request: A Request that not signed
### list_buckets
Send list_buckets_request

See Also: https://docs.qingcloud.com/qingstor/api/service/get.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|location|string|Limits results to buckets that in the location|

##### Returns

Unpacker: Server Response that unpacked.

---



#### Bucket

Create a Bucket instance with QingStor service

##### Parameters

|Name|Type|Description|
|-|-|-|
|bucket_name|str|Bucket's name|
|zone|str|Zone's name|

##### Returns

Bucket: Create a Bucket instance






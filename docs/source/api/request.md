## Request

Request which can sign and be sent

### Parameters

|Name|Type|Description|
|-|-|-|
|config|Config|Config that initializes a QingStor service|
|operation|dict|operation built by input|

### Attribute

|Name|Type|Description|
|-|-|-|
|req|Req|Req built bt Builder|
|access_key_id|str|user’s access_key_id|
|secret_access_key|str|user’s secret_access_key|
|logger|Logger|qingstor-sdk logger|

### Functions

#### get_authorization

Get signature authorization by operation

##### Parameters

None

##### Returns

str: signature string

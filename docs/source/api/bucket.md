## Bucket Class

Bucket Class provides Bucket and Object level APIs.

### Parameters

|Name|Type|Description|
|-|-|-|
|config|Config|Config that initializes a Bucket|
|properties|dict|Properties including bucket_name and zone|
|client|requests.Session|Client that sends requests|

### Attribute

|Name|Type|Description|
|-|-|-|
|config|Config|Config that initializes a QingStor service|
|client|requests.Session|Client that sends requests|

### Functions

    
### delete_request
Build request for delete


See Also: https://docs.qingcloud.com/qingstor/api/bucket/delete.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### delete
Send delete_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/delete.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### delete_cors_request
Build request for delete_cors


See Also: https://docs.qingcloud.com/qingstor/api/bucket/cors/delete_cors.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### delete_cors
Send delete_cors_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/cors/delete_cors.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### delete_external_mirror_request
Build request for delete_external_mirror


See Also: https://docs.qingcloud.com/qingstor/api/bucket/external_mirror/delete_external_mirror.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### delete_external_mirror
Send delete_external_mirror_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/external_mirror/delete_external_mirror.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### delete_policy_request
Build request for delete_policy


See Also: https://docs.qingcloud.com/qingstor/api/bucket/policy/delete_policy.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### delete_policy
Send delete_policy_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/policy/delete_policy.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### delete_multiple_objects_request
Build request for delete_multiple_objects


See Also: https://docs.qingcloud.com/qingstor/api/bucket/delete_multiple.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|content_md5|string|Object MD5sum|
|objects|array|A list of keys to delete|
|quiet|boolean|Whether to return the list of deleted objects|

##### Returns

Request: A Request that not signed
### delete_multiple_objects
Send delete_multiple_objects_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/delete_multiple.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|content_md5|string|Object MD5sum|
|objects|array|A list of keys to delete|
|quiet|boolean|Whether to return the list of deleted objects|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### get_acl_request
Build request for get_acl


See Also: https://docs.qingcloud.com/qingstor/api/bucket/get_acl.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### get_acl
Send get_acl_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/get_acl.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### get_cors_request
Build request for get_cors


See Also: https://docs.qingcloud.com/qingstor/api/bucket/cors/get_cors.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### get_cors
Send get_cors_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/cors/get_cors.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### get_external_mirror_request
Build request for get_external_mirror


See Also: https://docs.qingcloud.com/qingstor/api/bucket/external_mirror/get_external_mirror.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### get_external_mirror
Send get_external_mirror_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/external_mirror/get_external_mirror.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### get_policy_request
Build request for get_policy


See Also: https://https://docs.qingcloud.com/qingstor/api/bucket/policy/get_policy.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### get_policy
Send get_policy_request

See Also: https://https://docs.qingcloud.com/qingstor/api/bucket/policy/get_policy.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### get_statistics_request
Build request for get_statistics


See Also: https://docs.qingcloud.com/qingstor/api/bucket/get_stats.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### get_statistics
Send get_statistics_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/get_stats.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### head_request
Build request for head


See Also: https://docs.qingcloud.com/qingstor/api/bucket/head.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### head
Send head_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/head.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### list_multipart_uploads_request
Build request for list_multipart_uploads


See Also: https://docs.qingcloud.com/qingstor/api/bucket/list_multipart_uploads.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|delimiter|string|Put all keys that share a common prefix into a list|
|limit|integer|Results count limit|
|marker|string|Limit results to keys that start at this marker|
|prefix|string|Limits results to keys that begin with the prefix|

##### Returns

Request: A Request that not signed
### list_multipart_uploads
Send list_multipart_uploads_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/list_multipart_uploads.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|delimiter|string|Put all keys that share a common prefix into a list|
|limit|integer|Results count limit|
|marker|string|Limit results to keys that start at this marker|
|prefix|string|Limits results to keys that begin with the prefix|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### list_objects_request
Build request for list_objects


See Also: https://docs.qingcloud.com/qingstor/api/bucket/get.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|delimiter|string|Put all keys that share a common prefix into a list|
|limit|integer|Results count limit|
|marker|string|Limit results to keys that start at this marker|
|prefix|string|Limits results to keys that begin with the prefix|

##### Returns

Request: A Request that not signed
### list_objects
Send list_objects_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/get.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|delimiter|string|Put all keys that share a common prefix into a list|
|limit|integer|Results count limit|
|marker|string|Limit results to keys that start at this marker|
|prefix|string|Limits results to keys that begin with the prefix|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### put_request
Build request for put


See Also: https://docs.qingcloud.com/qingstor/api/bucket/put.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### put
Send put_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/put.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### put_acl_request
Build request for put_acl


See Also: https://docs.qingcloud.com/qingstor/api/bucket/put_acl.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|acl|array|Bucket ACL rules|

##### Returns

Request: A Request that not signed
### put_acl
Send put_acl_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/put_acl.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|acl|array|Bucket ACL rules|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### put_cors_request
Build request for put_cors


See Also: https://docs.qingcloud.com/qingstor/api/bucket/cors/put_cors.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|cors_rules|array|Bucket CORS rules|

##### Returns

Request: A Request that not signed
### put_cors
Send put_cors_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/cors/put_cors.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|cors_rules|array|Bucket CORS rules|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### put_external_mirror_request
Build request for put_external_mirror


See Also: https://docs.qingcloud.com/qingstor/api/bucket/external_mirror/put_external_mirror.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|source_site|string|Source site url|

##### Returns

Request: A Request that not signed
### put_external_mirror
Send put_external_mirror_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/external_mirror/put_external_mirror.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|source_site|string|Source site url|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### put_policy_request
Build request for put_policy


See Also: https://docs.qingcloud.com/qingstor/api/bucket/policy/put_policy.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|statement|array|Bucket policy statement|

##### Returns

Request: A Request that not signed
### put_policy
Send put_policy_request

See Also: https://docs.qingcloud.com/qingstor/api/bucket/policy/put_policy.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|statement|array|Bucket policy statement|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### abort_multipart_upload_request
Build request for abort_multipart_upload


See Also: https://docs.qingcloud.com/qingstor/api/object/abort_multipart_upload.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|upload_id|string|Object multipart upload ID|

##### Returns

Request: A Request that not signed
### abort_multipart_upload
Send abort_multipart_upload_request

See Also: https://docs.qingcloud.com/qingstor/api/object/abort_multipart_upload.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|upload_id|string|Object multipart upload ID|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### complete_multipart_upload_request
Build request for complete_multipart_upload


See Also: https://docs.qingcloud.com/qingstor/api/object/complete_multipart_upload.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|etag|string|MD5sum of the object part|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|
|upload_id|string|Object multipart upload ID|
|object_parts|array|Object parts|

##### Returns

Request: A Request that not signed
### complete_multipart_upload
Send complete_multipart_upload_request

See Also: https://docs.qingcloud.com/qingstor/api/object/complete_multipart_upload.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|etag|string|MD5sum of the object part|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|
|upload_id|string|Object multipart upload ID|
|object_parts|array|Object parts|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### delete_object_request
Build request for delete_object


See Also: https://docs.qingcloud.com/qingstor/api/object/delete.html

##### Parameters
None

##### Returns

Request: A Request that not signed
### delete_object
Send delete_object_request

See Also: https://docs.qingcloud.com/qingstor/api/object/delete.html

##### Parameters
None

##### Returns

Unpacker: Server Response that unpacked.

---



    
### get_object_request
Build request for get_object


See Also: https://docs.qingcloud.com/qingstor/api/object/get.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|if_match|string|Check whether the ETag matches|
|if_modified_since|timestamp|Check whether the object has been modified|
|if_none_match|string|Check whether the ETag does not match|
|if_unmodified_since|timestamp|Check whether the object has not been modified|
|range|string|Specified range of the object|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|
|response_cache_control|string|Specified the Cache-Control response header|
|response_content_disposition|string|Specified the Content-Disposition response header|
|response_content_encoding|string|Specified the Content-Encoding response header|
|response_content_language|string|Specified the Content-Language response header|
|response_content_type|string|Specified the Content-Type response header|
|response_expires|string|Specified the Expires response header|

##### Returns

Request: A Request that not signed
### get_object
Send get_object_request

See Also: https://docs.qingcloud.com/qingstor/api/object/get.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|if_match|string|Check whether the ETag matches|
|if_modified_since|timestamp|Check whether the object has been modified|
|if_none_match|string|Check whether the ETag does not match|
|if_unmodified_since|timestamp|Check whether the object has not been modified|
|range|string|Specified range of the object|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|
|response_cache_control|string|Specified the Cache-Control response header|
|response_content_disposition|string|Specified the Content-Disposition response header|
|response_content_encoding|string|Specified the Content-Encoding response header|
|response_content_language|string|Specified the Content-Language response header|
|response_content_type|string|Specified the Content-Type response header|
|response_expires|string|Specified the Expires response header|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### head_object_request
Build request for head_object


See Also: https://docs.qingcloud.com/qingstor/api/object/head.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|if_match|string|Check whether the ETag matches|
|if_modified_since|timestamp|Check whether the object has been modified|
|if_none_match|string|Check whether the ETag does not match|
|if_unmodified_since|timestamp|Check whether the object has not been modified|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|

##### Returns

Request: A Request that not signed
### head_object
Send head_object_request

See Also: https://docs.qingcloud.com/qingstor/api/object/head.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|if_match|string|Check whether the ETag matches|
|if_modified_since|timestamp|Check whether the object has been modified|
|if_none_match|string|Check whether the ETag does not match|
|if_unmodified_since|timestamp|Check whether the object has not been modified|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### initiate_multipart_upload_request
Build request for initiate_multipart_upload


See Also: https://docs.qingcloud.com/qingstor/api/object/initiate_multipart_upload.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|content_type|string|Object content type|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|

##### Returns

Request: A Request that not signed
### initiate_multipart_upload
Send initiate_multipart_upload_request

See Also: https://docs.qingcloud.com/qingstor/api/object/initiate_multipart_upload.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|content_type|string|Object content type|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### list_multipart_request
Build request for list_multipart


See Also: https://docs.qingcloud.com/qingstor/api/object/list_multipart.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|limit|integer|Limit results count|
|part_number_marker|integer|Object multipart upload part number|
|upload_id|string|Object multipart upload ID|

##### Returns

Request: A Request that not signed
### list_multipart
Send list_multipart_request

See Also: https://docs.qingcloud.com/qingstor/api/object/list_multipart.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|limit|integer|Limit results count|
|part_number_marker|integer|Object multipart upload part number|
|upload_id|string|Object multipart upload ID|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### options_object_request
Build request for options_object


See Also: https://docs.qingcloud.com/qingstor/api/object/options.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|access_control_request_headers|string|Request headers|
|access_control_request_method|string|Request method|
|origin|string|Request origin|

##### Returns

Request: A Request that not signed
### options_object
Send options_object_request

See Also: https://docs.qingcloud.com/qingstor/api/object/options.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|access_control_request_headers|string|Request headers|
|access_control_request_method|string|Request method|
|origin|string|Request origin|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### put_object_request
Build request for put_object


See Also: https://docs.qingcloud.com/qingstor/api/object/put.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|content_length|long|Object content size|
|content_md5|string|Object MD5sum|
|content_type|string|Object content type|
|expect|string|Used to indicate that particular server behaviors are required by the client|
|x_qs_copy_source|string|Copy source, format (/<bucket-name>/<object-key>)|
|x_qs_copy_source_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_copy_source_encryption_customer_key|string|Encryption key of the object|
|x_qs_copy_source_encryption_customer_key_md5|string|MD5sum of encryption key|
|x_qs_copy_source_if_match|string|Check whether the copy source matches|
|x_qs_copy_source_if_modified_since|timestamp|Check whether the copy source has been modified|
|x_qs_copy_source_if_none_match|string|Check whether the copy source does not match|
|x_qs_copy_source_if_unmodified_since|timestamp|Check whether the copy source has not been modified|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|
|x_qs_fetch_if_unmodified_since|timestamp|Check whether fetch target object has not been modified|
|x_qs_fetch_source|string|Fetch source, should be a valid url|
|x_qs_move_source|string|Move source, format (/<bucket-name>/<object-key>)|

##### Returns

Request: A Request that not signed
### put_object
Send put_object_request

See Also: https://docs.qingcloud.com/qingstor/api/object/put.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|content_length|long|Object content size|
|content_md5|string|Object MD5sum|
|content_type|string|Object content type|
|expect|string|Used to indicate that particular server behaviors are required by the client|
|x_qs_copy_source|string|Copy source, format (/<bucket-name>/<object-key>)|
|x_qs_copy_source_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_copy_source_encryption_customer_key|string|Encryption key of the object|
|x_qs_copy_source_encryption_customer_key_md5|string|MD5sum of encryption key|
|x_qs_copy_source_if_match|string|Check whether the copy source matches|
|x_qs_copy_source_if_modified_since|timestamp|Check whether the copy source has been modified|
|x_qs_copy_source_if_none_match|string|Check whether the copy source does not match|
|x_qs_copy_source_if_unmodified_since|timestamp|Check whether the copy source has not been modified|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|
|x_qs_fetch_if_unmodified_since|timestamp|Check whether fetch target object has not been modified|
|x_qs_fetch_source|string|Fetch source, should be a valid url|
|x_qs_move_source|string|Move source, format (/<bucket-name>/<object-key>)|

##### Returns

Unpacker: Server Response that unpacked.

---



    
### upload_multipart_request
Build request for upload_multipart


See Also: https://docs.qingcloud.com/qingstor/api/object/multipart/upload_multipart.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|content_length|long|Object multipart content length|
|content_md5|string|Object multipart content MD5sum|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|
|part_number|integer|Object multipart upload part number|
|upload_id|string|Object multipart upload ID|

##### Returns

Request: A Request that not signed
### upload_multipart
Send upload_multipart_request

See Also: https://docs.qingcloud.com/qingstor/api/object/multipart/upload_multipart.html

##### Parameters
|Name|Type|Description|
|-|-|-|
|object_key|str|Object key name|
|content_length|long|Object multipart content length|
|content_md5|string|Object multipart content MD5sum|
|x_qs_encryption_customer_algorithm|string|Encryption algorithm of the object|
|x_qs_encryption_customer_key|string|Encryption key of the object|
|x_qs_encryption_customer_key_md5|string|MD5sum of encryption key|
|part_number|integer|Object multipart upload part number|
|upload_id|string|Object multipart upload ID|

##### Returns

Unpacker: Server Response that unpacked.

---








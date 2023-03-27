# API Wrapper for OGC API EDR
## How to use

```
edr = EDRWrapper("http://example.org/v1.0/")

# show functions of EDRWrapper
edr.help
output: 
get_Collection(input_collectionId: Optional, query_option: Optional), get_Instance(query_option: str, input_collectionId: Optional, input_instanceId: Optional), get_CollectionItem_byId(itemId: str), get_CollectionLocation_byId(locId: str), set_CollectionId(collectionId: str), set_InstanceId(instanceId: str)"
query_options: instances, position, radius, area, cube, trajectory, corridor, items, locations

# example
edr.set_CollectionId("ab12cd")
edr.get_Collection()
```

## API provided in EDR


1. https://ogcapi.ogc.org/edr/

1. https://docs.ogc.org/is/19-086r5/19-086r5.html

1. https://app.swaggerhub.com/apis/OGC/ogcapi-edr-1-example-1/1.0.1#/Capabilities/listCollections


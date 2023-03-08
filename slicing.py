property_transfer_xml = """//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare 
namespace urn='urn:Magento';"""
result = property_transfer_xml.split("con:targetType")[1][1:-2]
print(result)

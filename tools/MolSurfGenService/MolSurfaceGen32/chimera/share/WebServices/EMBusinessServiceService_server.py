##################################################
# file: EMBusinessServiceService_server.py
#
# skeleton generated by "ZSI.generate.wsdl2dispatch.ServiceModuleWriter"
#      /home/chimera/chimeraBuild_OSMESA/build/build/bin/wsdl2py EMBusinessService.wsdl
#
##################################################

from ZSI.schema import GED, GTD
from ZSI.TCcompound import ComplexType, Struct
from EMBusinessServiceService_types import *
from ZSI.ServiceContainer import ServiceSOAPBinding

# Messages  
findContourLevelByAccessionCodeRequest = GED("http://service.emsearch.rcsb", "findContourLevelByAccessionCode").pyclass

findContourLevelByAccessionCodeResponse = GED("http://service.emsearch.rcsb", "findContourLevelByAccessionCodeResponse").pyclass

findFittedPDBidsByAccessionCodeRequest = GED("http://service.emsearch.rcsb", "findFittedPDBidsByAccessionCode").pyclass

findFittedPDBidsByAccessionCodeResponse = GED("http://service.emsearch.rcsb", "findFittedPDBidsByAccessionCodeResponse").pyclass

getResultSetXMLByAuthorRequest = GED("http://service.emsearch.rcsb", "getResultSetXMLByAuthor").pyclass

getResultSetXMLByAuthorResponse = GED("http://service.emsearch.rcsb", "getResultSetXMLByAuthorResponse").pyclass

getResultSetXMLByIDRequest = GED("http://service.emsearch.rcsb", "getResultSetXMLByID").pyclass

getResultSetXMLByIDResponse = GED("http://service.emsearch.rcsb", "getResultSetXMLByIDResponse").pyclass

getResultSetXMLByTitleRequest = GED("http://service.emsearch.rcsb", "getResultSetXMLByTitle").pyclass

getResultSetXMLByTitleResponse = GED("http://service.emsearch.rcsb", "getResultSetXMLByTitleResponse").pyclass


# Service Skeletons
class EMBusinessServiceService(ServiceSOAPBinding):
    soapAction = {}
    root = {}

    def __init__(self, post='/EMSearchWS/services/EMBusinessService', **kw):
        ServiceSOAPBinding.__init__(self, post)

    def soap_findContourLevelByAccessionCode(self, ps, **kw):
        request = ps.Parse(findContourLevelByAccessionCodeRequest.typecode)
        return request,findContourLevelByAccessionCodeResponse()

    soapAction[''] = 'soap_findContourLevelByAccessionCode'
    root[(findContourLevelByAccessionCodeRequest.typecode.nspname,findContourLevelByAccessionCodeRequest.typecode.pname)] = 'soap_findContourLevelByAccessionCode'

    def soap_findFittedPDBidsByAccessionCode(self, ps, **kw):
        request = ps.Parse(findFittedPDBidsByAccessionCodeRequest.typecode)
        return request,findFittedPDBidsByAccessionCodeResponse()

    soapAction[''] = 'soap_findFittedPDBidsByAccessionCode'
    root[(findFittedPDBidsByAccessionCodeRequest.typecode.nspname,findFittedPDBidsByAccessionCodeRequest.typecode.pname)] = 'soap_findFittedPDBidsByAccessionCode'

    def soap_getResultSetXMLByAuthor(self, ps, **kw):
        request = ps.Parse(getResultSetXMLByAuthorRequest.typecode)
        return request,getResultSetXMLByAuthorResponse()

    soapAction[''] = 'soap_getResultSetXMLByAuthor'
    root[(getResultSetXMLByAuthorRequest.typecode.nspname,getResultSetXMLByAuthorRequest.typecode.pname)] = 'soap_getResultSetXMLByAuthor'

    def soap_getResultSetXMLByID(self, ps, **kw):
        request = ps.Parse(getResultSetXMLByIDRequest.typecode)
        return request,getResultSetXMLByIDResponse()

    soapAction[''] = 'soap_getResultSetXMLByID'
    root[(getResultSetXMLByIDRequest.typecode.nspname,getResultSetXMLByIDRequest.typecode.pname)] = 'soap_getResultSetXMLByID'

    def soap_getResultSetXMLByTitle(self, ps, **kw):
        request = ps.Parse(getResultSetXMLByTitleRequest.typecode)
        return request,getResultSetXMLByTitleResponse()

    soapAction[''] = 'soap_getResultSetXMLByTitle'
    root[(getResultSetXMLByTitleRequest.typecode.nspname,getResultSetXMLByTitleRequest.typecode.pname)] = 'soap_getResultSetXMLByTitle'


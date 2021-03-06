##################################################
# file: EMDB_response_xsd_types.py
#
# schema types generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#    /home/chimera/chimeraBuild_OSMESA/build/build/bin/wsdl2py -x EMDB_response.xsd
#
##################################################

import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED

##############################
# targetNamespace
# 
##############################

class ns0:
    targetNamespace = ""

    class resultset_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "resultset"
        schema = ""
        def __init__(self, **kw):
            ns = ns0.resultset_Dec.schema
            TClist = [self.__class__.row_Dec(minOccurs=0, maxOccurs="unbounded", nillable=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("","resultset")
            kw["aname"] = "_resultset"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                typecode = self
                def __init__(self):
                    # pyclass
                    self._row = []
                    return
            Holder.__name__ = "resultset_Holder"
            self.pyclass = Holder


        class row_Dec(ZSI.TCcompound.ComplexType, LocalElementDeclaration):
            literal = "row"
            schema = ""
            def __init__(self, **kw):
                ns = ns0.resultset_Dec.row_Dec.schema
                TClist = [ZSI.TC.String(pname="accessionCode", aname="_accessionCode", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="sampleName", aname="_sampleName", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="mapReleaseDate", aname="_mapReleaseDate", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="resolution", aname="_resolution", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="fittedPDBidList", aname="_fittedPDBidList", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="title", aname="_title", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="citationAuthorList", aname="_citationAuthorList", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="citationJournalName", aname="_citationJournalName", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="citationJournalVolume", aname="_citationJournalVolume", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="citationJournalFirstPage", aname="_citationJournalFirstPage", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="citationJournalLastPage", aname="_citationJournalLastPage", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="citationJournalYear", aname="_citationJournalYear", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="contour", aname="_contour", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname="fittedPDBid", aname="_fittedPDBid", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
                kw["pname"] = ("","row")
                kw["aname"] = "_row"
                self.attribute_typecode_dict = {}
                ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
                class Holder:
                    typecode = self
                    def __init__(self):
                        # pyclass
                        self._accessionCode = None
                        self._sampleName = None
                        self._mapReleaseDate = None
                        self._resolution = None
                        self._fittedPDBidList = None
                        self._title = None
                        self._citationAuthorList = None
                        self._citationJournalName = None
                        self._citationJournalVolume = None
                        self._citationJournalFirstPage = None
                        self._citationJournalLastPage = None
                        self._citationJournalYear = None
                        self._contour = None
                        self._fittedPDBid = None
                        return
                Holder.__name__ = "row_Holder"
                self.pyclass = Holder




# end class ns0 (tns: )

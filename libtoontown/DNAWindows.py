
class DNAWindows:

    def __init__(self):
        self.code = None
        self.color = None
        self.count = None
        

    def getCode(self):
        return self.code

    def getColor(self):
        return self.color

    def getWindowCount(self):
        return self.count

    def setCode(self, cod):
        self.code = cod

    def setColor(self, col):
        self.color = col

    def setWindowCount(self, cnt):
        self.windowCount = cnt

## REFERENCE ##
"""
    class DNAWindows(DNAGroup)
     |  Method resolution order:
     |      DNAWindows
     |      DNAGroup
     |      libpandaexpress.TypedReferenceCount
     |      libpandaexpress.TypedObject
     |      libpandaexpress.ReferenceCount
     |      libpandaexpress.Namable
     |      libdtoolconfig.DTOOL_SUPPER_BASE111
     |      __builtin__.object
     |  
     |  Methods defined here:
     |  
     |  __copy__(...)
     |  
     |  __deepcopy__(...)
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see x.__class__.__doc__ for signature
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  getCode(...)
     |  
     |  getColor(...)
     |  
     |  getWindowCount(...)
     |  
     |  setCode(...)
     |  
     |  setColor(...)
     |  
     |  setWindowCount(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  DNAWindows = <type 'libtoontown.DNAWindows'>
     |  
     |  
     |  DtoolClassDict = {'DNAWindows': <type 'libtoontown.DNAWindows'>, 'Dtoo...
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  getClassType = <built-in method getClassType of type object>
     |  
     |  
     |  this = <member 'this' of 'libtoontown.DNAWindows' objects>
     |      C++ This if any
     |  
     |  this_metatype = <member 'this_metatype' of 'libtoontown.DNAWindows' ob...
     |      The dtool meta object
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from DNAGroup:
     |  
     |  add(...)
     |  
     |  at(...)
     |  
     |  current(...)
     |  
     |  getNumChildren(...)
     |  
     |  getParent(...)
     |  
     |  ls(...)
     |  
     |  remove(...)
     |  
     |  topLevelTraverse(...)
     |  
     |  traverse(...)
     |  
     |  upcastToNamable(...)
     |  
     |  upcastToTypedReferenceCount(...)
     |  
     |  write(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from DNAGroup:
     |  
     |  DNAGroup = <type 'libtoontown.DNAGroup'>
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from libpandaexpress.TypedReferenceCount:
     |  
     |  upcastToReferenceCount(...)
     |  
     |  upcastToTypedObject(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from libpandaexpress.TypedReferenceCount:
     |  
     |  TypedReferenceCount = <type 'libpandaexpress.TypedReferenceCount'>
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from libpandaexpress.TypedObject:
     |  
     |  downcastToTypedReferenceCount(...)
     |  
     |  getType(...)
     |  
     |  getTypeIndex(...)
     |  
     |  isExactType(...)
     |  
     |  isOfType(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from libpandaexpress.TypedObject:
     |  
     |  TypedObject = <type 'libpandaexpress.TypedObject'>
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from libpandaexpress.ReferenceCount:
     |  
     |  getRefCount(...)
     |  
     |  ref(...)
     |  
     |  testRefCountIntegrity(...)
     |  
     |  testRefCountNonzero(...)
     |  
     |  unref(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from libpandaexpress.ReferenceCount:
     |  
     |  ReferenceCount = <type 'libpandaexpress.ReferenceCount'>
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from libpandaexpress.Namable:
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  assign(...)
     |  
     |  clearName(...)
     |  
     |  getName(...)
     |  
     |  hasName(...)
     |  
     |  output(...)
     |  
     |  setName(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from libpandaexpress.Namable:
     |  
     |  Namable = <type 'libpandaexpress.Namable'>
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from libdtoolconfig.DTOOL_SUPPER_BASE111:
     |  
     |  __cmp__(...)
     |      x.__cmp__(y) <==> cmp(x,y)
     |  
     |  __hash__(...)
     |      x.__hash__() <==> hash(x)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from libdtoolconfig.DTOOL_SUPPER_BASE111:
     |  
     |  DtoolGetSupperBase = <built-in method DtoolGetSupperBase of type objec...
     |      Will Return SUPPERbase Class
"""

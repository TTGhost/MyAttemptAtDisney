from panda3d.core import *

class SeaPatchNode(NodePath):
    def __init__(self, name, patchRoot):
        NodePath.__init__(self, name)
        self.name = name
        self.patchRoot = patchRoot
        self.wantColor = False
        self.wantNormal = False
        self.wantReflect = False
        self.wantUv = False
        self.wantZ = False
        self.ZOffset = 0

    def collectGeometry(self):
        pass

    def getWantColor(self):
        return self.wantColor

    def getWantNormal(self):
        return self.wantNormal

    def getWantReflect(self):
        return self.wantReflect

    def getWantUv(self):
        return self.wantUv

    def getWantZ(self):
        return self.wantZ

    def getZOffset(self):
        return self.ZOffset

    def setWantColor(self, color):
        self.wantColor = color

    def setWantNormal(self, normal):
        self.wantNormal = normal

    def setWantReflect(self, reflect):
        self.wantReflect = reflect

    def setWantUv(self, uv):
        self.wantUv = uv

    def setWantZ(self, z):
        self.wantZ = z

    def setZOffset(self, zoff):
        self.ZOffset = zoff

    def turnOff(self):
        pass

    def turnOn(self):
        pass

    def update(self):
        pass

## REFERENCE ##
"""
    class SeaPatchNode(libpanda.PandaNode)
     |  Method resolution order:
     |      SeaPatchNode
     |      libpanda.PandaNode
     |      libpanda.TypedWritable
     |      libpandaexpress.TypedObject
     |      libpandaexpress.Namable
     |      libpandaexpress.ReferenceCount
     |      libdtoolconfig.DTOOL_SUPPER_BASE111
     |      __builtin__.object
     |  
     |  Methods defined here:
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
     |  collectGeometry(...)
     |  
     |  getWantColor(...)
     |  
     |  getWantNormal(...)
     |  
     |  getWantReflect(...)
     |  
     |  getWantUv(...)
     |  
     |  getWantZ(...)
     |  
     |  getZOffset(...)
     |  
     |  setWantColor(...)
     |  
     |  setWantNormal(...)
     |  
     |  setWantReflect(...)
     |  
     |  setWantUv(...)
     |  
     |  setWantZ(...)
     |  
     |  setZOffset(...)
     |  
     |  turnOff(...)
     |  
     |  turnOn(...)
     |  
     |  update(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  DtoolClassDict = {'DtoolClassDict': {'DtoolClassDict': {'DtoolClassDic...
     |  
     |  SeaPatchNode = <type 'libpirates.SeaPatchNode'>
     |  
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  getClassType = <built-in method getClassType of type object>
     |  
     |  
     |  this = <member 'this' of 'libpirates.SeaPatchNode' objects>
     |      C++ This if any
     |  
     |  this_metatype = <member 'this_metatype' of 'libpirates.SeaPatchNode' o...
     |      The dtool meta object
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from libpanda.PandaNode:
     |  
     |  __copy__(...)
     |  
     |  __deepcopy__(...)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  addChild(...)
     |  
     |  addStashed(...)
     |  
     |  adjustDrawMask(...)
     |  
     |  asLight(...)
     |  
     |  clearAttrib(...)
     |  
     |  clearBounds(...)
     |  
     |  clearEffect(...)
     |  
     |  clearEffects(...)
     |  
     |  clearPythonTag(...)
     |  
     |  clearState(...)
     |  
     |  clearTag(...)
     |  
     |  clearTransform(...)
     |  
     |  clearUnexpectedChange(...)
     |  
     |  combineWith(...)
     |  
     |  compareTags(...)
     |  
     |  copyAllProperties(...)
     |  
     |  copyChildren(...)
     |  
     |  copySubgraph(...)
     |  
     |  copyTags(...)
     |  
     |  countNumDescendants(...)
     |  
     |  findChild(...)
     |  
     |  findParent(...)
     |  
     |  findStashed(...)
     |  
     |  getAttrib(...)
     |  
     |  getBounds(...)
     |  
     |  getBoundsType(...)
     |  
     |  getChild(...)
     |  
     |  getChildSort(...)
     |  
     |  getDrawControlMask(...)
     |  
     |  getDrawShowMask(...)
     |  
     |  getEffect(...)
     |  
     |  getEffects(...)
     |  
     |  getFancyBits(...)
     |  
     |  getInternalBounds(...)
     |  
     |  getInternalVertices(...)
     |  
     |  getIntoCollideMask(...)
     |  
     |  getLegalCollideMask(...)
     |  
     |  getNestedVertices(...)
     |  
     |  getNetCollideMask(...)
     |  
     |  getNetDrawControlMask(...)
     |  
     |  getNetDrawShowMask(...)
     |  
     |  getNumChildren(...)
     |  
     |  getNumParents(...)
     |  
     |  getNumStashed(...)
     |  
     |  getOffClipPlanes(...)
     |  
     |  getParent(...)
     |  
     |  getPrevTransform(...)
     |  
     |  getPythonTag(...)
     |  
     |  getStashed(...)
     |  
     |  getStashedSort(...)
     |  
     |  getState(...)
     |  
     |  getTag(...)
     |  
     |  getTransform(...)
     |  
     |  getUnexpectedChange(...)
     |  
     |  hasAttrib(...)
     |  
     |  hasDirtyPrevTransform(...)
     |  
     |  hasEffect(...)
     |  
     |  hasPythonTag(...)
     |  
     |  hasTag(...)
     |  
     |  hasTags(...)
     |  
     |  isAmbientLight(...)
     |  
     |  isBoundsStale(...)
     |  
     |  isFinal(...)
     |  
     |  isGeomNode(...)
     |  
     |  isLodNode(...)
     |  
     |  isOverallHidden(...)
     |  
     |  isSceneRoot(...)
     |  
     |  isUnderSceneRoot(...)
     |  
     |  listTags(...)
     |  
     |  ls(...)
     |  
     |  makeCopy(...)
     |  
     |  markBoundsStale(...)
     |  
     |  markInternalBoundsStale(...)
     |  
     |  output(...)
     |  
     |  prepareScene(...)
     |  
     |  removeAllChildren(...)
     |  
     |  removeChild(...)
     |  
     |  removeStashed(...)
     |  
     |  replaceChild(...)
     |  
     |  replaceNode(...)
     |  
     |  resetPrevTransform(...)
     |  
     |  setAttrib(...)
     |  
     |  setBound(...)
     |  
     |  setBounds(...)
     |  
     |  setBoundsType(...)
     |  
     |  setEffect(...)
     |  
     |  setEffects(...)
     |  
     |  setFinal(...)
     |  
     |  setIntoCollideMask(...)
     |  
     |  setOverallHidden(...)
     |  
     |  setPrevTransform(...)
     |  
     |  setPythonTag(...)
     |  
     |  setState(...)
     |  
     |  setTag(...)
     |  
     |  setTransform(...)
     |  
     |  setUnexpectedChange(...)
     |  
     |  stashChild(...)
     |  
     |  stealChildren(...)
     |  
     |  unstashChild(...)
     |  
     |  upcastToNamable(...)
     |  
     |  upcastToReferenceCount(...)
     |  
     |  upcastToTypedWritable(...)
     |  
     |  write(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from libpanda.PandaNode:
     |  
     |  FBCullCallback = 64
     |  
     |  FBDrawMask = 32
     |  
     |  FBEffects = 4
     |  
     |  FBState = 2
     |  
     |  FBTag = 16
     |  
     |  FBTransform = 1
     |  
     |  PandaNode = <type 'libpanda.PandaNode'>
     |  
     |  
     |  UCChildren = 2
     |  
     |  UCDrawMask = 16
     |  
     |  UCParents = 1
     |  
     |  UCState = 8
     |  
     |  UCTransform = 4
     |  
     |  decodeFromBamStream = <built-in method decodeFromBamStream of type obj...
     |  
     |  
     |  getAllCameraMask = <built-in method getAllCameraMask of type object>
     |  
     |  
     |  getOverallBit = <built-in method getOverallBit of type object>
     |  
     |  
     |  resetAllPrevTransform = <built-in method resetAllPrevTransform of type...
     |  
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from libpanda.TypedWritable:
     |  
     |  __reduce__(...)
     |  
     |  __reduce_persist__(...)
     |  
     |  downcastToTypedWritableReferenceCount(...)
     |  
     |  encodeToBamStream(...)
     |  
     |  getBamModified(...)
     |  
     |  markBamModified(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from libpanda.TypedWritable:
     |  
     |  TypedWritable = <type 'libpanda.TypedWritable'>
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
     |  Methods inherited from libpandaexpress.Namable:
     |  
     |  assign(...)
     |  
     |  clearName(...)
     |  
     |  getName(...)
     |  
     |  hasName(...)
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

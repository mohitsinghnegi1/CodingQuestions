class File(object):

    def __init__(object, name, content=""):
        self.name = name
        self.size = len(content)
        self.content = content

    def getName(self):
        return self.name

    def getExt(self):
        return self.name.split('.')[-1]

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

    def setContent(self, content):
        self.content = content
        self.setSize(len(content))

    def rename(self, name):
        self.name = name

    def getInfo(self, op):

        switch(op):
            case 'size':
                print self.getSize()
                return
            case 'type':
                print self.getExt()
                return
            case 'content':
                print self.getContent()
                return
            default:
                print 'Invalid Operator'


class Directory(object):

    def __init__(object, name):
        self.name = name
        self.files = {}
        self.subDirectories = {}
        self.size = 0

    def createNewFile(self, name, content=""):
        # create new file
        file = File(name, content)
        # add file to current directory
        self.files[name] = file
        # update the size of directory
        self.size += file.getSize()

    def removeFile(self, name):
        if(not self.files.get(name, False)):
            return 'File does not exist!!'
        del self.files[name]

    def createNewSubDirectory(self, name):
        directory = Directory(name)
        # update directory to subdirectories
        self.subDirectories[name] = directory

    def removeSubDirectory(self, name):
        if(not self.subDirectories.get(name, False)):
            return 'Subdirectory does not exist!!'
        del self.subDirectories[name]

    def getName(self):
        return self.name

    def getSize(self):
        return self.size

    def getSubDirectories(self):
        return self.subDirectories

    def isSubDirectoryExist(self, name):
        return self.subDirectories.get(name, False)

    def getSubDirectory(self, name):
        return self.subDirectories.get(name)

    def getFiles(self):
        return self.files

    def isFileExist(self, name):
        return self.files.get(name, False)

    def getFile(self, name):
        return self.files[name]

    def filesGreaterThan(self, val):
        out = []  # array of Files

        for file in self.files:
            if(self.files[file].getSize() > val):
                out.append(file)
        return out

    def filesLessThan(self, val):
        out = []  # array of Files

        for file in self.files:
            if(self.files[file].getSize() < val):
                out.append(file)
        return out

    def findFiles(self, op, val):

        switch(op):
            case 'gt':
                return filesGreaterThan(val)
            case 'lt':
                return filesLessThan(val)
            default:
                print('Invalid operator')
        return []

    def getInfo(self, op):

        switch(op):
            case 'size':
                print self.getSize()
                return
            default:
                print "invalid operator"


class DirectoryManager(object):

    def __init__(self):
        self.rootDirectory = Directory('root')

    def getInstance():
        if(self.instance):
            return self.instance
        self.instance = DirectoryManager()
        return self.instance

    def goToLastDirectory(self, path):
        if(len(path) < 0):
            return False

        if(path[0] == self.rootDirectory.getName()):

            par = Directory('root')
            i = 1
            while(i < len(path)):

                if(path[i] in par.subDirectories):
                    par = par.subDirectories[path[i]]
                else:
                    print 'Subdirectory does not exist'
                    return False

                i += 1
             # we reach to the last subdirectory
            return par

        print "invalid path"
        return False

    def find(path, op, val):

        currentDirectory = goToLastDirectory(path)
        # if directory does not exit then return empty array
        if(currentDirectory == False):
            return []

        return currentDirectory.findFiles(op, val)

    def getInfoOfDir(path, op):
        currentDirectory = goToLastDirectory(path)
        currentDirectory.getInfo(op)

    def getInfo(path, filnameExt, op):
        currentDirectory = goToLastDirectory(path)
        if(not currentDirectory.isFileExist(filenameExt)):
            print "File with given name does not exist"
            return
        currentDirectory.getFile(name).getInfo(op)


dm = DirectoryManager()
dm.find(['root', 'downloads'], 'gt', 5)  # find a files inside this directory
dm.getInfoOfDir(['root', 'downloads'], 'size')
dm.getInfo(['root', 'downloads'], 'filename.ext', 'size')
